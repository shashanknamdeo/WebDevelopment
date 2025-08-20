from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=150)  # Certificate name
    organization = models.CharField(max_length=100)  # Who issued it
    image = models.ImageField(upload_to="certificates/")  # Upload certificate image
    date_issued = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

