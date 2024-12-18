from django.contrib import admin

import dimbaManager.apps.users.models as models

admin.site.register(models.User)
admin.site.register(models.NormalUser)
admin.site.register(models.Captain)
admin.site.register(models.FieldManager)
admin.site.register(models.StaffManager)
admin.site.register(models.Admin)


