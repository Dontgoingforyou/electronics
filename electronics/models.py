from django.db import models
from django.core.exceptions import ValidationError
from typing import Optional


class NetworkNode(models.Model):
    LEVEL_FACTORY: int = 0
    LEVEL_RETAIL: int = 1
    LEVEL_IP: int = 2

    LEVEL_CHOICES: list[tuple[int, str]] = [
        (LEVEL_FACTORY, "Завод"),
        (LEVEL_RETAIL, "Розничная сеть"),
        (LEVEL_IP, "Индивидуальный предприниматель"),
    ]

    name: str = models.CharField(max_length=255, verbose_name="Название")
    email: str = models.EmailField(unique=True, verbose_name="Email")
    country: str = models.CharField(max_length=100, verbose_name="Страна")
    city: str = models.CharField(max_length=100, verbose_name="Город")
    street: str = models.CharField(max_length=255, verbose_name="Улица")
    house_number: str = models.CharField(max_length=10, verbose_name="Номер дома")
    supplier: Optional["NetworkNode"] = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='clients', verbose_name="Поставщик"
    )
    debt: float = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Задолженность")
    level: int = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES, editable=False, verbose_name="Уровень")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    def save(self, *args, **kwargs) -> None:
        """ Определяет уровень объекта перед сохранением. """

        if self.supplier:
            if self.supplier.level >= self.LEVEL_IP:
                raise ValidationError("Нельзя назначить ИП поставщиком.")
            self.level = self.supplier.level + 1
        else:
            self.level = self.LEVEL_FACTORY
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} ({self.get_level_display()})"
