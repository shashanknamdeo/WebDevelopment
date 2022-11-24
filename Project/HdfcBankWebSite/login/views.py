from django.shortcuts import render
from django.http import HttpResponse


def index(request, name='Shirish'):
    return HttpResponse('<form methord="post"> name : <input type="text" name="name",, value=%s> <button type="submit">submit</button> </form>' % name)
    # return HttpResponse('<input type="text" id="UserID" name="UserID", value=%s>' % name)
    #return HttpResponse('<label id="UserIDla" >Customer ID/ User ID</label><input type="text" id="UserID" name="UserID"><label for="Password">Password/ IPIN</label><input type="text" id="Password" name="Password"><p style="color:skyblue;">Forgot Password / IPIN</p><p>IPIN (Password) is case sensitive</p><input type="submit" value="Submit"> </form>')

def home(requests):
    data = request.POST.get('name')
    print(data)
    return render(request,'views.py')
