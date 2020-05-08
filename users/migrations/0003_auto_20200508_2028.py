# Generated by Django 2.2.10 on 2020-05-08 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='branch',
            field=models.CharField(
                choices=[
                    ('COE', 'Computer Engineering'),
                    ('CSE', 'Computer Science Engineering'),
                    ('ECE', 'Electroincs and Communications Engineering'),
                    ('ENC', 'Electroincs and Computer Engineering'),
                    ('COBS', 'Computer Science and Business Studies'),
                    ('CE', 'Chemical Engineering'),
                    ('CiE', 'Civil Engineering'),
                    ('BiE', 'Biotechnology'),
                    ('BME', 'Biomedical Engineering'),
                    ('SE', 'Structural Engineering'),
                    ('IE', 'Infrastructure Engineering'),
                    ('ME', 'Mechanical Engineering'),
                    ('MEC', 'Mechatronics Engineering'),
                    ('EE', 'Electrical Engineering'),
                    ('ECE', 'Electroinc (Instrumentation and Control)'),
                    ('ME(P)', 'Mechanical (Production) Engineering'),
                    ('BE-MBA(ME)', 'Mechanical MBA Dual Degree'),
                    ('BE-MBA(ECE)', 'Electroincs MBA Dual Degree'),
                    ('Others', 'Other'),
                ],
                max_length=11,
            ),
        ),
    ]
