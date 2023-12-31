from django.db import models # noqa


class Event(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='events',
                              on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100, blank=False)
    cta_text = models.TextField(max_length=280, blank=False)
    bot_name = models.CharField(max_length=15, blank=False)
    event_start_date = models.DateTimeField()
    event_end_date = models.DateTimeField()

    def __str__(self):
        return self.event_name

    class Meta:
        ordering = ['event_start_date']
