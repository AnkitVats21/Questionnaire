# Generated by Django 3.1.2 on 2020-10-14 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz_Portal', '0006_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='a_image',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to='uploads/'),
        ),
    ]