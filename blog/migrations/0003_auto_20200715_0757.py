# Generated by Django 3.0.8 on 2020-07-15 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author_bio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ('-published_at',)},
        ),
    ]
