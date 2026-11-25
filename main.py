import os
import sys

REPLY = "I'm out until Monday. Your email is safe with me — I read the subject line, felt nothing, and archived it with love."

def auto_reply():
    try:
        channel = open("/output/entry.txt", "w", encoding="utf-8")
    except FileNotFoundError:
        os.mkdir("/output")
        channel = open("/output/entry.txt", "w", encoding="utf-8")
    with channel:
        channel.write(REPLY)

auto_reply()
