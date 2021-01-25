# Generated by Django 3.0.2 on 2021-01-21 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='expense',
            fields=[
                ('expId', models.AutoField(primary_key=True, serialize=False)),
                ('expName', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('comments', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.user_details')),
            ],
        ),
    ]