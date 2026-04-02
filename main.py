import pyglet
import os

player = None  # global player


def get_songs():
    songs = os.listdir("songs")
    songs = [s for s in songs if s.endswith(".mp3")]
    return songs


def select_song():
    songs = get_songs()

    print("\n🎵 Available Songs:")
    for i, song in enumerate(songs):
        print(i, song)

    choice = int(input("Select song number: "))
    return songs[choice]


def load(song_path):
    global player

    # Stop previous song
    if player:
        player.delete()

    music = pyglet.media.load(song_path)
    player = music.play()
    print("Playing:", song_path)


def play():
    global player
    if player:
        player.play()
        print("Resumed")
    else:
        print("No song loaded")


def pause():
    global player
    if player:
        player.pause()
        print("Paused")
    else:
        print("No song loaded")


def stop():
    global player
    if player:
        player.delete()
        player = None
        print("Stopped")
    else:
        print("No song loaded")


def main():
    # Initial song selection
    selected_song = select_song()
    load("songs/" + selected_song)

    while True:
        print("\n🎧 MUSIC PLAYER")
        print("1. Play")
        print("2. Pause")
        print("3. Stop")
        print("4. Change Song")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            play()

        elif choice == "2":
            pause()

        elif choice == "3":
            stop()

        elif choice == "4":
            selected_song = select_song()
            load("songs/" + selected_song)

        elif choice == "5":
            stop()
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()




