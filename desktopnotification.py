#pip install plyer
#pip install timemodule
from plyer import notification
import time


if __name__ == '__main__':
    while True:
        notification.notify(
         title="*** Please Take Rest ***",
         message="Rest reduces stress",
         app_icon="C:/Users/hp/Desktop/Python/rest.ico",
         timeout=10
        )
        time.sleep(20)