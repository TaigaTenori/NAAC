from django.forms import ModelForm
from naac import naac_settings as config
from players.models import Player
from django import forms


class CharacterCreationForm(ModelForm):
    vocation = forms.IntegerField(label="Select your vocation", widget=forms.Select(choices=config.VOCATIONS))
    town_id = forms.IntegerField(label="Starting town", widget=forms.Select(choices=config.towns))


    def clean_name(self):
        name = self.cleaned_data['name']
        if Player.objects.filter(name=name).exists():
            raise forms.ValidationError("This name is already in use.")
        return name

    class Meta:
        model = Player
        fields = ['name', 'vocation', 'town_id']
