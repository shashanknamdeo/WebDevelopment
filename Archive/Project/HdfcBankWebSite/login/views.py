from django.shortcuts import render
from django.http import HttpResponse


def index(request, name='Shirish'):
    return HttpResponse('<form methord="post"> name : <input type="text" name="name",, value=%s> <button type="submit">submit</button> </form>' % name)
    # return HttpResponse('<input type="text" id="UserID" name="UserID", value=%s>' % name)
    #return HttpResponse('<label id="UserIDla" >Customer ID/ User ID</label><input type="text" id="UserID" name="UserID"><label for="Password">Password/ IPIN</label><input type="text" id="Password" name="Password"><p style="color:skyblue;">Forgot Password / IPIN</p><p>IPIN (Password) is case sensitive</p><input type="submit" value="Submit"> </form>')
    # return render(request,'views.py')

# def register(request):
#     username = request.POST['name']
#     print(username)

# register(request)

# def home(requests):
#     data = request.POST.get('name')
#     print('sg')
#     return render(request,'views.py')

# from django.http import HttpResponseRedirect
# from django.shortcuts import render

# from .forms import NameForm

# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, 'name.html', {'form': form})
