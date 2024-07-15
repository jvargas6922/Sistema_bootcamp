from django.db import models
from challenge.models import Challenge
from student.models import Student


# Create your models here.
class Rating(models.Model):
    id_qualification = models.AutoField(primary_key=True)
    qualification = models.IntegerField()
    feedback = models.CharField(max_length=150)
    id_challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    id_student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'ratings'

    def __str__(self):
        return self.qualification