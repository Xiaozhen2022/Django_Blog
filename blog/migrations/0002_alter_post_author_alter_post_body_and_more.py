# Generated by Django 4.2.9 on 2024-01-30 02:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="作者",
            ),
        ),
        migrations.AlterField(
            model_name="post", name="body", field=models.TextField(verbose_name="正文"),
        ),
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="blog.category",
                verbose_name="分类",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_time",
            field=models.DateTimeField(verbose_name="创建时间"),
        ),
        migrations.AlterField(
            model_name="post",
            name="excerpt",
            field=models.CharField(blank=True, max_length=200, verbose_name="摘要"),
        ),
        migrations.AlterField(
            model_name="post",
            name="modified_time",
            field=models.DateTimeField(verbose_name="修改时间"),
        ),
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(blank=True, to="blog.tag", verbose_name="标签"),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=70, verbose_name="标题"),
        ),
    ]
