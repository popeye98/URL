from django.db import models
from django.conf import settings
import random
import string
from .utils import code_generator, create_shortcode

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)
from django_hosts.resolvers import reverse
from .validators import validate_url, validate_dot_com
# making custom all fuction which will overwrite 
# current all function 
# filter out alll active urls
class URLManager(models.Manager):
    def all(self, *args, **kwargs):
        initial = super(URLManager, self).all(*args, **kwargs)
        qs = initial.filter(active=True)
        return qs


class URL(models.Model):
    url = models.URLField(unique=True )
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True,blank=True)
    active      = models.BooleanField(default=True)
    objects = URLManager()  # making instance of that
    
    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(URL, self).save()

    def __str__(self):
        return self.url
    
    def get_short_url(self):
        url_path = reverse("scode", kwargs={'sc': self.shortcode}, host='www', scheme='http')
        print(url_path)
        return url_path
    