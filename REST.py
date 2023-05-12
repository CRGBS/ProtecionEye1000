import time
import tkinter as tk
#import ctypes

# Define the time intervals
WORK_TIME = 30 * 60  # 30 minutes in seconds
REST_TIME = 10 * 60  # 10 minutes in seconds
START_HOUR = 8      # Start time hour (24-hour format)
END_HOUR = 22       # End time hour (24-hour format)

# Define the function to remind the user to take a break
def remind_to_rest(is_resting):
    if is_resting:
        title = "Rest Reminder"
        message = "It's time to take a break! Rest for 10 minutes."
        duration = REST_TIME
    else:
        title = "Work Reminder"
        message = "Break time is over! Time to get back to work."
        duration = WORK_TIME

    # Create the GUI window
    window = tk.Tk()
    window.title(title)
    window.geometry("300x150")

    # Define the GUI elements
    label = tk.Label(window, text=message)
    label.pack(pady=20)

    # Add a label to show remaining time
    time_label = tk.Label(window, text=f"Remaining time: {duration // 60:02d}:{duration % 60:02d}")
    time_label.pack()

    #button = tk.Button(window, text="I know", command=window.destroy)
    #button.pack(pady=10)

    # Display the window
    window.deiconify()
    window.lift()
    window.attributes("-topmost", True)
    window.after_idle(window.attributes, '-topmost', False)

    # Start the countdown timer
    start_time = time.monotonic()
    while True:
        remaining_time = max(0, duration - int(time.monotonic() - start_time))
        time_label.config(text=f"Remaining time: {remaining_time // 60:02d}:{remaining_time % 60:02d}")
        window.update()
        if remaining_time == 0:
            break

    window.destroy()

# Loop to remind the user to take a break every 30 minutes
while True:
    current_hour = time.localtime().tm_hour
    if current_hour >= START_HOUR and current_hour < END_HOUR:
        time.sleep(WORK_TIME)
        remind_to_rest(False)
        time.sleep(REST_TIME)
        remind_to_rest(True)
    else:
        time.sleep(60)
