# Generated by Django 3.2.7 on 2021-09-30 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_auto_20210925_0117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='third_name',
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='company',
            name='companies',
            field=models.ManyToManyField(blank=True, related_name='_app_company_companies_+', to='app.Company', verbose_name='Компании-Партнеры'),
        ),
    ]
