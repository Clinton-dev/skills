# Generated by Django 4.2.3 on 2023-08-08 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_remove_blogs_link_blogs_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='links',
            field=models.URLField(blank=True, null=True),
        ),
    ]
