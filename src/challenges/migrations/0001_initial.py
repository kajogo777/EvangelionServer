# Generated by Django 2.2.1 on 2019-09-13 22:08

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bible', '0004_auto_20190914_0000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_date', models.DateField()),
                ('question', models.TextField(max_length=1000)),
                ('reward_color', models.CharField(max_length=10)),
                ('reward_name', models.CharField(max_length=100)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bible.BibleBook')),
                ('chapter', smart_selects.db_fields.ChainedForeignKey(chained_field='book', chained_model_field='book', on_delete=django.db.models.deletion.PROTECT, to='bible.BibleChapter')),
                ('end_verse', smart_selects.db_fields.ChainedForeignKey(chained_field='chapter', chained_model_field='chapter', on_delete=django.db.models.deletion.PROTECT, related_name='end_challenge', to='bible.BibleVerse')),
            ],
        ),
    ]
