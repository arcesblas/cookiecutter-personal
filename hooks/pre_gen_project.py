import os
import sys

# We define colors
MESSAGE_COLOR = "\x1b[31m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Let's do it! You're going to create something awesome!")
print(f"Creating project at { os.getcwd() }{RESET_ALL}")