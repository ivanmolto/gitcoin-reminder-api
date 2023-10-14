from django.db import models # noqa


class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    blurb = models.CharField(max_length=200, blank=False)
    url = models.URLField(max_length=80, blank=True)
    start_date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['start_date']
