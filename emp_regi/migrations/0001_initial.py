# Generated by Django 5.0.2 on 2024-02-29 08:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("emp_email", models.EmailField(max_length=15)),
                ("emp_contact", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "employee",
            },
        ),
    ]
