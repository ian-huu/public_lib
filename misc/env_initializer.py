import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

def init():
    global BASE_DIR    
    for x in os.listdir(BASE_DIR):
        path = os.path.join(BASE_DIR, x)
        if os.path.isdir(path):
            sys.path.append(path)
