from django.contrib import admin
from profile_api.models import UserProfile, ProfileFeedModel
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(ProfileFeedModel)
