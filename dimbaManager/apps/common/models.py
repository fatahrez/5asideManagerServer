from django.db import models


class CustomManager(models.Manager):
    """
    Filter not return deleted objects
    """
    def get_queryset(self):
        return super(CustomManager, self).get_queryset().filter(deleted=False, is_active=True)
    

class CommonFieldsMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    is_active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False, help_text="This is for soft delete")

    # everything will be used to query deleted objects e.g. Models.everything.all()
    everything = models.Manager()
    objects = CustomManager()

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.is_active = False
        self.save()

    class Meta:
        ordering = ['-updated_at', "-created_at"]
        abstract = True