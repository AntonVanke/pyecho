from django.db import models


# Create your models here.
class Users(models.Model):
    """
    用户表 users
    uid	             int(10)	    主键,非负,自增	user表主键
    username	     varchar(32)	唯一	            用户名称
    password	     varchar(32)	可为空	        用户密码
    email	         varchar(200)	唯一	            用户的邮箱
    screenName	     varchar(32)	可为空	        用户显示的名称
    created	         int(10)	    非负,可为空	    用户注册时间
    group	         varchar(16)	N/A	            用户组
    """
    uid = models.AutoField(primary_key=True, verbose_name='主键')
    username = models.CharField(max_length=32, verbose_name='用户名（英文）')
    password = models.CharField(max_length=32, verbose_name='用户密码')
    email = models.EmailField(max_length=200, verbose_name='用户邮箱', null=True)
    screenName = models.CharField(max_length=32, verbose_name='用户名', null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='用户注册时间')
    group = models.CharField(max_length=16, verbose_name='用户组', default='subscriber')


class Contents(models.Model):
    """
    文章 contents
    cid	            int(10)	        主键,非负,自增	文章id
    title	        varchar(200)	可为空	        内容标题
    created	        int(10)	        索引,非负,可为空	内容生成时的GMT unix时间戳
    modified	    int(10)	        非负,可为空	    内容更改时的GMT unix时间戳
    text	        text	        可为空	        内容文字
    authorId	    int(10)	        非负,可为空	    所属用户id
    status	        varchar(16)	    可为空	        内容状态
    """
    cid = models.AutoField(primary_key=True, verbose_name='文章主键')
    title = models.CharField(max_length=200, verbose_name='文章标题')
    created = models.DateTimeField(auto_now_add=True, verbose_name='文章写入时间')
    modified = models.DateTimeField(auto_now=True, verbose_name='文章修改时间')
    text = models.TextField(blank=True, null=True, verbose_name='文章内容')
    authorId = models.IntegerField()


class Metas(models.Model):
    """
    文章分类 metas
    mid	        int(10)	        主键,非负	分类主键
    name	    varchar(200)	可为空	    名称
    description	varchar(200)	可为空	    选项描述
    """
    mid = models.AutoField(primary_key=True, verbose_name='主键')
    name = models.CharField(max_length=200, verbose_name='分类标题')
    description = models.CharField(max_length=200, verbose_name='分类描述')


class Relationships(models.Model):
    """
    分类与文章对应表 relationships
    cid	int(10)	主键,非负	文章主键
    mid	int(10)	主键,非负	分类主键
    """
    cid = models.IntegerField(primary_key=True, verbose_name='文章主键')
    mid = models.IntegerField(primary_key=True, verbose_name='分类主键')


class Comments(models.Model):
    """
    评论 comments
    coid	    int(10)	        主键,非负,自增	comment表主键
    cid	        int(10)	        索引,非负	    post表主键,关联字段
    uid     	int(10)	        非负,可为空	    评论所属用户id
    created	    int(10)	        非负,可为空	    评论生成时的GMT unix时间戳
    ip	        varchar(64)	    可为空	        评论者ip地址
    agent	    varchar(200)	可为空	        评论者客户端
    text	    text	        可为空	        评论文字
    """
    coid = models.AutoField(primary_key=True, verbose_name='评论id')
    cid = models.IntegerField(primary_key=True, verbose_name='文章主键')
    uid = models.AutoField(primary_key=True, verbose_name='主键')
    created = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    text = models.TextField(blank=True, null=True, verbose_name='评论内容')


class Options(models.Model):
    """
    设置 options
    """
    pass
