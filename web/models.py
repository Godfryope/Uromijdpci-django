from tkinter import CASCADE
from django.conf import Settings
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.urls import reverse

# Create your models here.

# adding the Project model
class Project(models.Model):
    title = models.CharField(max_length=100)
    overview = RichTextUploadingField(blank=True, null=True)
    projectTitle = RichTextUploadingField(blank=True, null=True)
    projectBrief = RichTextUploadingField(blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    newsfeed = models.BooleanField(null=True, blank=True, default=False)
    
    # comment_count = models.IntegerField(default=0)
    # author = models.ForeignKey(Author, auto_created=True, on_delete=models.CASCADE)
    # views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def __str__(self):
        return f"{self.id} {self.title} {self.image}"

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-timestamp']

    def get_field_values(self):
        return [field.value_to_string(self) for field in Project._meta.fields]

