# Generated by Django 3.2 on 2021-05-16 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='keywords',
            field=models.CharField(blank=True, help_text='Optional keywords to be used in the HTML title tag. If left blank, the main keywords field will be used.', max_length=500, null=True, verbose_name='Keywords'),
        ),
    ]
