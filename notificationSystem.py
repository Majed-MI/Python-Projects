from plyer import notification
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "Gallery/man_icon.ico",
        timeout = 10
    )

if __name__ == "__main__":
    while True:
        nTitle = 'Hello Mr. Majed'
        nText = f"It has been 1 hour since you are infront of the laptop. Please Close Your laptop now."
        notifyMe(nTitle, nText)
        time.sleep(30)
