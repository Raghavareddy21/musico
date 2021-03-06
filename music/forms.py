from django import forms
from django.contrib.auth.models import User
from djng.forms import fields, NgDeclarativeFieldsMetaclass, NgModelFormMixin, NgForm
from . import models

class MovieForm(forms.ModelForm):

    class Meta:
        model = models.movielist
        fields = ('name', 'about', 'date', 'image')


class SongForm(forms.ModelForm):

    class Meta:
        model = models.song
        fields = ('album', 'song_name', 'artist', 'song_location')
class musicForm(forms.Form):
    search_box = forms.CharField(label='search_box', max_length=100)


    # def save(self):
    #     #saves the data to database
    #
    #     user = movielist.objects.create(
    #     name=self.cleaned_data.get('name'),
    #     about=self.cleaned_data.get('about'),
    #     date=self.cleaned_data.get('date'),
    #     image=self.cleaned_data.get('image'),
    #     )
