"""
Jukebox: Design a musical jukebox using object-oriented principles.

but a more interview friendly question can be

---
The Problem: The "Café Beats" Jukebox
You are hired to build the software for a physical Jukebox. People in a café want to listen to music while they eat, but they have to share one machine.

Part 1: The Core Requirements (What it MUST do)
The Library: The Jukebox has a collection of many Songs. Each song belongs to an Album and has an Artist.

The Payment: The machine doesn't play music for free. A user must insert money to get credits. One credit allows them to pick one song.

The Selection: A user browses the library and picks a song. If they have enough credits, the song is added to the Queue.

The Playback: The Jukebox plays songs one by one in the order they were added (First-In, First-Out). When a song finishes, the next one starts automatically.

The Display: The Jukebox needs to show which song is currently playing.

--- Hints for the problem
Part 2: Your Goal (How to solve it)
Try to write out the Python classes (or just the outlines) for this. Focus on these three areas:

A. Data Structures (The "Nouns")
How will you store the songs so they are easy to find?

What data structure is best for a "Queue" where the first song in is the first song out?

B. The "State" (The "Current Situation")
How does the Jukebox know it's currently "Busy" playing a song vs. "Idle"?

Where do you keep track of the user's remaining money?

C. The Methods (The "Verbs")
process_payment(amount)

select_song(song_id)

play_next()

Part 3: Constraints to Think About (The "Gotchas")
The Empty Queue: What does the machine do if the queue is empty? Does it just sit there? Does it play a random "default" song?

The Price: What if a song costs $0.50 but the user only put in a quarter?

Song Info: Should a Song object know its own length (in seconds)? Why might the Jukebox need that information?
"""

# Using the defenition.md approach

# Step 1: Given in the question 
# Step 2: Core classes: Song, Album, Artist, Jukebox (collection of songs, queue), User (payment, creidts, one credit for one song), 
# Step 3: Actions
# Song (name, artist, album, duration, price / credits)
# Album (name, one or many Artists, songs)
# jukebox (collection of songs, queue, display)
# User (money, credits)

import time

class Artist():
    def __init__(self, name: str):
        self.name: str = name

class Album():
    def __init__(self, name: str, artist: Artist):
        self.name: str = name
        self.artist: Artist = artist

class Song():
    def __init__(self, name: str, album: Album, duration: int, credits: int):
        self.name: str = name
        self.album: Album = album
        self.duration: int = duration
        self.credits: int = credits

class Jukebox():
    def __init__(self, songs: list[Song]):
        self.songs: list[Song] = songs
        self.queue: list[Song] = []
        self.current_song: Song | None = None

    def browse_songs(self):
        for i, song in enumerate(self.songs):
            print(f"{i}: {song.name} from {song.album.name} by {song.album.artist.name}")

    def get_credits(self, cash: int):
        # Assuming $1 = 1 credit
        return cash * 1 / 1

    def select_song(self, song_index: int, credits: int):
        song = self.songs[song_index]

        print("Song selected")

        if credits >= song.credits:
            self.queue.append(song)
            extra_credits = credits - song.credits
            print("Song added to the queue")
            return extra_credits
        else:
            print(f"Credits too low to play the song. The song needs {song.credits} but you gave {credits}")

    def start_jukebox(self):
        while self.queue:
            song = self.queue.pop(0)
            self.current_song = song
            print(f"Playing {song.name}")

            time.sleep(song.duration)

            print("Song finished")

        self.current_song = None

    def display_current(self):
        if self.current_song != None:
            return f"Current song: {self.current_song.name}"
        else:
            return "No song being played"
        
# Mock song data
artist1 = Artist(name="Artist1")

album1 = Album(name="Album1", artist=artist1)

song1 = Song(name="Song1", album=album1, duration=3.5, credits=2)
song2 = Song(name="Song2", album=album1, duration=4, credits=3)
song3 = Song(name="Song3", album=album1, duration=4, credits=4)

jukebox = Jukebox(songs=[song1, song2, song3])

jukebox.browse_songs()

print(jukebox.select_song(song_index=0, credits=5))

jukebox.start_jukebox()

print(jukebox.display_current())