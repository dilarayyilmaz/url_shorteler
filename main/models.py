
import string
import random
from django.db import models

def generate_random_slug():
    while True:
        slug = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        if not UrlData.objects.filter(slug=slug).exists():
            return slug

class UrlData(models.Model):
    url = models.URLField(max_length=500, verbose_name="Orjinal URL")
    slug = models.SlugField(max_length=10, unique=True, blank=True, help_text="Otomatik oluşturulur.")

    def save(self, *args, **kwargs):
        if not self.pk or not self.slug:
            self.slug = generate_random_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug} -> {self.url[:30]}..."