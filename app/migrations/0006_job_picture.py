# Generated by Django 2.2.4 on 2023-12-22 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_delete_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='picture',
            field=models.CharField(default='piic', max_length=45),
        ),
    ]