from django.db import models


class Cake(models.Model):
    weight = models.PositiveIntegerField(null=False, verbose_name="Peso de la torta")
    name = models.CharField(max_length=100, null=False, verbose_name="Nombre de la torta")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

