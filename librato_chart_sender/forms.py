from django import forms
import re


class NewConfigForm(forms.ModelForm):

    def __init__(self, form):
        self.form = form
        self.errors = []

    def is_valid(self):

        if self.__validate_emails(self.form.get('recipients')) and \
           self.__validate_integers(self.form.get('chart_ids')):
            return True
        else:
            return False

    def errors(self):
        self.errors

    def __validate_email(self, email):
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        return True if re.match(email_regex, email) else False

    def __validate_emails(self, emails_list):
        for email in emails_list:
            if not self.__validate_email(email):
                self.errors.append('{email} is not valid.'.format(email=email))
                return False
        return True

    def __validate_integers(self, integers):
        for integer in integers:
            if not self.__validate_integer(integer):
                self.errors.append('{integer} is not valid.'.format(integer=integer))
                return False
        return True

    def __validate_integer(self, number):
        integer_regex = r"^-?[0-9]+$"
        return True if re.match(integer_regex, number) else False
