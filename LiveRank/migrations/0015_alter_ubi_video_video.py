# Generated by Django 3.2.5 on 2023-07-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LiveRank', '0014_alter_ubi_video_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ubi_video',
            name='video',
            field=models.FileField(upload_to='media/%Y/%m/%d/'),
        ),
    ]
