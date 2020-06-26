# Generated by Django 3.0.7 on 2020-06-25 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('gst', models.CharField(blank=True, max_length=150, null=True)),
                ('logo', models.ImageField(default='partner_photo/default.jpg', upload_to='partner_photo/')),
                ('info', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Partners',
            },
        ),
    ]