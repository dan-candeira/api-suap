# Generated by Django 2.2.4 on 2019-12-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20191202_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campus',
            old_name='campi',
            new_name='campus',
        ),
        migrations.AlterField(
            model_name='guiche',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Em atendimento'),
        ),
    ]