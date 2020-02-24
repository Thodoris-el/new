# Generated by Django 3.0.2 on 2020-02-24 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('api', '0004_user_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.CreateModel(
            name='CUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('userid', models.AutoField(db_column='CUserID', primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='CUsername', max_length=40, unique=True)),
                ('password', models.CharField(db_column='Password', max_length=1000)),
                ('email', models.EmailField(db_column='Email', max_length=125, unique=True)),
                ('firstname', models.CharField(blank=True, db_column='FirstName', max_length=40, null=True)),
                ('lastname', models.CharField(blank=True, db_column='LastName', max_length=40, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
