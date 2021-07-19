from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=200)
    answer1 = models.CharField(max_length=200)
    answer2 = models.CharField(max_length=200)

    def __str__(self):
        return self.question[:10]