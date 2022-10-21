# Generated by Django 4.0.5 on 2022-10-21 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('StackApp', '0006_delete_thisapp_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_Up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default='', max_length=10)),
                ('profession', models.CharField(default='', max_length=100)),
                ('inst_or_org', models.CharField(default='', max_length=100)),
                ('Address', models.CharField(default='', max_length=150)),
                ('prof_image', models.ImageField(default="{% static 'images/default_profile.jpg' %}", upload_to='projects/profile_images')),
                ('fullname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
