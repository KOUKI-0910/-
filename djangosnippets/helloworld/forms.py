from django import forms
from helloworld.models import Helloworld, Shop,Sighting

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Helloworld
        fields = ('title', 'problem_image', 'description', 'latitude', 'longitude')
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('name', 'address', 'latitude', 'longitude')
        widgets = {
            'name': forms.HiddenInput(),
            'address': forms.HiddenInput(),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

class SightingForm(forms.ModelForm):
    class Meta:
        model = Sighting
        fields = ['sighting_location', 'sighting_datetime', 'sighting_image']
        labels = {
            'sighting_location': '目撃場所',
            'sighting_datetime': '目撃日時',
            'sighting_image': '画像',
        }
        widgets = {
            'sighting_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }