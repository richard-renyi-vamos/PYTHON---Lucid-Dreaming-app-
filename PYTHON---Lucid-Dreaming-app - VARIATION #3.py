import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import datetime
import os
import threading
import time
import pygame

# 🧠 Initialize audio module
pygame.mixer.init()

# 🔊 Load your cue audio file (must be a .mp3 or .wav in same dir)
AUDIO_FILE = "lucid_cue.wav"
JOURNAL_FILE = "dream_journal.txt"

# 💡 Reminder system
def reality_check_reminder():
    while True:
        time.sleep(60 * 60)
        messagebox.showinfo("Reality Check!", "Are you dreaming? 🤔 Do a reality check! 🪞🫣")

# 🎵 Play cue audio
def play_audio():
    if os.path.exists(AUDIO_FILE):
        pygame.mixer.music.load(AUDIO_FILE)
        pygame.mixer.music.play()
    else:
        messagebox.showwarning("Audio File Not Found", "Your lucid cue audio is missing!")

# ⏹️ Stop cue audio
def stop_audio():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        messagebox.showinfo("Audio", "Cue stopped 🔇")

# 📓 Save dream journal entry
def save_entry(entry):
    with open(JOURNAL_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {entry}\n")
    messagebox.showinfo("Saved", "Dream entry saved! 🌙✨")

# 📖 View dream journal
def view_journal():
    if os.path.exists(JOURNAL_FILE):
        with open(JOURNAL_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        view_window = tk.Toplevel(root)
        view_window.title("📖 Dream Journal Entries")
        text_area = scrolledtext.ScrolledText(view_window, wrap=tk.WORD, width=60, height=20)
        text_area.insert(tk.INSERT, content)
        text_area.pack()
    else:
        messagebox.showinfo("No Entries", "No dream journal entries found yet.")

# 🧹 Clear journal
def clear_journal():
    if os.path.exists(JOURNAL_FILE):
        confirm = messagebox.askyesno("Clear Journal", "Are you sure you want to clear all entries?")
        if confirm:
            open(JOURNAL_FILE, "w", encoding="utf-8").close()
            messagebox.showinfo("Cleared", "All dream entries cleared.")
    else:
        messagebox.showinfo("Not Found", "No journal found to clear.")

# ⏰ Schedule cue audio after user-defined minutes
def schedule_cue():
    mins = simpledialog.askinteger("Set Cue", "Play audio cue after how many minutes? ⏱️", minvalue=1, maxvalue=1440)
    if mins:
        threading.Thread(target=lambda: (time.sleep(mins * 60), play_audio()), daemon=True).start()
        messagebox.showinfo("Scheduled", f"Lucid cue will play in {mins} minutes. 💤")

# 🎛️ GUI setup
root = tk.Tk()
root.title("Lucid Dream Toolkit 🌌🛌")

tk.Button(root, text="Reality Check Reminder 🪞", command=lambda: threading.Thread(target=reality_check_reminder, daemon=True).start()).pack(pady=5)
tk.Button(root, text="Play Lucid Cue 🔊", command=play_audio).pack(pady=5)
tk.Button(root, text="Stop Cue 🔇", command=stop_audio).pack(pady=5)
tk.Button(root, text="Write Dream Entry 📝", command=lambda: save_entry(simpledialog.askstring("Dream Entry", "Write your dream:"))).pack(pady=5)
tk.Button(root, text="View Dream Journal 📖", command=view_journal).pack(pady=5)
tk.Button(root, text="Clear Dream Journal 🧹", command=clear_journal).pack(pady=5)
tk.Button(root, text="Schedule Lucid Cue ⏰", command=schedule_cue).pack(pady=5)

root.mainloop()
