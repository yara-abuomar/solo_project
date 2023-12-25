# Generated by Django 2.2.4 on 2023-12-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_job_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Liks',
            field=models.ManyToManyField(related_name='like_jobs', to='app.User'),
        ),
        migrations.AlterField(
            model_name='job',
            name='picture',
            field=models.FilePathField(null=True),
        ),
    ]