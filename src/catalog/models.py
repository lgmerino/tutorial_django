# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

"""
AFRICA = 1
ANTARCTICA = 2
ASIA = 3
EUROPE = 4
NORTH_AMERICA = 5
OCEANIA = 6
SOUTH_AMERICA = 7
CONTINENT_CHOICES = ((AFRICA, 'África'),
                     (ANTARCTICA, 'Antártida'),
                     (ASIA, 'Asia'),
                     (EUROPE, 'Europa'),
                     (NORTH_AMERICA, 'América del norte'),
                     (OCEANIA, 'Oceanía'),
                     (SOUTH_AMERICA, 'América del sur'),)


def band_image_upload_to(instance, filename):
    ts = time.time()
    fileName, fileExtension = os.path.splitext(filename)
    return 'band_image/%s%s' % (ts, fileExtension)
"""


class Band(models.Model):
    name = models.CharField(max_length=150,
                            blank=False,
                            help_text='Nombre del grupo musical')
    web = models.URLField(blank=True, default='')
    bio = models.TextField(blank=False, help_text='Biografía del grupo')
    """
    continent = models.IntegerField(null=False, blank=False, choices=CONTINENT_CHOICES)
    image = models.ImageField(
        null=False,
        with_field=800, height_field=600,
        upload_to=band_image_upload_to,
        help_text='Foto del grupo')
    """