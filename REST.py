import time
import tkinter as tk
#import ctypes

# Define the time intervals
WORK_TIME = 30 * 60  # 30 minutes in seconds
REST_TIME = 10 * 60  # 10 minutes in seconds
START_HOUR = 8      # Start time hour (24-hour format)
END_HOUR = 22       # End time hour (24-hour format)

# Define the function to remind the user to take a break
def remind_to_rest():
    # Flash the window on the taskbar to get user's attention
#    ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), True)
    
    # Create the GUI window
    window = tk.Tk()
    window.title("Rest Reminder")
    window.geometry("300x150")
    
    # Define the GUI elements
    label = tk.Label(window, text="It's time to take a break! Rest for 10 minutes.")
    label.pack(pady=20)
    
    button = tk.Button(window, text="I know", command=window.destroy)
    button.pack(pady=10)
    
    # Display the window
    window.deiconify()
    window.lift()
    window.attributes("-topmost", True)
    window.after_idle(window.attributes, '-topmost', False)
    window.mainloop()
    
    # Wait for the rest period to end
    time.sleep(REST_TIME)
    
    # Flash the window on the taskbar to get user's attention
#    ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), True)
    
    # Create the GUI window to notify the end of the rest period
    window = tk.Tk()
    window.title("Rest Reminder")
    window.geometry("300x150")
    
    # Define the GUI elements
    label = tk.Label(window, text="Break time is over! Time to get back to work.")
    label.pack(pady=20)
    
    button = tk.Button(window, text="I'm ready", command=window.destroy)
    button.pack(pady=10)
    
    # Display the window
    window.deiconify()
    window.lift()
    window.attributes("-topmost", True)
    window.after_idle(window.attributes, '-topmost', False)
    window.mainloop()

# Loop to remind the user to take a break every 30 minutes
while True:
    current_hour = time.localtime().tm_hour
    if current_hour >= START_HOUR and current_hour < END_HOUR:
        time.sleep(WORK_TIME)
        remind_to_rest()
    else:
        time.sleep(60)
