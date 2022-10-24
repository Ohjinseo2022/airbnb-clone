# Generated by Django 4.1.2 on 2022-10-24 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0005_alter_experiences_category_alter_experiences_host_and_more'),
        ('rooms', '0007_alter_room_amenity_alter_room_category_and_more'),
        ('medias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='experience',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medias', to='experiences.experiences'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medias', to='rooms.room'),
        ),
        migrations.AlterField(
            model_name='video',
            name='experience',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='experiences.experiences'),
        ),
    ]