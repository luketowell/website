from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(150)

    def __str__(self):
        return self.caption()

    class Meta:
        verbose_name_plural = "Tags"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=255)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

# Post Model
class Post(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True db_index = True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super.save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug} - {self.title} (Published on: {self.date})"
    

