# Generated by Django 2.1.3 on 2018-11-05 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=32, verbose_name='日志标题')),
                ('b_body', models.TextField(verbose_name='日志内容')),
                ('b_time', models.DateTimeField(verbose_name='日志时间')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=32, verbose_name='文章类型')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='b_to_t',
            field=models.ForeignKey(on_delete=None, to='web.Title'),
        ),
    ]