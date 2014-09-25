#!/usr/bin/env python
import logging
import time
import signal

import config
import database
import providers
import queue


interrupted = False


def main():
    logging.root.setLevel(logging.INFO)
    logging.info("Starting up email queue")

    session = database.get_session(config.database)
    provider = providers.get_provider(config.provider)
    processor = queue.QueueProcessor(config, session, provider)

    try:
        while not interrupted:
            logging.debug("checking email queue")
            processor.process()
            time.sleep(config.queue.getfloat('sleep_seconds', 10))
    except Exception as e:
        logging.critical(e.message)
    finally:
        database.close_connection()


def signal_handler(signal, frame):
    global interrupted
    interrupted = True
    logging.info("Shutting down email queue")


signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    main()
