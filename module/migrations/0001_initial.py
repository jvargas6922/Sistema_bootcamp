# Generated by Django 5.0.6 on 2024-07-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id_module', models.AutoField(primary_key=True, serialize=False)),
                ('module', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'modules',
                'managed': False,
            },
        ),
    ]
