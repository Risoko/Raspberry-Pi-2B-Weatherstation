import os

def get_time():
    """Return time use sensor RTC."""
    return os.popen('sudo hwclock -r').read()

if __name__ == "__main__":
    print(get_time())