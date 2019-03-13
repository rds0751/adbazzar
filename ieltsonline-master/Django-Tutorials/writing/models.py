from django.db import models

# Create your models here.
class Writing(models.Model):
    Question_Name =  models.CharField(max_length=100, default="Question")
    timeInstruction = models.CharField(max_length=100)
    Question = models.CharField(max_length=1000)
    wordInstruction = models.CharField(max_length=100)
    image_ques = models.ImageField(upload_to='picfolder/', null=True, blank=True)

    def __str__(self):
        return self.Question_Name
