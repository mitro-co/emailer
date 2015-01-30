import os
from backports import configparser

config = configparser.ConfigParser()
config.read('config.ini.example')

if os.getenv('PROVIDER') is not None:
    config.set('default', 'provider', os.getenv('PROVIDER'))

if os.getenv('SUPPORT_EMAIL') is not None:
    config.set('default', 'support_email', os.getenv('SUPPORT_EMAIL'))

if os.getenv('FROM_NAME') is not None:
    config.set('default', 'from_name', os.getenv('FROM_NAME'))

if os.getenv('FROM_EMAIL') is not None:
    config.set('default', 'from_email', os.getenv('FROM_EMAIL'))

if os.getenv('REPLY_TO_EMAIL') is not None:
    config.set('default', 'reply_to_email', os.getenv('REPLY_TO_EMAIL'))

if os.getenv('REPLY_TO_NAME') is not None:
    config.set('default', 'reply_to_name', os.getenv('REPLY_TO_NAME'))

if os.getenv('TEMPLATES_PATH') is not None:
    config.set('default', 'templates_path', os.getenv('TEMPLATES_PATH'))

if os.getenv('SERVICE_NAME') is not None:
    config.set('default', 'service_name', os.getenv('SERVICE_NAME'))

if os.getenv('SERVICE_URL') is not None:
    config.set('default', 'service_url', os.getenv('SERVICE_URL'))

if os.getenv('STATIC_URL') is not None:
    config.set('default', 'static_url', os.getenv('STATIC_URL'))

if os.getenv('QUEUE_SLEEP_SECONDS') is not None:
    config.set('queue', 'sleep_seconds', os.getenv('QUEUE_SLEEP_SECONDS'))

if os.getenv('DB_HOSTNAME') is not None:
    config.set('database', 'hostname', os.getenv('DB_HOSTNAME'))

if os.getenv('DB_PORT') is not None:
    config.set('database', 'port', os.getenv('DB_PORT'))

if os.getenv('DB_DATABASE') is not None:
    config.set('database', 'database', os.getenv('DB_DATABASE'))

if os.getenv('DB_USERNAME') is not None:
    config.set('database', 'username', os.getenv('DB_USERNAME'))

if os.getenv('DB_PASSWORD') is not None:
    config.set('database', 'password', os.getenv('DB_PASSWORD'))

if os.getenv('SMTP_HOSTNAME') is not None:
    config.set('smtp', 'hostname', os.getenv('SMTP_HOSTNAME'))

if os.getenv('SMTP_PORT') is not None:
    config.set('smtp', 'port', os.getenv('SMTP_PORT'))

if os.getenv('SMTP_USERNAME') is not None:
    config.set('smtp', 'username', os.getenv('SMTP_USERNAME'))

if os.getenv('SMTP_PASSWORD') is not None:
    config.set('smtp', 'password', os.getenv('SMTP_PASSWORD'))

if os.getenv('SMTP_TLS') is not None:
    config.set('smtp', 'tls', os.getenv('SMTP_TLS'))

if os.getenv('MAILGUN_DOMAIN') is not None:
    config.set('mailgun', 'domain', os.getenv('MAILGUN_DOMAIN'))

if os.getenv('MAILGUN_API_KEY') is not None:
    config.set('mailgun', 'api_key', os.getenv('MAILGUN_API_KEY'))


if os.getenv('MANDRILL_API_KEY') is not None:
    config.set('mandrill', 'api_key', os.getenv('MANDRILL_API_KEY'))

cfgfile = open("config.ini", 'w')
config.write(cfgfile)
cfgfile.close()