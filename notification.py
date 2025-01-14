from plyer import notification
import time

if __name__ == '__main__':
   while True:
        notification.notify(
            title="TAKE REST",message="because it is important",timeout=5)
        time.sleep(10)
