# Generated by Django 3.0.3 on 2020-08-18 18:55

from django.db import migrations, models
import django.utils.timezone
import hotsite.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=hotsite.models.get_image_path)),
                ('link', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
    ]
