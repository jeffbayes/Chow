from django.db import models

class DishEntry(models.Model):
    venue_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    avg_rating = models.FloatField(null=True)
    ratings = models.IntegerField()


    def __unicode__(self):
        return self.name
