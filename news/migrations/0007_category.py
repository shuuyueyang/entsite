# Generated by Django 3.2 on 2021-05-18 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_news_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_created_date', models.DateTimeField(editable=False, null=True)),
                ('_updated_date', models.DateTimeField(editable=False, null=True)),
                ('seq_number', models.IntegerField(verbose_name='seq_number')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(help_text="Used to build the category's URL.", max_length=255, unique=True, verbose_name='slug')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]