# Generated by Django 2.2.3 on 2019-08-03 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saccoapp', '0004_auto_20190803_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telleraccountbalance',
            name='amount',
            field=models.IntegerField(default=0.0, max_length=50),
        ),
    ]
