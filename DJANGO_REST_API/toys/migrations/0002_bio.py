# Generated by Django 4.0.5 on 2022-07-23 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unkknown', max_length=100)),
                ('phone_number', models.IntegerField(default='-1')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
