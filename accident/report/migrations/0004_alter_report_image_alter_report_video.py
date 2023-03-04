# Generated by Django 4.1.7 on 2023-03-04 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_report_cause_of_accident_report_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='image',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='report',
            name='video',
            field=models.FileField(default=None, upload_to='videos/'),
        ),
    ]
