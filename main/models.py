from django.db import models

class Staff(models.Model):
    firstname = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.firstname} {self.surname}"
    


class Attendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.start_time} - {self.end_time}"