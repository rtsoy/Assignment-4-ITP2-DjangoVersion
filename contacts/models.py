from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=32, null=False)
    phone_number = models.CharField(max_length=32, null=False)
    email = models.EmailField(max_length=64)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self) -> str:
        return f'{self.name} | {self.phone_number} | {self.email}'
