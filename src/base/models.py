import uuid

from django.contrib.auth.models import User
from django.utils.functional import cached_property
from django.db import models

from .utils import get_short_id


class TimeAuditModel(models.Model):
    ''' To track when the record was created and last modified'''
    created_at = models.DateTimeField('Created At',
                                      auto_now_add=True)
    updated_at = models.DateTimeField('Updated At',
                                      auto_now=True)

    class Meta:
        abstract = True


class UserAuditModel(models.Model):
    '''To track who created and last modified the record'''
    created_by = models.ForeignKey(User, related_name='created_%(class)s_set',
                                   null=True, blank=True, verbose_name='Created By',
                                   on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='updated_%(class)s_set',
                                   null=True, blank=True, verbose_name='Updated By',
                                   on_delete=models.CASCADE)

    class Meta:
        abstract = True


class AuditModel(TimeAuditModel, UserAuditModel):
    '''To track by who and when was the last record modified'''

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @cached_property
    def get_uuid(self):
        return self.uuid

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.short_id = get_short_id()
        super(UUIDModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class TimeAuditUUIDModel(TimeAuditModel, UUIDModel):

    class Meta:
        abstract = True


class UserAuditUUIDModel(UserAuditModel, UUIDModel):

    class Meta:
        abstract = True


class AuditUUIDModel(AuditModel, UUIDModel):

    class Meta:
        abstract = True