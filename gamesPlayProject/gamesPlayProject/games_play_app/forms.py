from django import forms
from django.forms import HiddenInput

from gamesPlayProject.games_play_app.models import ProfileModel, GameModel


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        widgets = {
            'password': forms.TextInput(
                attrs={'type': 'password'}
            ),
        }


class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = ProfileModel
        fields = (
            'email',
            'age',
            'password',
        )
        widgets = {
            'password': forms.TextInput(
                attrs={'type': 'password'}
            ),
        }


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            GameModel.objects.all().delete()
            self.instance.delete()

        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = HiddenInput()


class GameBaseForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'


class GameCreateForm(GameBaseForm):
    pass


class GameEditForm(GameBaseForm):
    pass


class GameDeleteForm(GameBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
