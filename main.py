import Communication
import Vision

from threading import Thread


best_targ = None

def send_data():
    while True:
        Communication.update_tables(best_targ)


def find_targets():
    while True:
        global best_targ
        best_targ = Vision.find_vision_targets()

Communication.init()
Vision.init()

coms = Thread(send_data())
vision = Thread(find_targets())

Communication.init()
Vision.init()

coms.start()
vision.start()