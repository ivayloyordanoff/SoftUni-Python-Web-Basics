from django import forms

from onlineLibraryProject.online_library_app.models import Profile, Book


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
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
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'URL',
                }
            ),
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            Book.objects.all().delete()
            self.instance.delete()

        return self.instance


class BookBaseForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image': forms.TextInput(
                attrs={
                    'placeholder': 'Image',
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Fiction, Novel, Crime..'
                },
            )
        }


class BookCreateForm(BookBaseForm):
    pass


class BookEditForm(BookBaseForm):
    pass


class BookDeleteForm(BookBaseForm):
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
