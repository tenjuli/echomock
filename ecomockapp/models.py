from django.db import models
from django.utils import timezone

# Create your models here.

class Author (models.Model):
    full_name = models.CharField('氏名', max_length=50)
    mail_address = models.CharField('メールアドレス', max_length=50)
    organization = models.CharField('所属組織', max_length=50)
    registration_date = models.DateTimeField('登録日', default=timezone.now)
    
    def __str__(self):
        return self.full_name

class Plugin (models.Model):
    name = models.CharField('名称', max_length=50)
    summary = models.CharField('概要', max_length=210)
    description = models.CharField('詳細説明', max_length=990)
    plugin = models.FileField('プラグインモジュール', upload_to='plugins/')
    target = models.CharField('操作対象', max_length=210)
    release_date = models.DateTimeField('公開日', default=timezone.now)
    # author = models.ForeignKey('作者', Author, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Scenario (models.Model):
    name = models.CharField('名称', max_length=50)
    summary = models.CharField('概要', max_length=210)
    description = models.CharField('詳細説明', max_length=990)
    scenario = models.FileField('シナリオモジュール', upload_to='scenarios/')
    release_date = models.DateTimeField('公開日', default=timezone.now)
    # require = models.ForeignKey('必須プラグイン', Plugin,
    require = models.ForeignKey(Plugin,
                                on_delete=models.PROTECT)
    # author = models.ForeignKey('作者', Author, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

# Ends here.
