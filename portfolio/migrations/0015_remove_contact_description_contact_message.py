# Generated by Django 4.2.3 on 2023-08-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_alter_blogs_links'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='description',
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
