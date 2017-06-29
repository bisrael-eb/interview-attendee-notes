from django.db import models

# Create your models here.
class Attendee(models.Model):
    class Meta:
        db_table = 'attendees'

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def to_dict(self):
        return dict(
            first_name=self.first_name,
            last_name=self.last_name
        )

