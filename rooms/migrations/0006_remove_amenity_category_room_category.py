# Generated by Django 4.1.2 on 2022-10-21 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_options'),
        ('rooms', '0005_rename_romm_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amenity',
            name='category',
        ),
        migrations.AddField(
            model_name='room',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category'),
        ),
    ]
