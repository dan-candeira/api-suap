# Generated by Django 2.2.4 on 2019-12-02 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20191202_0159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atendimento',
            old_name='fk_atendente',
            new_name='atendente',
        ),
        migrations.RenameField(
            model_name='atendimento',
            old_name='fk_guiche',
            new_name='guiche',
        ),
        migrations.RenameField(
            model_name='atendimento',
            old_name='fk_senha',
            new_name='senha',
        ),
        migrations.RenameField(
            model_name='guiche',
            old_name='fk_campus',
            new_name='campus',
        ),
        migrations.RenameField(
            model_name='senha',
            old_name='fk_categoria',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='senha',
            old_name='fk_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='senha',
            old_name='fk_tipo',
            new_name='tipo',
        ),
    ]