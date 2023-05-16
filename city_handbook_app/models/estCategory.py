from django.db import models

class EstCategory(models.Model):

    name = models.CharField("Категирия заведения", max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) ->str:
        return self.name



