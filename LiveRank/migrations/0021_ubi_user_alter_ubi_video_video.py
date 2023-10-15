# Generated by Django 4.2.3 on 2023-07-20 14:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("LiveRank", "0020_chatsession_chatmessage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ubi_user",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("shoulder_right", models.TextField(default="")),
                ("shoulder_left", models.TextField(default="")),
                ("leg_right", models.TextField(default="")),
                ("leg_left", models.TextField(default="")),
            ],
        ),
        migrations.AlterField(
            model_name="ubi_video",
            name="video",
            field=models.FileField(upload_to="%Y/%m/%d/%H/%M"),
        ),
    ]
