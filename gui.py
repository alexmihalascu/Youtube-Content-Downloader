import tkinter as tk
from tkinter import filedialog, messagebox
from downloader import download_video, convert_to_mp3

def create_gui(root):
    def download():
        url = url_entry.get()
        resolution = resolution_var.get()
        download_path = filedialog.askdirectory()
        if not download_path:
            messagebox.showerror("Error", "No download path selected.")
            return
        try:
            video_path = download_video(url, resolution, download_path)
            messagebox.showinfo("Success", f"Video downloaded at {video_path}")
            if convert_var.get():
                audio_path = convert_to_mp3(video_path)
                messagebox.showinfo("Success", f"Audio extracted at {audio_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # GUI setup
    root.title("YouTube Content Downloader")

    logo_label = tk.Label(root, text="🎥")
    logo_label.pack()
    title_label = tk.Label(root, text="YouTube Content Downloader")
    title_label.pack()

    url_label = tk.Label(root, text="Insert YouTube video link:")
    url_label.pack()
    url_entry = tk.Entry(root, width=50)
    url_entry.pack()

    resolution_var = tk.StringVar(value='720p')
    resolution_label = tk.Label(root, text="Select video resolution:")
    resolution_label.pack()
    resolution_dropdown = tk.OptionMenu(root, resolution_var, '720p', '480p', '360p')
    resolution_dropdown.pack()

    convert_var = tk.BooleanVar()
    convert_check = tk.Checkbutton(root, text="Download as MP3", variable=convert_var)
    convert_check.pack()

    download_button = tk.Button(root, text="Download", command=download)
    download_button.pack()
