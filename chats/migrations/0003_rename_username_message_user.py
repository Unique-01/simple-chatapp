# Generated by Django 3.2.16 on 2022-12-26 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_rename_user_message_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='username',
            new_name='user',
        ),
    ]