from django.db import models

class Establishment(models.Model):

    name = models.CharField("Название", max_length=100)
    description = models.CharField("Описание", max_length=2000)
    category = models.ForeignKey("city_handbook_app.estCategory", on_delete=models.CASCADE, related_name="establishments", verbose_name="Категория", null=True)
    city = models.ForeignKey("city_handbook_app.City", on_delete=models.CASCADE, related_name="establishments", verbose_name="Город", null=True)
    address = models.CharField("Адрес", max_length=100)
    contacts = models.CharField("Контакты", max_length=100)
    create_time = models.DateTimeField("Дата создания", auto_now_add=True)
    update_time = models.DateTimeField("Дата обновлени", auto_now=True)

    class Meta:
        verbose_name = "Заведение"
        verbose_name_plural = "Заведения"

    def __str__(self) ->str:
        return self.name



