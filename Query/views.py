from django.shortcuts import render
from django.http import HttpResponse
import pyodbc

db =pyodbc.connect('DRIVER={SQL Server}; SERVER=localhost; DATABASE=JY;')



def welcome(request):
    context = {
        'msg':'欢迎来到图书借阅数据库系统JY'
    }
    return render(request, 'Query/welcome.html', context)

def insert(request):
    cursor =db.cursor()
    cursor.execute('select * from book')
    book_list = cursor.fetchall()
    cursor.close()  # 关闭Cursor对象
    context = {
        'params': {'书号','书名','ISBN','作者','出版社','借阅次数','价格'},
        'book_list': book_list,
    }
    return render(request, 'Query/insert.html', context)

def execInsert(request):
    cursor =db.cursor()
    sql = "insert into book values (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(sql, (request.POST.get('book_id'), request.POST.get('book_name'), request.POST.get('book_isbn'), request.POST.get('book_author'), request.POST.get('book_publisher'), request.POST.get('interview_times'), request.POST.get('book_price')))
    cursor.commit()
    context = {
        'inserted': request.POST.get('book_id'),
    }
    cursor.close()
    return render(request, 'Query/insertResult.html', context)

def delete(request):
    cursor =db.cursor()
    cursor.execute('select * from book')
    book_list = cursor.fetchall()
    cursor.close()  # 关闭Cursor对象
    context = {
        'book_list': book_list,
    }
    return render(request, 'Query/delete.html', context)

def execDelete(request):
    cursor =db.cursor()
    deleted = []
    for selected in request.POST:
        cursor.execute("delete from book where book_id = ?", (selected))
        deleted.append(selected)
    cursor.commit()
    if deleted:
        deleted.pop(len(deleted)-1)
    context = {
        'deleted': deleted,
    }
    cursor.close()
    return render(request, 'Query/deleteResult.html', context)

def select(request):
    cursor =db.cursor()
    cursor.execute('select * from book')
    book_list = cursor.fetchall()
    cursor.close()  # 关闭Cursor对象
    context = {
        'book_list': book_list,
    }
    return render(request, 'Query/select.html', context)

def update(request):
    cursor =db.cursor()
    cursor.execute('select * from book')
    book_list = cursor.fetchall()
    cursor.close()  # 关闭Cursor对象
    context = {
        'book_list': book_list,
    }
    return render(request, 'Query/update.html', context)

def execUpdate(request):
    cursor =db.cursor()
    updated = []
    for selected in request.POST:
        cursor.execute("update book set interview_times = ? where book_id = ?", (request.POST.get('newValue'), selected))
        updated.append(selected)
    cursor.commit()
    if updated:
        updated.pop(len(updated)-1)
        updated.pop(len(updated)-1)
    context = {
        'updated': updated,
    }
    cursor.close()
    return render(request, 'Query/updateResult.html', context)

def exitJY(request):
    db.close()
    return HttpResponse("成功退出系统！")