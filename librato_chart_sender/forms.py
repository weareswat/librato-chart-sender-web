from django import forms

class NewConfigForm(forms.ModelForm):

    def __init__(self, form):
        self.form = form
        self.errors = []

    def is_valid(self):
        print self.form.get('email')
        print self.form.get('api-key')
        print ','.join(self.form.getlist('chart_ids'))
        print self.form.getlist('recipients')
        return True

    def errors(self):
        self.errors

    def __validate_email(self):
        self.errors.append('Email is not valid.')
        return True

    def __validate_chart_ids(self):
        return True