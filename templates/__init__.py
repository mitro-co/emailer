from .message import Message
from templates.types import *
from tornado import template

types = {
    'new_user_invitation': NewUserInvitationEmail(),
    'address_verification': AddressVerificationEmail(),
    'new-device-login': NewDeviceLoginEmail(),
    'issue_reported': IssueReportedEmail(),
    'product-verify': ProductVerifyEmail(),
    'onboard-verify': OnboardVerifyEmail(),
    'share-to-recipient-web-new-user': ShareToRecipientWebNewUserEmail(),
    'onboard-first-secret': OnboardFirstSecretEmail(),
    'share-to-recipient-web': ShareToRecipientWebEmail()
}


def get_email(email_type):
    return types[email_type]


def get_html_content(template, variables):
    return _generate_template(template + ".html", variables, html_escape=True)


def get_text_content(template, variables):
    return _generate_template(template + ".txt", variables, html_escape=True)


_template_loader = None
_no_escaping_template_loader = None


def _generate_template(name, variables, html_escape):
    '''Loads the template from name (with caching) and renders it using variables.
    If html_escape is False, escaping will be disabled.'''
    # create the template loader once; it caches templates
    global _template_loader
    global _no_escaping_template_loader
    if not html_escape:
        # load templates without autoescaping
        if _no_escaping_template_loader is None:
            _no_escaping_template_loader = template.Loader(config.templates_path, autoescape=None)
        template_loader = _no_escaping_template_loader
    else:
        assert html_escape
        if _template_loader is None:
            _template_loader = template.Loader(config.templates_path, autoescape='xhtml_escape')
        template_loader = _template_loader

    t = template_loader.load(name)
    return t.generate(**variables)