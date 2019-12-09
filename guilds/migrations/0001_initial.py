# Generated by Django 2.2.7 on 2019-12-09 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0004_auto_20191202_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('world_id', models.PositiveIntegerField(default=1)),
                ('motd', models.CharField(max_length=50)),
                ('creationdata', models.IntegerField()),
                ('checkdata', models.IntegerField()),
                ('description', models.CharField(max_length=77)),
                ('logo_url', models.CharField(max_length=77)),
                ('ownerid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='players.Player')),
            ],
            options={
                'db_table': 'guilds',
            },
        ),
    ]
