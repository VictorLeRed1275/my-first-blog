# Generated by Django 2.1 on 2019-03-25 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190325_1422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemreview',
            old_name='text',
            new_name='review',
        ),
        migrations.RenameField(
            model_name='postcomment',
            old_name='text',
            new_name='comment',
        ),
    ]