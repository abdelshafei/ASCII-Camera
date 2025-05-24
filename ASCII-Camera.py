import os
import cv2
import numpy as np

# Last bits of characters get the darkest coloured pixels while the first characters get the opposite.
# Usage of tuples as its more memory effecient and faster in proformance
ascii_chars = (' ', '.', "'", ',', ':', ';', 'c', 'l', 'x', 'o', '*', '?', 'k', 'X', '&', 'd', 'O', '0', 'K', 'i', 'N', 'G')

# To not show actual live webcam footage
SHOW_REAL_VIDEO = False

COLOURIZED = False

def rowToAscii(row):
    scale = len(ascii_chars)
    return tuple(ascii_chars[min(int(x / 256 * scale), scale - 1)] for x in row)

def pixelToAscii(grayVal):
    return tuple(rowToAscii(row) for row in grayVal)

def showAscii(gray_frame):
    os.system("clear")
    print('\n'.join((''.join(row) for row in gray_frame)), end='')

capture = cv2.VideoCapture(0)

while(cv2.waitKey(1) & 0xFF != ord('q')):

    # Get adjusted size of the terminal
    screen_width, screen_height = os.popen('stty size', 'r').read().split()

    # read each frame from the capture feed
    ret, frame = capture.read()

    if not ret:
        break

    if not COLOURIZED:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Gray scale the actual colorized frames

        adjusted_frame = cv2.resize(gray_frame, (int(screen_height), int(screen_width))) # adjusted cv window to the terminal's dimensions

        ascii_frame = pixelToAscii(adjusted_frame)
        showAscii(ascii_frame)

    # else:
        

    if SHOW_REAL_VIDEO:
        cv2.imshow('Grayscale Frame', adjusted_frame)
        
                


# Release capture data when everything is done
capture.release()
cv2.destroyAllWindows()
