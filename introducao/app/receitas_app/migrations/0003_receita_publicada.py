# Generated by Django 3.2.8 on 2021-10-30 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas_app', '0002_receita_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]
