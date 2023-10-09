# Generated by Django 4.2.6 on 2023-10-07 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Modulo",
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
                (
                    "order",
                    models.PositiveIntegerField(
                        db_index=True, editable=False, verbose_name="order"
                    ),
                ),
                ("titulo", models.CharField(max_length=64)),
                ("publico", models.TextField()),
                ("descricao", models.TextField()),
            ],
            options={
                "ordering": ("order",),
                "abstract": False,
            },
        ),
    ]
