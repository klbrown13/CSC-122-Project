from django.conf import settings
from django.db import models
from django.urls import reverse

JOB_TYPE = (
    ("Full-Time", "Full-Time"),
    ("Part-Time", "Part-Time"),
)

INTERNSHIP_STATUS = (
    ("Internship", "Internship"),
    ("Not an Internship", "Not an Internship"),
)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add=True)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=200,
                                choices=JOB_TYPE,
                                default='Full-Time')
    internship_status = models.CharField(max_length=200,
                                choices=INTERNSHIP_STATUS,
                                default='Internship')
    body = models.TextField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("post_list")
    