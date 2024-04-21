import time
import pyautogui

def keep_screen_awake(interval=60, duration=None):
        """
        Keep the screen awake by simulating a keyboard press at regular intervals.
        
        Args:
            interval (int): Time interval in seconds between simulated key presses. Default is 60 seconds.
            duration (int): Optional duration in seconds for which to keep the screen awake. If None, it will run indefinitely.
        """
        try:
            if duration:
                end_time = time.time() + duration
                while time.time() < end_time:
                    pyautogui.press('shift')  # Simulate a keyboard press (you can use any key)
                    time.sleep(interval)
            else:
                while True:
                    pyautogui.press('shift')  # Simulate a keyboard press (you can use any key)
                    time.sleep(interval)
        except KeyboardInterrupt:
            print("Screen awake function stopped.")