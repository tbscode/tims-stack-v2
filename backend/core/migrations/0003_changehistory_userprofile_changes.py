# Generated by Django 4.1.2 on 2023-07-02 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_userprofile_last_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('model', models.CharField(max_length=50)),
                ('change_made', models.DateTimeField(auto_now_add=True)),
                ('change', models.JSONField(default=dict)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='change_history_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='changes',
            field=models.ManyToManyField(related_name='user_profile_changes', to='core.changehistory'),
        ),
    ]
