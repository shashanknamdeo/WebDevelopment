
# HttpResponse is used to
# pass the information
# back to view
import sys
sys.path.append(r'D:\NotebookShareAsus\Material\Python\PythonLibrary\Postgres')

from django.http import HttpResponse
from django.shortcuts import render, redirect
# from .forms import login
from LibPostgres import fetchPostgresDatabase
from hdfcbankwebsite.models import transactions



# Defining a function which
# will receive request and
# perform task depending
# upon function definition

 
# Create your views here.
# def hello_geeks(request):
#     if request.method == 'POST':
#         fm = login(request.POST)
#         print(fm)
#         # logic of view will be implemented here
#         return render(request,'home.html',{'form':fm})

def verifyUser(customer_id, password):
    dict1 = {'customerid':customer_id}
    df1 =  fetchPostgresDatabase(database='hdfcbank', table_name='idsandpasswords', primary_key_dict=dict1, verbose=1)
    index = df1.index[df1['customerid']==customer_id].tolist()
    print(index)
    if len(index)!=0:
        real_passward = df1._get_value(index[0], 'password')
        print(real_passward)
        if real_passward == password:
            return True
        else:
            return False



def login(request):
    if request.method == 'GET':
        return render(request,'loginpage.html',)
    # 
    elif request.method == 'POST':
        info_dict = dict(request.POST)
        print('UserID:', request.POST.get('UserID'))
        customer_id_list = info_dict['UserID']
        password_list = info_dict['Password']
        if (customer_id_list[0] != '') and (password_list[0] != ''):
            customer_id = int(customer_id_list[0])
            password = password_list[0]
            print('customer_id:', customer_id)
            print('password:', password)
            if verifyUser(customer_id=customer_id, password=password):
                # return render(request,'homepage.html',)
                return redirect('/home')
            else:
                return render(request,'loginpageerror.html',)
        #
        else :
            return render(request,'loginpage.html',)


def home(request):
    if request.method == 'GET':
        return render(request,'homepage.html',)
    # if request.method == 'POST':
    #     print('grdfv')


def showdata(request):
    results = transactions.objects.all()
    print('data',results)
    return render(request,'homepage.html',{"data":results})