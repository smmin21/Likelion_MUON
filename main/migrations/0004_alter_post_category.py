# Generated by Django 3.2.2 on 2021-11-09 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('information', '정보'), ('review', '후기'), ('etc', '잡담')], default='top', max_length=100, verbose_name='카테고리'),
        ),
    ]