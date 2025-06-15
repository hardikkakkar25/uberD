# admin.py
from django.contrib import admin
from .models import PricingConfig, TimeMultiplier, ConfigChangeLog

class TimeMultiplierInline(admin.TabularInline):
    model = TimeMultiplier
    extra = 1

@admin.register(PricingConfig)
class PricingConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    inlines = [TimeMultiplierInline]

@admin.register(ConfigChangeLog)
class ConfigChangeLogAdmin(admin.ModelAdmin):
    list_display = ('config', 'actor', 'timestamp')
    readonly_fields = ('timestamp',)
