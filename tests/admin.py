from django.contrib import admin
from .models import Test, TestImages
import admin_thumbnails
# Register your models here.
# Register your models here#
@admin_thumbnails.thumbnail('image') 
class TestGalleryInline(admin.TabularInline):
    model = TestImages
    extra = 1


class TestAdmin(admin.ModelAdmin):
    list_display = ('product_tested', 'client', 'test_type', 'start_date', 'end_date', 'status', 'final_grade')
    inlines = [TestGalleryInline]


admin.site.register(Test, TestAdmin)
admin.site.register(TestImages)