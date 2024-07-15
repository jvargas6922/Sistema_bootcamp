from django.db import models
from section.models import Section

# Create your models here.
class Content(models.Model):
    id_content = models.AutoField(primary_key=True)
    content = models.CharField(max_length=120)
    id_section = models.ForeignKey(Section, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'contents'

    def __str__(self):
        return self.content