# Generated by Django 4.1.7 on 2023-03-06 21:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_alter_project_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="description",
            field=models.TextField(default=""),
        ),
    ]