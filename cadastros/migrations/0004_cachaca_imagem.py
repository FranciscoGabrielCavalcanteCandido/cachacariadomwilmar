# Generated by Django 4.2.4 on 2024-01-25 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_remove_cachaca_uf'),
    ]

    operations = [
        migrations.AddField(
            model_name='cachaca',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='imagens/', verbose_name='Imagem'),
        ),
    ]