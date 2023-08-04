from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    auction = models.BooleanField(help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#
# # max_digits - максимальное кол-во цифр в числе
# decimal_places = число знаков после запятой

# 1_000_000_000,00
