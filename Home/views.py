from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import psycopg2
import pandas



index_list = ['id', 'password', 'last login', 'is superuser', 'username', 'first name', 'last name', 'email', 'is staff', 'is active', 'data joined']
def Fetch_Data(request, database = 'Home', table = 'Home_task'):
    '''
    :param database: This parameter determines which database is going to be look in for the information
    :param table: This parameter determines which table is going to be fetched
    :return: this function returns a list that contains the information that was fetched
    '''
    conn = psycopg2.connect(
        database = database, user = 'postgres', password = ';&38bfkGeb', host = 'localhost', port = '5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM public."{table}"')

    result = cursor.fetchall()
    List_Of_Tasks = []
    for task in result:
        List_Of_Tasks.append(list(task))

    List_Of_Tasks.sort()

    conn.commit()
    conn.close()
    return List_Of_Tasks


def Fetch_Spesific_Colums_Of_Data(request, colums, database = 'Home', table = 'Home_task'):
    '''
    :param database: This parameter determines which database is going to be look in for the information
    :param table: This parameter determines which table is going to be fetched
    :param colums: list of the colums names that you want to extract
    :return: this function returns a list that contains the information that was fetched
    '''
    conn = psycopg2.connect(
        database = database, user = 'postgres', password = ';&38bfkGeb', host = 'localhost', port = '5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f'SELECT {colums} FROM public."{table}"')

    result = cursor.fetchall()
    List_Of_Tasks = []
    for task in result:
        List_Of_Tasks.append(list(task))

    List_Of_Tasks.sort()

    conn.commit()
    conn.close()
    return List_Of_Tasks


def Refresh_User_Data(request):
    Big_Data = Fetch_Data(request, database='Home', table='auth_user')

    Dict = dict()

    for index, one_list in enumerate(Big_Data):
        Dict = {f'{index_list[index]}': one_list}


    return Dict

def Home_Page(request):
    print("testtttttttttttttttttttttt", Refresh_User_Data(request))
    Dict = dict()

    data = Fetch_Data(request)
    return render(request, 'Home.html', {'data': data})

def Project_Register_Page(request):
    return render(request, 'Project_Register.html', {})


def Suggestions_Page(request):
    return render(request, 'Suggestions.html', {})









#
# from django_dyn_dt.datatb import DataTB
#
#
# def dyn_datatb(request):
#     context = {}
#
#     ddt = DataTB(model_class_path="home.models.Product")  # Link Dynamic view to a Model (full path)
#     context['data_table1'] = ddt.render()  # Render() returns the dynamic widget
#
#     return render(request, 'pages/dyn-datatb.html', context=context)


