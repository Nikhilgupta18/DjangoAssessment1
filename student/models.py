from django.db import models

# Create your models here.

class Section(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    


class Student(models.Model):
    name = models.CharField(max_length=256)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=False, blank=False, related_name='section')


    def __str__(self):
        return self.name
