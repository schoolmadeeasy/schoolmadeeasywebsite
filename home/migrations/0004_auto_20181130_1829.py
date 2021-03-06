# Generated by Django 2.1.3 on 2018-11-30 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20181121_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='media/uploads/')),
                ('order', models.PositiveIntegerField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='image',
        ),
        migrations.AddField(
            model_name='assignmentimage',
            name='assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Assignment'),
        ),
    ]
