from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from mezzanine.core.admin import TabularDynamicInlineAdmin

from .models import *

# Register your models here.


# class Slide(TabularDynamicInlineAdmin):
#      pass
#
#
# class IconBlurb(TabularDynamicInlineAdmin):
#      pass
#

# class HomePage(admin.ModelAdmin):
#     pass
     # inlines = [
     #     Slide,
     #     IconBlurb,
     # ]

admin.site.register(HomePage)
admin.site.register(Slide)
admin.site.register(IconBlurb)
