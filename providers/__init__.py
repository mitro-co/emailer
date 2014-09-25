import config

from mailgun import Mailgun
from mandrill import Mandrill
from smtp import SMTP

_provider = None


def get_provider(provider):
    global _provider

    if _provider is not None:
        return _provider

    if provider == 'mailgun':
        _provider = Mailgun(config.mailgun)
    elif provider == 'mandrill':
        _provider = Mandrill(config.mandrill)
    elif provider == 'smtp':
        _provider = SMTP(config.smtp)
    else:
        raise AttributeError('provider "' + provider + '" must be one of: mailgun|mandrill|smtp')

    return _provider