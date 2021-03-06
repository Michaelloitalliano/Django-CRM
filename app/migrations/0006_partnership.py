# Generated by Django 3.2.7 on 2021-09-30 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210930_0535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partnership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=30, verbose_name='Должность')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company', verbose_name='Компания')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee', verbose_name='Работник')),
            ],
        ),
    ]
