import winsound
import time

def play_note(note, duration):
    # Frequency dictionary for notes
    frequencies = {
        "C": 261.63,
        "D": 293.66,
        "E": 329.63,
        "F": 349.23,
        "G": 392.00,
        "A": 440.00,
        "B": 493.88,
    }
    frequency = frequencies.get(note.upper(), 440)  # Default to A
    winsound.Beep(int(frequency), duration)

def play_song():
    song = [("C", 500), ("D", 500), ("E", 500), ("F", 500), ("G", 500), ("A", 500), ("B", 500)]
    for note, duration in song:
        play_note(note, duration)
        time.sleep(0.1)

play_song()
