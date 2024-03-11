import sched
import time
import tkinter as tk

# Define the time intervals
WORK_TIME = 30 * 60  # 30 minutes in seconds
REST_TIME = 10 * 60  # 10 minutes in seconds
START_HOUR = 8       # Start time hour (24-hour format)
END_HOUR = 22        # End time hour (24-hour format)
EXTENSION_TIME = 60 * 60  # 1 hour in seconds

# Create the scheduler
scheduler = sched.scheduler(time.monotonic, time.sleep)

def remind_to_rest(is_resting):
    global WORK_TIME, REST_TIME
    if is_resting:
        title = "Rest Reminder"
        message = f"It's time to take a break! Rest for {REST_TIME // 60} minutes."
        duration = REST_TIME
    else:
        title = "Work Reminder"
        message = "Break time is over! Time to get back to work."
        duration = WORK_TIME

    # Create the GUI window
    window = tk.Tk()
    window.title(title)
    window.geometry("900x320")
    window.configure(bg="black")  # Set window background color to black
    window.resizable(width=False, height=False)  #set the window resizable property to False

    # Define the GUI elements
    label = tk.Label(window, text=message, font=("Arial", 32), bg="black", fg="gray")
    label.pack(pady=20)

    # Add a label to show remaining time
    time_label = tk.Label(window, text=f"Remaining time: {duration // 60:02d}:{duration % 60:02d}", font=("Arial", 23),
                          bg="black", fg="gray")
    time_label.pack()

    # Add a button to extend the timer by 1 hour
    def extend_timer():
        nonlocal duration
        duration += EXTENSION_TIME  # Extend the timer

    extend_button = tk.Button(window, text=f"Extend for {EXTENSION_TIME // 60} minutes", command=extend_timer,
                              font=("Arial", 23), bg="black", fg="gray")
    extend_button.pack(side=tk.LEFT, padx=80)

    # Add a button to Reset reminders
    def reset_reminders():
        for event in scheduler.queue:
            scheduler.cancel(event)
        window.destroy()
        schedule_reminders()
        scheduler.run()
    reset_button = tk.Button(window, text="Reset Reminders", command=reset_reminders,
                        font=("Arial", 23), bg="black", fg="gray")
    reset_button.pack(side=tk.LEFT, padx=7)
    
    # Display the window
    window.attributes("-topmost", True)
    window.grab_set()
    window.focus_force()

    # Define the function to update the timer label
    def update_time_label():
        nonlocal duration, time_label, window
        remaining_time = max(0, duration - int(time.monotonic() - start_time))
        time_label.config(
            text=f"Remaining time: {remaining_time // 60:02d}:{remaining_time % 60:02d}", font=("Arial", 23),
            bg="black", fg="gray")
        if remaining_time > 0:
            window.after(1000, update_time_label)
            # Check if the window is still valid
            #TODO if window.winfo_exists():
        else:
            window.destroy()

    # Start the countdown timer
    start_time = time.monotonic()
    update_time_label()

    # Start the mainloop to update the GUI
    window.mainloop()

def schedule_reminders():
    current_hour = time.localtime().tm_hour
    if START_HOUR <= current_hour < END_HOUR:
        scheduler.enter(3, 1, remind_to_rest, (False,))
        scheduler.enter(3, 1, remind_to_rest, (True,))
    scheduler.enter(WORK_TIME + REST_TIME + 1, 1, schedule_reminders)

# Schedule the first reminder
schedule_reminders()

# Start the scheduler
scheduler.run()
