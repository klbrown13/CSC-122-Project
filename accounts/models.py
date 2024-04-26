from django.contrib.auth.models import AbstractUser
from django.db import models


STATUS = (("Looking for Work", "Looking for Work"),
          ("Looking for an Internship", "Looking for an Internship"))
JOB_TYPE = (("Full-Time", "Full-Time"),
          ("Part-Time", "Part-Time"))

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    work_status = models.CharField(max_length=30, choices = STATUS, default='Looking for Work')
    job_type = models.CharField(max_length=30, choices = JOB_TYPE, default='Full-Time')