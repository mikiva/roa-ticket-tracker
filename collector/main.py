import logging
import sys
import threading
from threading import Event

from logging import getLogger
from settings import db_settings
import worker

FORMAT = '%(asctime)s :: %(name)s :: %(levelname)-8s :: %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

log = getLogger(__name__)

event = Event()


class WorkerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)

    def run(self, *args, **kwargs):
        while not event.is_set():
            # FETCH AND UPDATE
            worker.fetch_and_update()
            event.wait(timeout=db_settings.WORKER_TIMEOUT)


def main():
    u = WorkerThread()
    try:
        log.info("START WORKER")
        u.start()
        event.wait()

    except(KeyboardInterrupt, SystemExit):
        log.info("EXIT WORKER")
        event.set()  # INTERRUPT
        u.join()
        sys.exit(0)


if __name__ == "__main__":
    main()
