from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
