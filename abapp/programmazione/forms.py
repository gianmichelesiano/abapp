from django import forms
from django.contrib import admin


class EserciziAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EserciziAdminForm, self).__init__(*args, **kwargs)
        self.fields['rinforzo'].widget = admin.widgets.AdminTextareaWidget()