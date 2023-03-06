# Generated by Django 3.2.16 on 2023-03-06 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0002_alter_userprofile_default_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('email_subscription', models.BooleanField(default=False)),
                ('message', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='message', to='profiles.userprofile')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]