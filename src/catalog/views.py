# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

import forms
import models


class BandCreateView(CreateView):
    model = models.Band
    template_name = 'band/create.html'
    form_class = forms.BandCreateForm

    def get_success_url(self):
        return reverse('BandListView')


class BandListView(ListView):
    model = models.Band
    template_name = 'band/list.html'


class BandUpdateView(UpdateView):
    model = models.Band
    template_name = 'band/create.html'
    form_class = forms.BandCreateForm

    def get_success_url(self):
        return reverse('BandListView')


class BandDeleteView(DeleteView):
    model = models.Band
    template_name = 'band/delete.html'

    def get_success_url(self):
        return reverse('BandListView')
