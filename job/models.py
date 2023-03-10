from django.db import models

# Create your models here.

Job_Type = (
    ('full time', 'full time'),
    ('part time', 'part time'),
)


class job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=Job_Type)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.FloatField(default=0)
    experiance = models.IntegerField(default=1)

    def __str__(self):
        return self.title
