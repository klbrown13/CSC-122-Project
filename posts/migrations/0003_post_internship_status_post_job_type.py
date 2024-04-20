# Generated by Django 4.2.11 on 2024-04-20 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="internship_status",
            field=models.CharField(
                choices=[
                    ("Internship", "Internship"),
                    ("Not an Internship", "Not an Internship"),
                ],
                default="Internship",
                max_length=200,
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="job_type",
            field=models.CharField(
                choices=[("Full-Time", "Full-Time"), ("Part-Time", "Part-Time")],
                default="Full-Time",
                max_length=200,
            ),
        ),
    ]
