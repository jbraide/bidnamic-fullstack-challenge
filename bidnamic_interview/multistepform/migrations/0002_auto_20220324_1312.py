# Generated by Django 3.2.12 on 2022-03-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multistepform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodataandbiddinginformation',
            name='bidding_setting',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biodataandbiddinginformation',
            name='google_ads_id',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
