from django.db import models
from django.contrib import admin
from django.utils.html import format_html

class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=80,)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=12, decimal_places=2, help_text="От 0 до 1.000.000.000")
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    @admin.display(description="Дата создания")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M")
            return format_html("<span style='color: green'>Сегодня в {}</span>", created_time)
        return self.created_at

    @admin.display(description="Дата последнего обновления")
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M")
            return format_html("<span style='color: coral'>Сегодня в {}</span>", updated_time)
        return self.updated_at


    class Meta:
        db_table="advertisements"
        verbose_name="Объявление"
        verbose_name_plural="объявления"

    def __str__(self):
        return f"<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})"
#
# # max_digits - максимальное кол-во цифр в числе
# decimal_places = число знаков после запятой

# 1_000_000_000,00