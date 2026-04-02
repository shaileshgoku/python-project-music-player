import pyglet
import os
import tkinter as tk

player = None


def get_songs():
    songs = os.listdir("songs")
    songs = [s for s in songs if s.endswith(".mp3")]
    return songs


def load(song_path):
    global player

    if player:
        player.delete()

    music = pyglet.media.load(song_path)
    player = music.play()


def play_song():
    selected = listbox.curselection()
    if selected:
        song = songs[selected[0]]
        load("songs/" + song)


def pause_song():
    global player
    if player:
        player.pause()


def resume_song():
    global player
    if player:
        player.play()


def stop_song():
    global player
    if player:
        player.delete()


# --- GUI Setup ---
root = tk.Tk()
root.title("🎧 Music Player")
root.geometry("400x400")

songs = get_songs()

# Listbox
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=20)

for song in songs:
    listbox.insert(tk.END, song)

# Buttons
play_btn = tk.Button(root, text="Play", command=play_song)
play_btn.pack(pady=5)

pause_btn = tk.Button(root, text="Pause", command=pause_song)
pause_btn.pack(pady=5)

resume_btn = tk.Button(root, text="Resume", command=resume_song)
resume_btn.pack(pady=5)

stop_btn = tk.Button(root, text="Stop", command=stop_song)
stop_btn.pack(pady=5)

# Run app
root.mainloop()