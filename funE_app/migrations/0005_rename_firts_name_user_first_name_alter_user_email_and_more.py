# Generated by Django 4.1.7 on 2023-03-08 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funE_app', '0004_user_email_user_username_alter_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='firts_name',
            new_name='first_name',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=24),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=12),
        ),
    ]
