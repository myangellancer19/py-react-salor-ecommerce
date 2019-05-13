# Generated by Django 2.0.3 on 2018-08-03 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("discount", "0010_auto_20180724_1251")]

    operations = [
        migrations.CreateModel(
            name="VoucherTranslation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("language_code", models.CharField(max_length=10)),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "voucher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="discount.Voucher",
                    ),
                ),
            ],
        ),
        migrations.AlterUniqueTogether(
            name="vouchertranslation", unique_together={("language_code", "voucher")}
        ),
    ]
