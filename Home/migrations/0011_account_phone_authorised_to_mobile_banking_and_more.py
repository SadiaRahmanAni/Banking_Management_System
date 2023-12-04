# Generated by Django 4.2.1 on 2023-05-11 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_remove_account_phone_authorised_to_mobile_banking'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phone_authorised_to_mobile_banking',
            field=models.CharField(default='NULL', max_length=11),
        ),
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='personalbankingform',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]