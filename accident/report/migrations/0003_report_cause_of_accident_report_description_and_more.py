# Generated by Django 4.0.5 on 2023-03-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_report_gender_witness_report_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='cause_of_accident',
            field=models.TextField(default='what is the cause?'),
        ),
        migrations.AddField(
            model_name='report',
            name='description',
            field=models.TextField(default='Describe what happened'),
        ),
        migrations.AddField(
            model_name='report',
            name='image',
            field=models.ImageField(default=None, upload_to='static\\images'),
        ),
        migrations.AddField(
            model_name='report',
            name='number_of_death',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='number_of_injured',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='number_of_vehicle_involved',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='video',
            field=models.FileField(default=None, upload_to='static\x0bideos'),
        ),
    ]
