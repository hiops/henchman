from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from treasurer.models import Transaction


class Account(models.Model):

    user = models.ForeignKey('auth.User', related_name='accounts')
    name = models.CharField(max_length=255)
    total = models.FloatField(blank=True, default=0)
    limit = models.FloatField(blank=True, default=0)

    class Meta:
        app_label = 'treasurer'

    def __str__(self):
        return '{self.user} "{self.name}" {self.total}'.format(self=self)


@receiver(post_save, sender=Transaction)
def recalculate_total(sender, **kwargs):
    acc = Account.objects.get(id=kwargs['instance'].account_id)
    acc.total += float(kwargs['instance'].total)
    acc.save()
