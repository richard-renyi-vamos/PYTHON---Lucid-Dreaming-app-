import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime
import os
import threading
import time
import pygame  # for audio playback

# 🧠 Initialize audio module
pygame.mixer.init()

# 🔊 Load your cue audio file (must be a .mp3 or .wav in same dir)
AUDIO_FILE = "lucid_cue.wav"  # Change to your file

# 📁 Dream journal file
JOURNAL_FILE = "dream_journal.txt"


# 💡 Reminder system
def reality_check_reminder():
    while True:
        time.sleep(60 * 60)  # every hour
        messagebox.showinfo("Reality Check!", "Are you dreaming? 🤔 Do a reality check! 🪞🫣")


# 🎵 Play cue audio
def play_audio():
    if os.path.exists(AUDIO_FILE):
        pygame.mixer.music.load(AUDIO_FILE)
        pygame.mixer.music.play()
    else:
        messagebox.showwarning("Audio File Not Found", "Your lucid cue audio is missing!")


# 📓 Save dream journal entry
def save_entry(entry):
    with open(JOURNAL_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n[{timestamp]()
