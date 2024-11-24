import time
from datetime import datetime
import threading
try:
    import winsound  # For Windows audio cue
except ImportError:
    winsound = None  # Use playsound or similar on other platforms


def reality_check_reminder(interval=60):
    """
    Sends a reminder to perform reality checks every 'interval' minutes.
    """
    while True:
        now = datetime.now()
        print(f"⏰ Time for a reality check! - {now.strftime('%H:%M:%S')}")
        print("👉 Ask yourself: Am I dreaming?")
        print("👉 Try to push your finger through your palm.")
        print("👉 Look at a clock or read some text twice.\n")
        time.sleep(interval * 60)  # Wait for the next reminder


def log_dream():
    """
    Simple text-based dream journal for recording dreams.
    """
    while True:
        print("\n💭 Log Your Dream:")
        dream = input("Type your dream description below (or type 'exit' to stop logging):\n")
        if dream.lower() == 'exit':
            print("📔 Exiting dream journal.")
            break
        with open("dream_journal.txt", "a") as journal:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            journal.write(f"Date: {date}\nDream: {dream}\n{'-'*50}\n")
        print("✨ Dream logged successfully!")


def play_audio_cue(interval=90):
    """
    Play a sound cue every 'interval' minutes to trigger lucidity.
    """
    while True:
        print("🔊 Playing audio cue!")
        if winsound:
            winsound.Beep(440, 1000)  # Beep for 1 second
        else:
            print("⚠ Beep not available. Replace this with your custom audio player!")
        time.sleep(interval * 60)


def sleep_cycle_tracker(cycles=4, cycle_duration=90):
    """
    Tracks sleep cycles (default 4 cycles of 90 minutes).
    """
    for cycle in range(1, cycles + 1):
        print(f"😴 Sleep Cycle {cycle}/{cycles} started... Sweet dreams! 🌌")
        time.sleep(cycle_duration * 60)  # Simulate a 90-minute cycle
        print(f"⏰ Wake up gently! Cycle {cycle} complete.\n")


if __name__ == "__main__":
    print("🌟 Welcome to the Lucid Dreaming App! 🌙")
    print("Choose a feature to use:")
    print("1. Reality Check Reminders")
    print("2. Dream Journal")
    print("3. Audio Cue Assistant")
    print("4. Sleep Cycle Tracker")
    
    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        interval = int(input("Enter reminder interval (in minutes): ").strip())
        threading.Thread(target=reality_check_reminder, args=(interval,)).start()
    elif choice == "2":
        log_dream()
    elif choice == "3":
        interval = int(input("Enter audio cue interval (in minutes): ").strip())
        threading.Thread(target=play_audio_cue, args=(interval,)).start()
    elif choice == "4":
        cycles = int(input("Enter the number of sleep cycles: ").strip())
        cycle_duration = int(input("Enter cycle duration (in minutes): ").strip())
        sleep_cycle_tracker(cycles, cycle_duration)
    else:
        print("❌ Invalid choice. Exiting app.")
