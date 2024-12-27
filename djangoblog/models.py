from email.policy import default
from pyexpat import model
from re import M
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from tinymce.models import HTMLField
import string  # for string constants
import random  # for generating random strings
from django.utils.text import slugify

class PostsCategory(models.Model):
    catname = models.CharField(max_length=300, default='Post')
    catcreate_date = models.DateField(auto_now_add=True)
    catimg = models.ImageField(null=True, blank=True, upload_to='images/catimg')
    def __str__(self):
        return self.catname
    def get_absolute_url(self):
        return reverse('home')
    # def save(self, *args, **kwargs):
    #     self.postscategories = slugify(self.catname)
    #     return super().save(*args, **kwargs)



class Post(models.Model):
    title = models.CharField(max_length=300)
    authors = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(editable=False, unique=True, blank=True, null=True)
    body = HTMLField()
    featured_content = models.CharField(max_length=250)
    create_date = models.DateField(auto_now_add=True)
    postscategory = models.ForeignKey(PostsCategory, on_delete=models.PROTECT, default=1)
    catslug = models.SlugField(editable=False, unique=True, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    class Meta:
        # order on primary key to make sure it's unique
        ordering = ('-create_date', '-pk')

    def __str__(self):
        return self.title + ' | ' + str(self.authors)  
    
    def get_absolute_url(self):
        return reverse('articleview', args=(str(self.id)))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    def catsave(self, *args, **kwargs):
        self.catslug = slugify(self.postscategories)
        return super().save(*args, **kwargs)
