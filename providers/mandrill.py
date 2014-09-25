import json

import requests
from templates import Message


class Mandrill:

    api_url = 'https://mandrillapp.com/api/1.0'

    def __init__(self, config):
        self.api_key = config.get('api_key');

        if not self.api_key:
            raise AttributeError("config: mandrill requires api_key")

        return

    def send(self, message):
        data = self.create_message_data(message)

        headers = {'content-type': 'application/json'}
        result = requests.post(self.api_url + '/messages/send.json', data, headers=headers)
        return result.status_code is 200

    def create_message_data(self, message=Message):
        data = {'key': self.api_key, 'message': {}}
        data['message']['html'] = message.body_html
        data['message']['text'] = message.body_text
        data['message']['subject'] = message.subject
        data['message']['from_email'] = message.from_email
        data['message']['from_name'] = message.from_name

        if message.from_email != message.reply_to_email:
            if message.reply_to_name:
                data['message']['headers'] = {'Reply-To': message.reply_to_name + ' <' + message.reply_to_email + '>'}
            else:
                data['message']['headers'] = {'Reply-To': message.reply_to_email}

        to = []
        for key, value in message.to.iteritems():
            to.append({
                'email': key,
                'name': value,
                'type': 'to'
            })

        for key, value in message.cc.iteritems():
            to.append({
                'email': key,
                'name': value,
                'type': 'cc'
            })

        for key, value in message.bcc.iteritems():
            to.append({
                'email': key,
                'name': value,
                'type': 'bcc'
            })

        data['message']['to'] = to

        return json.dumps(data, separators=(',',':'))