"""Module that provides models to the blog."""
from django.db import models

# Create your models here.

class Author(models.Model):
    """Author model."""
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email_address = models.EmailField(max_length=80)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    """Tag model."""
    caption = models.CharField(max_length=40)

    def __str__(self) -> str:
        return str(self.caption)


class Post(models.Model):
    """Post model."""
    title = models.CharField(max_length=100)
    excerpt = models.TextField()
    image_name = models.CharField(max_length=200)
    date = models.DateField()
    slug = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, null=True)

    def __str__(self) -> str:
        return f"{self.title} - By: {self.author}"
