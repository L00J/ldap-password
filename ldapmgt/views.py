from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views import View
from . import LDAPTool


def index(request):
    template_name = 'index.html'

    if request.method == 'POST':  # 当提交表单时

        # 判断是否传参
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('oldpassword')
            newpassword = request.POST.get('newpassword')
            try:
                ldap_obj = LDAPTool.LDAP()
                if ldap_obj:
                    res = ldap_obj.ldap_update_pass(username, password, newpassword)
                    if "success" in res:
                        return HttpResponse("%s:你的ldap密码修改为[%s]" % (username,newpassword))
                    else:
                        return HttpResponse("密码修改失败")
                    #     return HttpResponse(res)

            except Exception as e:
                return HttpResponse("连接异常:%s" % e)




    # 业务逻辑代码
    return render(request, template_name, {"name": "", "hobby": ["reading", "blog"]})
