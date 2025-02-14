from django.contrib import admin
from django.contrib import messages

from electronics.models import NetworkNode


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "supplier", "city", "debt", "created_at")
    list_filter = ("city",)
    search_fields = ("name", "city")
    readonly_fields = ("level", "created_at")
    actions = ["clear_debt"]

    @admin.action(description="Очистить задолженность перед поставщиком")
    def clear_debt(self, request, queryset) -> None:
        updated_count = queryset.filter(debt__gt=0).update(debt=0.00)

        if updated_count > 0:
            self.message_user(request, f"Задолженность очищена у {updated_count} объектов.", level=messages.SUCCESS)
        else:
            self.message_user(request, "Нет объектов с задолженностью для очистки.", level=messages.INFO)

    def supplier_name(self, obj):
        return obj.supplier.name if obj.supplier else "Нет поставщика"
    supplier_name.short_description = 'Поставщик'
