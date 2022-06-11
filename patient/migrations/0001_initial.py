# Generated by Django 3.1.3 on 2021-04-28 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='p_Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='p_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('personal_address', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('place', models.CharField(max_length=30)),
                ('pincode', models.IntegerField(default=0)),
                ('email_id', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('mob', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.p_login')),
            ],
        ),
    ]
