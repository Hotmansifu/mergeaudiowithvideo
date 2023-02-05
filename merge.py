import tkinter as tk
import tkinter.filedialog as fd
import moviepy.editor as mp

def browse_video():
    video_file = fd.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi")])
    video_file_entry.delete(0, tk.END)
    video_file_entry.insert(0, video_file)

def browse_audio():
    audio_file = fd.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    audio_file_entry.delete(0, tk.END)
    audio_file_entry.insert(0, audio_file)

def merge():
    video_file = video_file_entry.get()
    audio_file = audio_file_entry.get()
    start_time = int(start_time_entry.get())

    video = mp.VideoFileClip(video_file)
    audio = mp.AudioFileClip(audio_file)

    video = video.set_start(start_time)

    if audio.duration > video.duration:
        audio = audio.subclip(0, video.duration)

    video = video.set_audio(audio)

    save_file = fd.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 Video", "*.mp4")])
    video.write_videofile(save_file)

    status_label.config(text="Video merged successfully.")


root = tk.Tk()
root.title("Merge Video and Audio")

video_file_label = tk.Label(root, text="Video file path:")
video_file_entry = tk.Entry(root)
video_file_browse_button = tk.Button(root, text="Browse", command=browse_video)

audio_file_label = tk.Label(root, text="Audio file path:")
audio_file_entry = tk.Entry(root)
audio_file_browse_button = tk.Button(root, text="Browse", command=browse_audio)

start_time_label = tk.Label(root, text="Start time (seconds):")
start_time_entry = tk.Entry(root)

merge_button = tk.Button(root, text="Merge", command=merge)

status_label = tk.Label(root, text="")

video_file_label.pack()
video_file_entry.pack()
video_file_browse_button.pack()

audio_file_label.pack()
audio_file_entry.pack()
audio_file_browse_button.pack()

start_time_label.pack()
start_time_entry.pack()

merge_button.pack()

status_label.pack()

root.mainloop()
