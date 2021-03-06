# Generated by Django 3.2 on 2021-05-18 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': '新闻栏目'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='title',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.category', verbose_name='category'),
        ),
    ]
