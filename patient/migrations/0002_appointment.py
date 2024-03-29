# Generated by Django 3.1.3 on 2021-04-29 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('dr_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.dr_reg')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.p_reg')),
            ],
        ),
    ]
