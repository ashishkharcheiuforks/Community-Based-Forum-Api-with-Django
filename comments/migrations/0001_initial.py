# Generated by Django 2.2 on 2019-08-06 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, default='', max_length=10000, null=True)),
                ('votes', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('sticky', models.BooleanField(default=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('parent_id', models.IntegerField(default=-1, null=True)),
            ],
            options={
                'ordering': ('-votes', '-creation_date'),
            },
        ),
    ]