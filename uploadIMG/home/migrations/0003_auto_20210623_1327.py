# Generated by Django 2.0.6 on 2021-06-23 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210623_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catagory',
            old_name='mane',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='catagory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Catagory'),
        ),
    ]
