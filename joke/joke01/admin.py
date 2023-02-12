from django.contrib import admin
from django.utils.html import format_html

from joke01.models import Test, Contact, Tag, TestCase
from django.db import models
import time

# Register your models here.
@admin.register(Contact) # 模型Contact,继承下方ContactAdmin
class ContactAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     ['Main', {
    #         'fields': ('age', 'name', 'email'),
    #     }],
    #     # ['Advance', {
    #     #     'classes': ('collapse',),  # 隐藏
    #     #     'fields': ('age',),
    #     # }]
    # )
    list_display = ['age', 'name', 'email']


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    """
    模块:case_modules
    用例描述:case_description
    前提条件:case_precondition
    操作步骤:operating_steps
    预期结果:expected_result
    测试结果:test_result
    备注: remarks
    """
    list_display = ['case_modules', 'case_description', 'case_precondition',
                    'operating_steps', 'expected_result', 'test_result',
                    'remarks','return_href']
    list_filter = ['case_modules','case_description']  # 过滤器
    search_fields = ['test_result']     # 根据结果进行搜索

    # def creat_time_admin(self, obj):
    #     time_Array = time.localtime(obj.created_time)
    #     styletime = time.struct_time("%y-%m-%d %H:%M:%S", time_Array)
    #     return styletime

    def return_href(self,obj):
        # obj 表示模型的TestCase类
        return format_html('<a href={}>跳转</a>', 'https://www.baidu.com')


@admin.register(Tag)
class TestCaseAdmin(admin.ModelAdmin):
    pass


@admin.register(Test)
class TestCaseAdmin(admin.ModelAdmin):
    pass




#
#
# class Test01(admin.TabularInline):
#     model = Post
#     extra = 3
#
#
# class Test02(admin.ModelAdmin):
#     list_display = ['id', 'a', 'b']     # 显示自动，可以点击进行排序
#     list_filter = ['c']     # 过滤自动，过滤框会出现在右侧
#     search_fields = ["搜索"]      # 搜索字段，搜索框会出现在上侧
#     list_per_page = 10  # 分页，分页框会出现在下侧
#
#     fieldsets = [   # 属性页分组
#         ('base', {'fields':['btitle']}),
#         ('super', {'fields':['bpub_date']})  # fields：属性的先后顺序
#     ]
#     inlines = [Test01]
