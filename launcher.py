import os
import sys
import ctypes

# Prevent console window from showing
if hasattr(sys, 'frozen'):
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)

# Redirect stdout and stderr to null
sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')

# Import the actual application
from network_status_indicator import main

if __name__ == "__main__":
    main()