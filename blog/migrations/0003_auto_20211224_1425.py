# Generated by Django 3.2.9 on 2021-12-24 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211208_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='facebook_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='gitHub_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='instagram_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='telegram_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='youtube_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]