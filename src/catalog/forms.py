from django import forms

from catalog import models as catalog_models


class BandCreateForm(forms.ModelForm):
    class Meta:
        model = catalog_models.Band
        fields = ('name',
                  'web',
                  'bio',)
