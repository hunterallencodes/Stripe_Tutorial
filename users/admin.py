from django.contrib import admin

from .models import Profile, Subscription, User


class SubscriptionInline(admin.TabularInline):
    model = Subscription


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = [
        'is_superuser',
        'groups',
        'username',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'email',
    ]
    inlines = [
        SubscriptionInline
    ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user',]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_active',]
    list_editable = ['is_active',]
