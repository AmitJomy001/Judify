import tkinter as tk
def downaud():
    import youtube_dl
    import tkinter as tk
    import threading


#img1 = tk.PhotoImage(file = "C:....")
#button = tk.button(things, image = img1)    




    # Set up the youtube_dl options
    ydl_opts = {
        'outtmpl': './DOWNLOADS/%(title)s.%(ext)s',  # Save the file in the DOWNLOADS directory
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    # Download the audio in a separate thread
    def download():
        # Get the URL from the input field
        url = entry.get()

        # Create a new thread
        thread = threading.Thread(target=download_worker, args=(url,))
        button.pack_forget()
        thread.start()

    # The worker function that will be run in the separate thread
    def download_worker(url):
        # Get information about the video
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        # Get the estimated download time and file size
        time = info['duration']
        size = info['filesize']

        # Convert the time and size to the desired format
        time = int(time / 60)
        seconds = time % 60
        time = f"{time}:{seconds}"
        size = round(size / 1000000, 2)

        # Show the estimated download time and file size in the GUI
        label['text'] = f"Estimated download time: {time}\nEstimated file size: {size} MB"

        # Download the audio
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            # Set the progress hook to update the GUI
            ydl.add_progress_hook(download_progress_hook)
            ydl.download([url])

        # Show a success message
        label['text'] = "Download complete!"
        # Show the download button again
        button.pack()

    # The progress hook function that will be called to update the GUI
    def download_progress_hook(d):
        # Calculate the remaining time
        time = int(d.get('eta', 0))
        seconds = time % 60
        time = f"{time}:{seconds}"

        # Show the remaining time in the GUI
        label['text'] = f"Time remaining: {time}"

    # Create the tkinter GUI
    root = tk.Tk()
    root.title("YouTube Audio Downloader")
    root.geometry('800x400')

    label = tk.Label(root, text="Enter a YouTube video URL:", foreground="green")
    label.pack()

    entry = tk.Entry(root, width=40)
    entry.pack()

    button = tk.Button(root, text="Download", command=download)
    button.pack()

    root.mainloop()
def playoff():
    import os
    import tkinter as tk
    import threading
    import pygame

    # Set the current working directory to the DOWNLOADS directory
    os.chdir('./DOWNLOADS')

    # Get a list of available songs in the DOWNLOADS directory
    songs = os.listdir()

    # Set up pygame
    pygame.init()
    pygame.mixer.init()

    # Create the tkinter GUI
    root = tk.Tk()
    root.title("Song Player")
    root.geometry('800x400')

    # Create the listbox to display the available songs
    songs_list = tk.Listbox(root, width=65, height = 7)   #'''you  may want to remove height'''
    songs_list.pack(pady = 12)
 
    # Populate the listbox with the available songs
    for song in songs:
        songs_list.insert(tk.END, song)

    def play():
        # Get the selected song from the listbox
        selected_song = songs_list.get(songs_list.curselection())

        # Load the selected song into pygame
        pygame.mixer.music.load(selected_song)

        # Play the selected song
        pygame.mixer.music.play()

    def pause():
        # Pause the currently playing song
        pygame.mixer.music.pause()

    # Create the play and pause buttons
    play_button = tk.Button(root, text="Play", command=play)
    play_button.pack(pady = 5)

    pause_button = tk.Button(root, text="Pause", command=pause)
    pause_button.pack(pady = 5)

    root.mainloop()


# Create the tkinter GUI
root = tk.Tk()
root.title("YouTube Audio Downloader")
root.geometry('800x400')

# Create a tkinter menu
menu = tk.Menu(root)
root.config(menu=menu)

# Create the "Download audio" menu option
download_audio_menu = tk.Menu(menu)
menu.add_cascade(label="Download audio", menu=download_audio_menu)
download_audio_menu.add_command(label="Download audio", command=downaud)

# Create the "Play a song" menu option
play_song_menu = tk.Menu(menu)
menu.add_cascade(label="Play a song", menu=play_song_menu)
play_song_menu.add_command(label="Play a song", command=playoff)

root.mainloop()
