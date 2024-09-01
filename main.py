import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please Drink Water Now!",
            message="Women should have about 2 litres (8 cups) of fluids a day, and men about 2.6 litres (10 cups).",
            app_icon=r"C:\Users\pradu\OneDrive\Documents\Project\Python\Reminder application for notification\icon.ico",
            timeout=5
        )
        time.sleep(60*60)  
