# Generated by Django 2.2.5 on 2020-05-25 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_form', '0003_auto_20181026_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='customer_name',
        ),
        migrations.AddField(
            model_name='feedback',
            name='email',
            field=models.CharField(default='test', max_length=120),
        ),
        migrations.AddField(
            model_name='feedback',
            name='username',
            field=models.CharField(default='test', max_length=120),
        ),
    ]
