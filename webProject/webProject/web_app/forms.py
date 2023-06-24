from django import forms
from django.forms import HiddenInput

from webProject.web_app.models import ProfileModel, FruitModel


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = ProfileModel
        exclude = ('image_url', 'age',)
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password',
                }
            )
        }
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }


class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = ProfileModel
        exclude = ('email', 'password',)
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
            'age': 'Age',
        }


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            FruitModel.objects.all().delete()
            self.instance.delete()

        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = HiddenInput()


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'


class FruitCreateForm(FruitBaseForm):
    class Meta:
        model = FruitModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Fruit Image URL',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit Description',
                }
            ),
            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': 'Nutrition Info',
                }
            ),
        }
        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }


class FruitEditForm(FruitBaseForm):
    class Meta:
        model = FruitModel
        fields = '__all__'
        labels = {
            'image_url': 'Image URL',
        }


class FruitDeleteForm(FruitBaseForm):
    class Meta:
        model = FruitModel
        exclude = ('nutrition',)
        labels = {
            'image_url': 'Image URL',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
