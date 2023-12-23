# Generated by Django 4.2.7 on 2023-11-21 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_alter_movies_options_movies_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='genre',
            field=models.CharField(choices=[('drama', 'Drama'), ('comedy', 'Comedy'), ('science', 'Science Fiction'), ('horror', 'Horror'), ('action', 'Action'), ('romance', 'Romance'), ('fantasy', 'Fantasy')], max_length=150),
        ),
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.movies')),
                ('owner_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'MovieList',
            },
        ),
    ]