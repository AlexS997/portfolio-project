from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=256)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100] + "..."

    def pub_date_better(self):
        return self.pub_date.strftime('%b %e %Y')
