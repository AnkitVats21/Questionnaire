# Generated by Django 3.1.2 on 2020-10-14 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz_Portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='type',
            field=models.CharField(choices=[('MCQ', 'MCQ'), ('True_Flase', 'True_False'), ('Description', 'Description')], max_length=50),
        ),
    ]