from queue_processor import QueueProcessor

_processor = None


def get_processor():
    global _processor
    if _processor is None:
        _processor = QueueProcessor()
    return _processor