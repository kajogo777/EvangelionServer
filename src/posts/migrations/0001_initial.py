# Generated by Django 2.2.10 on 2020-04-18 17:51

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_auto_20191011_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('summary', models.TextField(blank=True, max_length=200, null=True)),
                ('text', ckeditor.fields.RichTextField(config_name='default',
                                                       blank=False,
                                                       null=False)),
                ('active_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PostUser',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(blank=True, choices=[
                 (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('post', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='posts.Post')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='users.User')),
            ],
            options={
                'unique_together': {('post', 'user')},
            },
        ),
        migrations.CreateModel(
            name='PostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='users.Group')),
                ('post', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='posts.Post')),
            ],
            options={
                'unique_together': {('post', 'group')},
            },
        ),
    ]
