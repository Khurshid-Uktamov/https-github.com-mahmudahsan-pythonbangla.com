# Generated by Django 2.0.5 on 2018-05-28 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_topiccategory_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteoption',
            name='meta_author',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='siteoption',
            name='meta_description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='siteoption',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
