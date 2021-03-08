# Generated by Django 3.1.7 on 2021-03-07 21:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True, verbose_name='Título')),
                ('contenido', models.TextField(null=True, verbose_name='Contenido del post')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='posts/%Y/%m/%d', verbose_name='Imagen del post')),
                ('fecha_alta', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta')),
                ('fecha_actualizacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualización')),
                ('autor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categoria')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'db_table': 'posts',
                'ordering': ['id'],
            },
        ),
    ]
