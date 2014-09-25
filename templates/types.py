import urllib

import config
import templates
from templates import Message


class NewUserInvitationEmail:
    subject = '{sender} has shared an account with you'
    type = 'new_user_invitation'
    template = 'new-user-invitation'

    def __init__(self):
        return

    def get_message(self, item):
        args = item.get_arguments()

        sender_email = args[0]
        recipient_email = args[1]
        temp_password = args[2]

        url_args = {
            'u': recipient_email,
            'p': temp_password,
        }

        login_url = urllib.basejoin(config.service_url, 'install.html' + '#' + urllib.urlencode(url_args))

        variables = {
            'sender_email': sender_email,
            'recipient_email': recipient_email,
            'temp_password': temp_password,
            'login_url': login_url,
        }

        subject = self.subject.format(sender=sender_email)

        html = templates.get_html_content(self.template, variables)
        text = templates.get_text_content(self.template, variables)

        return Message(subject, recipient_email, None, text, html)


class AddressVerificationEmail:
    subject = 'Verify your {service} account'
    type = 'address_verification'
    template = 'address-verification'

    def __init__(self):
        return

    def get_message(self, item):
        subject = self.subject.format(service=config.service_name)

        args = item.get_arguments()
        to = args[0]

        url_args = {
            'user': args[0],
            'code': args[1],
        }

        variables = {
            'verification_link': urllib.basejoin(config.service_url,
                                                 'mitro-core/user/VerifyAccount' + '?' + urllib.urlencode(url_args)),
            'service': config.service_name
        }

        html = templates.get_html_content(self.template, variables)
        text = templates.get_text_content(self.template, variables)

        return Message(subject, to, None, text, html)


class NewDeviceLoginEmail:
    subject = '{service}: Verify your account for a new device'
    type = 'new_device_login'
    template = 'new-device-login'

    def __init__(self):
        return

    def get_message(self, item):
        subject = self.subject.format(service=config.service_name)

        args = item.get_arguments()
        recipient_email = args[0]
        token = args[1]
        token_signature = args[2]

        url_args = {
            'user': recipient_email,
            'token': token,
            'token_signature': token_signature
        }

        variables = {
            'verification_link': urllib.basejoin(config.service_url,
                                                 'mitro-core/user/VerifyDevice' + '?' + urllib.urlencode(url_args)),
            'service': config.service_name
        }

        html = templates.get_html_content(self.template, variables)
        text = templates.get_text_content(self.template, variables)

        return Message(subject, recipient_email, None, text, html)


class IssueReportedEmail:
    subject = '%(service) issue report (id: %(id) url: %(url))'
    type = 'issue_reported'
    template = 'issue-reported'

    def __init__(self):
        return

    def get_message(self, item):
        return None
        # args = item.get_arguments()
        # user_email_address = args[0]
        # url = args[1]
        # issue_type = args[2]
        # description = args[3]
        # issue_id = args[4]
        #
        # subject = self.subject % {'service': config.service_name, 'id': issue_id, 'url': url}
        #
        # variables = {
        # 'issue_id': issue_id,
        #     'user_email': user_email_address,
        #     'url': url,
        #     'issue_type': issue_type,
        #     'description': description
        # }
        #
        # html = templates.get_html_content(self.template, variables)
        # text = templates.get_text_content(self.template, variables)
        #
        # return Message(subject, config.support_email, None, text, html)


class ProductVerifyEmail:
    type = 'product-verify'
    template = 'product-verify'

    def __init__(self):
        return

    def get_message(self, item):
        return None


class OnboardVerifyEmail:
    type = 'onboard-verify'
    template = 'onboard-verify'

    def __init__(self):
        return

    def get_message(self, item):
        return None


class ShareToRecipientWebNewUserEmail:
    type = 'share-to-recipient-web-new-user'
    template = 'share-to-recipient-web-new-user'

    def __init__(self):
        return

    def get_message(self, item):
        return None


class OnboardFirstSecretEmail:
    subject = 'Congratulations on saving your first secret!'
    type = 'onboard-first-secret'
    template = 'onboard-first-secret'

    def __init__(self):
        return

    def get_message(self, item):
        args = item.get_template_params()
        to = args['TO']

        variables = {
            'service': config.service_name
        }

        html = templates.get_html_content(self.template, variables)
        text = templates.get_text_content(self.template, variables)

        return Message(self.subject, to, None, text, html)


class ShareToRecipientWebEmail:
    type = 'share-to-recipient-web'
    template = 'share-to-recipient-web'

    def __init__(self):
        return

    def get_message(self, item):
        return None