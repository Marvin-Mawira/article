from django.db import models
from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)  # Ensures the slug is unique
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(upload_to='thumb', blank=True, null=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        # Ensure the slug is unique
        original_slug = self.slug
        counter = 1
        while Article.objects.filter(slug=self.slug).exists():
            self.slug = f"{original_slug}-{counter}"
            counter += 1

        super().save(*args, **kwargs)

    