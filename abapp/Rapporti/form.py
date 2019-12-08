
from django import forms
from django.forms import ModelForm, Textarea
from Rapporti.models import  Relazioni
 # forms.py
class RelazioniForm(forms.ModelForm):
  relazione = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'materialize-textarea','rows': 100, 'cols': 100}))
  feedback = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'materialize-textarea','rows': 100, 'cols': 100}))
  class Meta:
    model = Relazioni
    fields = ('__all__')