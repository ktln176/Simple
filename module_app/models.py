from django.db import models


# Create your models here.
class User(models.Model):
    account = models.CharField(verbose_name='用户账号', max_length=20, primary_key=True)
    account_name = models.CharField(verbose_name='用户名称', max_length=20, null=False)
    password = models.CharField(verbose_name='用户密码', max_length=20, null=False)
    create_time = models.DateTimeField(verbose_name='创建时间', max_length=0, null=False)
    remark = models.TextField(verbose_name='备注', null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['account'], name='account_index')
        ]
