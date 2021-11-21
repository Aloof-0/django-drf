
# render函数作用：传入模版和模版参数，用于渲染页面数据，并且构建响应返回
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import BookInfo
# Create your views here.


class BooksView(View):

    def get(self, request):
        # 1、提取参数
        # 2、校验参数
        # 3、业务数据处理 —— 通过模型类获取书本对象数据
        books = BookInfo.objects.all()

        # 4、构建模版参数
        # context = {
        #     'book_list': [
        #         {
        #             'id': 书本的id,
        #             'btitle': 书名,
        #             'bpub_date': 出版日期
        #         },
        #         # .....
        #     ]
        # }
        book_list = []
        for book in books:
            book_list.append({
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date
            })

        context = {
            'book_list': book_list
        }

        # 5、渲染完整的页面数据，构建响应返回 —— 前后端不分离
        # render函数作用：传入模版和模版参数，用于渲染页面数据，并且构建响应返回
        # response = render(request, 'index.html', context=context)
        # return response
        # 5、把模版参数(动态数据)，直接构建响应返回(json格式) —— 前后端分离
        return JsonResponse(context)