from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

# Create your models here.

# Post Model
class Post(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True db_index = True)
    content = models.TextField(validators=[MinLengthValidator(10)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super.save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug} - {self.title} (Published on: {self.date})"