from django.shortcuts import reverse,redirect


#新增一个对象，用于模板提交数据

def runoob(request):
    return redirect(reverse,"joke01:context")