import requests
import requests.auth


class Mailgun:

    api_url = 'https://api.mailgun.net/v2'

    def __init__(self, config):
        self.api_key = config.get('api_key')
        self.domain = config.get('domain')

        if not self.api_key:
            raise AttributeError("config: mailgun requires api_key")

        if not self.domain:
            raise AttributeError("config: mailgun requires domain")

        return

    def send(self, message):
        data = self.create_message_data(message)
        result = requests.post(self.api_url + '/' + self.domain + '/messages', data, auth=('api', self.api_key))
        return result.status_code is 200

    def create_message_data(self, message):
        to = []
        for key, value in message.to.iteritems():
            if value:
                to.append(value + '<' + key + '>')
            else:
                to.append(key)

        cc = []
        for key, value in message.cc.iteritems():
            if value:
                to.append(value + '<' + key + '>')
            else:
                to.append(key)

        bcc = []
        for key, value in message.bcc.iteritems():
            if value:
                to.append(value + '<' + key + '>')
            else:
                to.append(key)

        data = {}
        if message.from_name:
            data['from'] = message.from_name + '<' + message.from_email + '>'
        else:
            data['from'] = message.from_email

        if message.from_email != message.reply_to_email:
            if message.reply_to_name:
                data['h:Reply-To'] = message.reply_to_name + '<' + message.reply_to_email + '>'
            else:
                data['h:Reply-To'] = message.reply_to_email

        data['to'] = ','.join(to)

        if cc:
            data['cc'] = ','.join(cc)

        if bcc:
            data['bcc'] = ','.join(cc)

        data['subject'] = message.subject
        data['text'] = message.body_text
        data['html'] = message.body_html
        return data