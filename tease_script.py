import threading
import time

def fake_sleep():
    print("Sleeping for 3 seconds...")
    time.sleep(3)
    return True

thick = threading.Thread(target=fake_sleep)
thick.start()

