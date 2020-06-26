from django.contrib import admin
from .models import Partners, Vouchers


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'gst')

admin.site.register(Partners, PartnerAdmin)

class Voucheradmin(admin.ModelAdmin):
    list_display = ('code', 'email', 'expiry')
admin.site.register(Vouchers, Voucheradmin)
