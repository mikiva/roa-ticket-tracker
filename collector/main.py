import logging
from threading import Event
import sys
from logging import getLogger
import worker

FORMAT = '%(asctime)s :: %(name)s :: %(levelname)-8s :: %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

log = getLogger(__name__)

event = Event()

def main():
    log.info("RUN COLLECTOR")
    try:
        worker.fetch_and_update()
    except:
        log.error("ERROR FETCHING AND UPDATING", exc_info=1)
        sys.exit(1)

    


if __name__ == "__main__":
    main()
