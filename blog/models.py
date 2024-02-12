from django.db import models
# django.contrib.auth 是 django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Post(models.Model):
    # 文章标题
    title = models.CharField('标题',max_length=70)

    # 文章正文，我们使用了 TextField。
    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    body = models.TextField('正文')

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField('创建时间',default=timezone.now)
    modified_time = models.DateTimeField('修改时间')

    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField('摘要',max_length=200, blank=True)
    category = models.ForeignKey(Category,verbose_name='分类',on_delete=models.CASCADE) #文章和分类是一对多关系
    tags = models.ManyToManyField(Tag, verbose_name='标签',blank=True) #文章和标签是多对多关系
    author = models.ForeignKey(User, verbose_name='作者',on_delete=models.CASCADE)

    def get_absolute_url(self):  #为了得到带id编号的文件链接,pk是主键也是id
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
