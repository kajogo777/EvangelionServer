# Generated by Django 2.2.1 on 2019-07-12 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_auto_20190712_0933'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='response',
            unique_together={('user', 'challenge', 'answer')},
        ),
    ]
