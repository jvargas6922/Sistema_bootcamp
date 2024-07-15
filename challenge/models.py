from django.db import models
from content.models import Content
# Create your models here.

class Challenge(models.Model):
    id_challenge = models.AutoField(primary_key=True)
    challenge = models.CharField(max_length=100)
    id_content = models.ForeignKey(Content, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'challenges'

    def __str__(self):
        return self.challenge
