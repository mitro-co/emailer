import config


class Message:
    subject = None
    from_email = config.from_email
    from_name = config.from_name
    reply_to_email = config.reply_to_email
    reply_to_name = config.reply_to_name
    to = {}
    cc = {}
    bcc = {}
    body_text = None
    body_html = None

    def __init__(self, subject, to_address, to_name, body_text, body_html):
        self.subject = subject
        self.to = {to_address: to_name}
        self.body_text = body_text
        self.body_html = body_html
        return
