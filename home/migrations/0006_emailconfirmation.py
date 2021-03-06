# Generated by Django 2.1.3 on 2018-12-09 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_assignment_email_confirmed'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailConfirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=250)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Assignment')),
            ],
        ),
    ]
