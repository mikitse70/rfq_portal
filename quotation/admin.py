from django.contrib import admin
from .models import QuotationLine,QuotationRequest,SupplierBid
admin.site.register(QuotationLine)
admin.site.register(QuotationRequest)
admin.site.register(SupplierBid)

