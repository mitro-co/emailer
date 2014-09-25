import cStringIO
import smtplib
import email
import email.generator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from templates import Message


# From: http://radix.twistedmatrix.com/2010/07/how-to-send-good-unicode-email-with.html
# Override python's weird assumption that utf-8 text should be encoded with
# base64, and instead use quoted-printable (for both subject and body).
email.Charset.add_charset('utf-8', email.Charset.QP, email.Charset.QP, 'utf-8')


class SMTP:

    def __init__(self, config):
        self.hostname = config.get('hostname', 'localhost')
        self.port = config.getint('port', 25)
        self.username = config.get('username')
        self.password = config.get('password')
        self.tls = config.getboolean('tls', True)
        return

    def send(self, message):
        smtp = smtplib.SMTP(self.hostname, self.port, timeout=5)

        if self.tls:
            smtp.starttls()

        if self.username:
            smtp.login(self.username, self.password)

        data = self.create_message_data(message)

        try:
            smtp.sendmail(message.from_address, self.create_recipients_list(message), self.message_data_to_string(data))
            success = True
        except:
            success = False
        finally:
            smtp.quit()

        return success

    def create_recipients_list(self, message):
        to = []
        for key, value in message.to.iteritems():
            to.append(key)
        for key, value in message.cc.iteritems():
            to.append(key)
        for key, value in message.bcc.iteritems():
            to.append(key)

        return ','.join(to)

    def create_message_data(self, message=Message):
        msg = MIMEMultipart('alternative')

        text_part = MIMEText(message.body_text, 'plain', 'UTF-8')
        if not message.body_html:
            # No HTML: Create a single part message with the text body
            msg = text_part

        msg['Subject'] = message.subject

        if message.from_name:
            msg['From'] = message.from_name + '<' + message.from_email + '>'
        else:
            msg['From'] = message.from_email

        if message.from_email != message.reply_to_email:
            if message.reply_to_name:
                msg['Reply-To'] = message.reply_to_name + '<' + message.reply_to_email + '>'
            else:
                msg['Reply-To'] = message.reply_to_email

        to = []
        for key, value in message.to.iteritems():
            if value:
                to.append(value + '<' + key + '>')
            else:
                to.append(key)

        msg['To'] = ','.join(to)

        cc = []
        for key, value in message.cc.iteritems():
            if value:
                to.append(value + '<' + key + '>')
            else:
                to.append(key)

        msg['Cc'] = ','.join(cc)


        bcc = []
        for key, value in message.bcc.iteritems():
            if value:
                to.append(value + '<' + key + '>')
            else:
                to.append(key)

        msg['Bcc'] = ','.join(cc)


        if message.body_html:
            # The message is multi-part, with HTML and text
            html_part = MIMEText(message.body_html, 'html', 'UTF-8')
            # most important at end
            msg.attach(text_part)
            msg.attach(html_part)

        return msg

    def message_data_to_string(self, message):
        # The default email Message as_string escapes From lines, in case it is
        # used in a Unix mbox format:
        # http://homepage.ntlworld.com./jonathan.deboynepollard/FGA/mail-mbox-formats.html
        io = cStringIO.StringIO()
        g = email.generator.Generator(io, False)  # second arg: "should I mangle From?"
        g.flatten(message)
        return io.getvalue()
