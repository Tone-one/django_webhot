from django.db import models


# Create your models here.


# 测试用例表单
class TestCase(models.Model):
    """
    模块:case_modules
    用例描述:case_description
    前提条件:case_precondition
    操作步骤:operating_steps
    预期结果:expected_result
    测试结果:test_result
    备注: Remarks
    """

    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    case_modules = models.TextField(verbose_name="用例模块")
    case_description = models.TextField(verbose_name="用例描述")
    case_precondition = models.TextField(verbose_name="前提条件")
    operating_steps = models.TextField(verbose_name="操作步骤")
    expected_result = models.TextField(verbose_name="预期结果")
    test_result = models.TextField(verbose_name="测试结果")
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    remarks = models.TextField(blank=True, verbose_name="备注")

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。


    def __unicode__(self):
        return self.__str__()

    # 修改模块的名字为中文-通用
    class Meta:
        verbose_name = "测试用例"
        verbose_name_plural = '测试用例'


class Test(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.__str__()

    # 修改模块的名字为中文-通用
    class Meta:
        verbose_name = "测试用例"
        verbose_name_plural = '测试用例'

class Contact(models.Model):

    name = models.CharField(max_length=200, verbose_name="名字")
    age = models.IntegerField(default=0, verbose_name="年龄")
    email = models.EmailField(verbose_name="邮件")

    def __unicode__(self):
        return self.__str__()

    # 修改模块的名字为中文
    class Meta:
        verbose_name = "联系人"
        verbose_name_plural = '联系人'


class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.__str__()

    # 修改模块的名字为中文-通用
    class Meta:
        verbose_name = "测试用例"
        verbose_name_plural = '测试用例'