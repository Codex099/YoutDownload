import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox
from threading import Thread

def update_progress(d):
    if d['status'] == 'downloading':
        percent = float(d.get('_percent_str', '0%').replace('%', ''))
        progress_var.set(percent)
        progress_bar.update()

def download():
    url = url_entry.get()
    quality = var_quality.get()
    folder = folder_var.get()
    if not url or not folder:
        messagebox.showerror("Erreur", "Veuillez entrer l'URL et choisir un dossier.")
        return

    # Format yt-dlp pour la qualité vidéo choisie
    ydl_opts = {
        'format': f'bestvideo[height<={quality}]',
        'outtmpl': f'{folder}/%(title)s.%(ext)s',
        'progress_hooks': [update_progress],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Succès", "Téléchargement terminé !")
        progress_var.set(0)
    except Exception as e:
        messagebox.showerror("Erreur", str(e))
        progress_var.set(0)

def start_download():
    Thread(target=download).start()

def choose_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_var.set(folder)

root = tk.Tk()
root.title("Téléchargeur YouTube Vidéo")

tk.Label(root, text="URL de la vidéo YouTube :").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Label(root, text="Dossier de téléchargement :").pack()
folder_var = tk.StringVar()
folder_frame = tk.Frame(root)
folder_frame.pack(pady=5)
tk.Entry(folder_frame, textvariable=folder_var, width=40).pack(side=tk.LEFT, padx=5)
tk.Button(folder_frame, text="Choisir...", command=choose_folder).pack(side=tk.LEFT)

tk.Label(root, text="Qualité vidéo :").pack()
var_quality = tk.StringVar(value="720")
tk.OptionMenu(root, var_quality, "360", "480", "720", "1080").pack(pady=5)

tk.Label(root, text="Progression du téléchargement :").pack(pady=5)
progress_var = tk.DoubleVar()
progress_bar = tk.Scale(root, variable=progress_var, from_=0, to=100, orient=tk.HORIZONTAL, length=300, showvalue=0,)
progress_bar.pack(pady=5)

tk.Button(root, text="Télécharger", command=start_download).pack(pady=10)

root.mainloop()