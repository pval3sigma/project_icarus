
import logging

from jobs import kick_off
from icarus.api.keys import get_keys

def start():

    keys = get_keys()
    logging.info(f"Keys are saved")
    

    return


if __name__ == "__main__":
    kick_off('icarus','main', start)