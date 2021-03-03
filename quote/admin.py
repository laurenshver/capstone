from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Quote)
admin.site.register(QuoteTool)
admin.site.register(QuoteStatus)