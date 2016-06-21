import re

class NewConfigForm:

    def __init__(self, form):
        self.form = form
        self.errors = []

    def is_valid(self):
        if all([self.__validate_recipient_emails(self.form.getlist('recipients')),
                self.__validate_integers(self.form.getlist('chart_ids')),
                self.__validate_librato_email(self.form.get('email'))]):
            return True
        else:
            return False

    def get_errors(self):
        return self.errors

    def get_form_values(self):
        return {
            'email_username': self.form.get('email'),
            'api_key': self.form.get('api_key'),
            'chart_ids': self.form.getlist('chart_ids'),
            'recipients': self.form.getlist('recipients')

        }

    def __validate_email(self, email):
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        return True if re.match(email_regex, email) else False

    def __validate_integer(self, number):
        integer_regex = r"^-?[0-9]+$"
        return True if re.match(integer_regex, number) else False

    def __validate_librato_email(self, email):
        if not self.__validate_email(email):
            self.errors.append('{email} is not a valid Librato email/username.'.format(email=email))
            return False
        else:
            return True

    def __validate_recipient_emails(self, emails_list):
        if not emails_list:
            self.errors.append('You must specify at least one recipient')
            return False
        else:
            valid = True
            for email in emails_list:
                if not self.__validate_email(email):
                    self.errors.append('{email} is not a valid recipient email.'.format(email=email))
                    valid = False
            return valid

    def __validate_integers(self, integers):
        if not integers:
            self.errors.append('You must specify at least one chart number')
            return False
        else:
            valid = True
            for integer in integers:
                if not self.__validate_integer(integer):
                    self.errors.append('{integer} is not a valid chart number.'.format(integer=integer))
                    valid = False
            return valid