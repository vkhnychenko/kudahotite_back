# Generated by Django 3.0.8 on 2020-07-20 04:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_itemsslider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Материал')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материалы',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Размер')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры',
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Тематика')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Тематика',
                'verbose_name_plural': 'Тематики',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Тэги')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Тэги',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.AlterModelOptions(
            name='itemsslider',
            options={'verbose_name': 'Объекты для слайдера', 'verbose_name_plural': 'Объекты для слайдера'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='products',
            name='description',
        ),
        migrations.AddField(
            model_name='products',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата добавления товара'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=100, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='products',
            name='material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Material', verbose_name='Материал'),
        ),
        migrations.AddField(
            model_name='products',
            name='size',
            field=models.ManyToManyField(to='catalog.Size', verbose_name='Размер'),
        ),
        migrations.AddField(
            model_name='products',
            name='subjects',
            field=models.ManyToManyField(to='catalog.Subjects', verbose_name='Тематика'),
        ),
        migrations.AddField(
            model_name='products',
            name='tags',
            field=models.ManyToManyField(to='catalog.Tags', verbose_name='Тэги'),
        ),
    ]
