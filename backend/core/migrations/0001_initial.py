# Generated by Django 3.0.8 on 2020-07-02 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='username', max_length=50)),
                ('money', models.IntegerField(default=0)),
                ('gems', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=1)),
                ('damage', models.IntegerField(default=50)),
                ('fiends', models.ManyToManyField(to='core.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField(default=0)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Player')),
            ],
        ),
    ]