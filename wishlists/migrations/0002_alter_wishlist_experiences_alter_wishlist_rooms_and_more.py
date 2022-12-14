# Generated by Django 4.1.2 on 2022-10-24 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experiences', '0005_alter_experiences_category_alter_experiences_host_and_more'),
        ('rooms', '0007_alter_room_amenity_alter_room_category_and_more'),
        ('wishlists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='experiences',
            field=models.ManyToManyField(related_name='wishlists', to='experiences.experiences'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='rooms',
            field=models.ManyToManyField(related_name='wishlists', to='rooms.room'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to=settings.AUTH_USER_MODEL),
        ),
    ]
