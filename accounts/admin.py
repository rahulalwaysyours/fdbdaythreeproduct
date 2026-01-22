from django.contrib import admin
from accounts.models import User

#changing view of admin panel for Product model
class AccountManager(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'date_of_birth',) # comma (,) is used because, it makes tuple
    list_filters = ('is_active',)
    search_fields = ('email',)
    # ordering = ("-id") #sorted using id in reverse order
    ordering = ("-created_at",)

# Register your models here.
admin.site.register(User, AccountManager)