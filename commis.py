import threading

class Commis(threading.Thread):
    def __init__(self, name, quantity, unit):
        threading.Thread.__init__(self)