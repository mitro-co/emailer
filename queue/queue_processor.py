import datetime
import json
import logging

from database import EmailQueueModel
import templates


class QueueProcessor:
    def __init__(self, config, session, provider):
        self.session = session
        self.provider = provider
        self.config = config
        return

    def process(self):
        while True:
            item = self.get_next_item()

            if item is None:
                break

            self.process_item(item)
        return

    def process_item(self, item):
        try:
            email = templates.get_email(item.type_string)
            message = email.get_message(item)

            if message is None:
                raise Exception('empty message for type: ' + item.type_string + ' id: ' + str(item.id))

            result = self.provider.send(message)
            logging.info('sent ' + item.type_string + ' to ' + json.dumps(message.to))
        except Exception as e:
            logging.critical(e.message)
            result = False

        if result is True:
            self.delete_item(item)

        return result

    def get_next_item(self):
        item = self.session.query(EmailQueueModel).filter_by(attempted_time=None).first()

        if item is None:
            self.session.commit()
            return None

        # Mark as attempted; lame attempt to "log" failed items
        item.attempted_time = datetime.datetime.utcnow()

        # flush then expunge: changes propagate but item can be used without a database session
        self.session.flush()
        self.session.expunge(item)
        self.session.commit()

        return item

    def delete_item(self, item):
        assert self.session.query(EmailQueueModel).filter_by(id=item.id).count() == 1
        self.session.delete(item)
        self.session.commit()