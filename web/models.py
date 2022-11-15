from django.conf import Settings
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.urls import reverse

# Create your models here.

# adding the Blog model
class Blog(models.Model):
    title = models.CharField(max_length=200)
    overview = RichTextUploadingField(blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # comment_count = models.IntegerField(default=0)
    # author = models.ForeignKey(Author, auto_created=True, on_delete=models.CASCADE)
    # views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def __str__(self):
        return f"{self.slug} {self.title} {self.image}"

    def get_absolute_url(self):
        return reverse('details', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-timestamp']


    def get_field_values(self):
        return [field.value_to_string(self) for field in Blog._meta.fields]

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = RichTextUploadingField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    aprroved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

