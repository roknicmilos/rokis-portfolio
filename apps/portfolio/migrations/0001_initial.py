# Generated by Django 5.1.2 on 2024-10-13 17:13

import apps.common.validators
import django.core.validators
import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('school', models.CharField(max_length=100, verbose_name='school')),
                ('degree', models.CharField(max_length=100, verbose_name='degree')),
                ('start', models.DateField(help_text="Day is not important. Select 1st if you don't know the exact start day.", verbose_name='start')),
                ('end', models.DateField(blank=True, help_text="Leave empty if you are currently studying here. Day is not important. Select 1st if you don't know the exact end day.", null=True, verbose_name='end')),
                ('location', models.CharField(max_length=100, verbose_name='location')),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Educations',
            },
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('company', models.CharField(max_length=100, verbose_name='company')),
                ('start', models.DateField(help_text="Day is not important. Select 1st if you don't know the exact start day.", verbose_name='start')),
                ('end', models.DateField(blank=True, help_text="Leave empty if you are currently working here. Day is not important. Select 1st if you don't know the exact end day.", null=True, verbose_name='end')),
                ('location', models.CharField(max_length=100, verbose_name='location')),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'verbose_name': 'Employment',
                'verbose_name_plural': 'Employments',
                'default_related_name': 'employments',
            },
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('company', models.CharField(max_length=100, verbose_name='company')),
                ('start', models.DateField(help_text="Day is not important. Select 1st if you don't know the exact start day.", verbose_name='start')),
                ('end', models.DateField(blank=True, help_text="Leave empty if you are currently working here. Day is not important. Select 1st if you don't know the exact end day.", null=True, verbose_name='end')),
                ('location', models.CharField(max_length=100, verbose_name='location')),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'verbose_name': 'Internship',
                'verbose_name_plural': 'Internships',
                'default_related_name': 'internships',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('label', models.CharField(max_length=100, verbose_name='label')),
                ('level', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='level')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('type', models.CharField(choices=[('linkedin', 'LinkedIn'), ('github', 'GitHub'), ('website', 'Website')], max_length=10, verbose_name='type')),
                ('label', models.CharField(max_length=100, verbose_name='label')),
                ('url', models.URLField(verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('first_left_segment', models.CharField(choices=[('contact', 'Contact'), ('links', 'Links'), ('skills', 'Skills'), ('languages', 'Languages'), ('internship', 'Internship'), ('education', 'Education')], default='contact', max_length=20, verbose_name='first segment in left column')),
                ('second_left_segment', models.CharField(choices=[('contact', 'Contact'), ('links', 'Links'), ('skills', 'Skills'), ('languages', 'Languages'), ('internship', 'Internship'), ('education', 'Education')], default='links', max_length=20, verbose_name='second segment in left column')),
                ('third_left_segment', models.CharField(choices=[('contact', 'Contact'), ('links', 'Links'), ('skills', 'Skills'), ('languages', 'Languages'), ('internship', 'Internship'), ('education', 'Education')], default='skills', max_length=20, verbose_name='third segment in left column')),
                ('fourth_left_segment', models.CharField(choices=[('contact', 'Contact'), ('links', 'Links'), ('skills', 'Skills'), ('languages', 'Languages'), ('internship', 'Internship'), ('education', 'Education')], default='languages', max_length=20, verbose_name='fourth segment in left column')),
                ('fifth_left_segment', models.CharField(choices=[('contact', 'Contact'), ('links', 'Links'), ('skills', 'Skills'), ('languages', 'Languages'), ('internship', 'Internship'), ('education', 'Education')], default='internship', max_length=20, verbose_name='fifth segment in left column')),
                ('sixth_left_segment', models.CharField(choices=[('contact', 'Contact'), ('links', 'Links'), ('skills', 'Skills'), ('languages', 'Languages'), ('internship', 'Internship'), ('education', 'Education')], default='education', max_length=20, verbose_name='sixth segment in left column')),
                ('is_published', models.BooleanField(default=False, verbose_name='is published')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('filename', models.CharField(max_length=100, verbose_name='filename')),
                ('page_count', models.PositiveSmallIntegerField(default=1, help_text='If the content of your Portfolio does not fit on one page, the content will be automatically split into multiple pages. Set the expected number of pages here to apply the first page styling across all pages.', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)], verbose_name='page count')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='portfolio/images/', validators=[apps.common.validators.MaxFileSizeValidator(100)], verbose_name='avatar')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
                ('role', models.CharField(max_length=100, verbose_name='role')),
                ('email', models.EmailField(max_length=100, verbose_name='email')),
                ('phone', models.CharField(max_length=20, verbose_name='phone')),
                ('address_label', models.CharField(max_length=100, verbose_name='address label')),
                ('address_link', models.URLField(max_length=1000, verbose_name='address link')),
                ('about_me', models.TextField(blank=True, null=True, verbose_name='about me')),
                ('first_right_segment', models.CharField(choices=[('about_me', 'About Me'), ('employment', 'Employment'), ('projects', 'Projects')], default='about_me', max_length=20, verbose_name='first segment in right column')),
                ('second_right_segment', models.CharField(choices=[('about_me', 'About Me'), ('employment', 'Employment'), ('projects', 'Projects')], default='employment', max_length=20, verbose_name='second segment in right column')),
                ('third_right_segment', models.CharField(choices=[('about_me', 'About Me'), ('employment', 'Employment'), ('projects', 'Projects')], default='projects', max_length=20, verbose_name='third segment in right column')),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolios',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('role', models.CharField(max_length=100, verbose_name='role')),
                ('start', models.DateField(help_text="Day is not important. Select 1st if you don't know the exact start day.", verbose_name='start')),
                ('end', models.DateField(blank=True, help_text="Leave empty if you are currently working on this project. Day is not important. Select 1st if you don't know the exact end day.", null=True, verbose_name='end')),
                ('technologies', models.CharField(max_length=255, verbose_name='technologies')),
                ('description', models.TextField(default='', verbose_name='description')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('label', models.CharField(max_length=100, verbose_name='label')),
                ('level', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='level')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
    ]
