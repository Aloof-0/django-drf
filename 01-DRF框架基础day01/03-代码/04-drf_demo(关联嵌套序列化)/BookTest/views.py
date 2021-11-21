
from django.views import View
from django.http import JsonResponse
import json
from .models import *

# 针对BookInfo模型类数据，完整增删改查5大类业务

# (1)、获取列表数据(多本书)
# 请求方式：GET
# 请求路径：/books/
# 请求参数：无
# 响应参数：json格式  --> 约定，响应参数的key名称，和模型类属性名保持一致。
# [
#     {
#       "btitle": 书名，
#       "bpub_date": 出版日期
#       ........
#     },
#     {}
# ]

# (2)、新建单一本书
# 请求方式：POST
# 请求路径：/books/
# 请求参数：json格式
# {
#     'btitle': 书名,
#     'bpub_date': 出版日期,
#     # .....
# }
# 响应参数：json格式 --> 新建数据返回


class BooksView(View):

    # (1)、获取列表数据(多本书)
    def get(self, request):

        # 1、读取模型类对象数据
        books = BookInfo.objects.all()

        # 2、构建响应参数
        book_list = []
        for book in books:
            book_list.append({
                'btitle': book.btitle,
                'bpub_date': book.bpub_date
                # .....
            })

        # 3、构建json响应
        return JsonResponse(book_list, safe=False)

    # (2)、新建单一本书
    def post(self, request):
        # 1、提取参数
        data = json.loads(request.body.decode())
        # 2、校验参数
        # 2.1、必要校验
        btitle = data.get('btitle')
        bpub_date = data.get('bpub_date')
        if not all([btitle,bpub_date]):
            return JsonResponse({
                'code': 400, # 小组自行约定的
                'errmsg': '缺少必传数据'
            }, status=400)
        # 2.2、约束校验
        if len(btitle) > 20:
            return JsonResponse({
                'code': 400,  # 小组自行约定的
                'errmsg': 'btitle校验错误'
            }, status=400)
        # 其他校验，略.....

        # 3、业务数据处理——新建模型类对象保存数据库
        book = BookInfo.objects.create(**data)

        # 4、构建响应
        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date
            # .....
        }, status=201)



# (3)、获取一本书
# (4)、更新一本书
# (5)、删除一本书