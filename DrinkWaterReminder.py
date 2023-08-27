# Import necessary modules
import time
from plyer import notification

# Display an initial welcome message
print("Welcome To Drink Water Reminder Made By Aryan\nThis Will Give You a reminder to drink water and take a break every 1 HOUR")

# Set up an infinite loop to repeat the reminder
while True:
    time.sleep(1800)  # Sleep for 30 minutes (1800 seconds)

    # Prepare the notification message
    message = "Drink Water And Take A Walk For 2 min"
    title = "Water Reminder"

    # Use the Plyer library to show a notification
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Notification will disappear after 10 seconds
    )
