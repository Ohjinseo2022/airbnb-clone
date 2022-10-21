# Generated by Django 4.1.2 on 2022-10-21 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_options'),
        ('experiences', '0003_perk_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perk',
            name='category',
        ),
        migrations.AddField(
            model_name='experiences',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category'),
        ),
    ]
