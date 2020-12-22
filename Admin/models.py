from django.db import models


# Create your models here.
class Users(models.Model):
    """
    用户表 users
    uid	             int(10)	    主键,非负,自增	user表主键
    name	         varchar(32)	唯一	            用户名称
    password	     varchar(32)	可为空	        用户密码
    mail	         varchar(200)	唯一	            用户的邮箱
    screenName	     varchar(32)	可为空	        用户显示的名称
    created	         int(10)	    非负,可为空	    用户注册时的GMT unix时间戳
    activated	     int(10)	    非负,可为空	    最后活动时间
    logged	         int(10)	    非负,可为空	    上次登录最后活跃时间
    group	         varchar(16)	N/A	            用户组
    authCode	     varchar(40)	可为空	        用户登录验证码
    """
    uid = models.AutoField(primary_key=True)


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
    pass


class Metas(models.Model):
    """
    文章分类 metas
    mid	        int(10)	        主键,非负	项目主键
    name	    varchar(200)	可为空	    名称
    description	varchar(200)	可为空	    选项描述
    """
    pass


class Relationships(models.Model):
    """
    分类与文章对应表 relationships
    cid	int(10)	主键,非负	内容主键
    mid	int(10)	主键,非负	项目主键
    """
    pass


class Comments(models.Model):
    """
    评论 comments
    coid	    int(10)	        主键,非负,自增	comment表主键
    cid	        int(10)	        索引,非负	    post表主键,关联字段
    created	    int(10)	        非负,可为空	    评论生成时的GMT unix时间戳
    author	    varchar(200)	可为空	        评论作者
    authorId	int(10)	        非负,可为空	    评论所属用户id
    ownerId	    int(10)	        非负,可为空	    评论所属内容作者id
    mail	    varchar(200)	可为空	        评论者邮件
    url	        varchar(200)	可为空	        评论者网址
    ip	        varchar(64)	    可为空	        评论者ip地址
    agent	    varchar(200)	可为空	        评论者客户端
    text	    text	        可为空	        评论文字
    type	    varchar(16)	    可为空	        评论类型
    status	    varchar(16)	    可为空	        评论状态
    parent	    int(10)	        可为空	        父级评论
    """
    pass


class Options(models.Model):
    """
    设置 options

    """
    pass
