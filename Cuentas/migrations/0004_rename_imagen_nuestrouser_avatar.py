# Generated by Django 4.0.4 on 2022-05-03 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cuentas', '0003_alter_nuestrouser_bio_alter_nuestrouser_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nuestrouser',
            old_name='imagen',
            new_name='avatar',
        ),
    ]