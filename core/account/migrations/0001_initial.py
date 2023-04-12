# Generated by Django 3.2 on 2023-04-11 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, verbose_name='Username')),
                ('password', models.CharField(max_length=500, verbose_name='Password')),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=11, unique=True, verbose_name='Phone number')),
                ('national_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='National code')),
                ('birthdate', models.DateField(default='None', help_text="user's birthdate")),
                ('gender', models.CharField(blank=True, default='None', max_length=50, null=True)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'db_table': 'custom_user',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account.customuser')),
            ],
            options={
                'db_table': 'author',
            },
            bases=('account.customuser',),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account.customuser')),
                ('status', models.CharField(choices=[('active', 'active'), ('deactive', 'deactive')], default='English', max_length=100, verbose_name='Language')),
            ],
            options={
                'db_table': 'staff',
            },
            bases=('account.customuser',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account.customuser')),
            ],
            options={
                'db_table': 'student',
            },
            bases=('account.customuser',),
        ),
    ]
