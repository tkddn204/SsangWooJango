from django.db import models


class Memo(models.Model):
    name = models.CharField(max_length=10)
    content = models.TextField(blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    reply_count = models.IntegerField(default=0)


class Bbs(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.CharField(max_length=20, blank=True, default='')
    pw = models.CharField(max_length=12, blank=True, default='')
    content = models.TextField()

    class Meta:
        ordering = ('created', )
