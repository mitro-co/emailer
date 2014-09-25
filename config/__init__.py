from backports import configparser

_config = configparser.ConfigParser()
_config.read('config.ini')

_default = _config['default']

provider = _default.get('provider', 'smtp')
support_email = _default.get('support_email', 'issues@mitro.co')
from_name = _default.get('from_name', 'Mitro')
from_email = _default.get('from_email', 'no-reply@mitro.co')
reply_to_name = _default.get('reply_to_name', from_name)
reply_to_email = _default.get('reply_to_email', from_email)
templates_path = _default.get('templates_path', 'templates')
service_name = _default.get('service_name', 'Mitro')
service_url = _default.get('service_url', 'https://mitro.co')
static_url = _default.get('static_url', 'https://mitro.co')

queue = _config['queue']
database = _config['database']
smtp = _config['smtp']
mailgun = _config['mailgun']
mandrill = _config['mandrill']