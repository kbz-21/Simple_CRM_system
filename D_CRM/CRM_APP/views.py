from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from CRM_APP.forms import SignUpForm, AddRecordForm 
from CRM_APP.models import Record
from CRM_APP.forms import LoginForm
from tablib import Dataset
from CRM_APP.resources import RecordResource
from django.utils.datastructures import MultiValueDictKeyError
# from .filters import FilterRecord
import datetime
from django.http import HttpResponse
import xlwt

def landing_page_view(request):
    return render(request, 'CRM_APP/landing.html')

def login_user(request):
    if request.method == 'GET':
        
        if request.user.is_authenticated:
            return redirect('home')
        form = LoginForm()
        return render(request,'CRM_APP/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome!')
                return redirect('home')
        
    messages.error(request,f'Invalid username or password')
    return render(request, 'CRM_APP/login.html', context={'form': form})


@login_required
def home(request):
    records = Record.objects.all()
    return render(request, 'CRM_APP/home.html', {'records': records})
    

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('login')

def register_user(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! welcome!")
            return redirect('home')

    else:
        form = SignUpForm()
        return render(request, 'CRM_APP/register.html' , {'form':form})
    return render(request, 'CRM_APP/register.html' , {'form':form})

@login_required
def customer_record(request,pk):
    if request.user.is_authenticated:
        # Look up Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'CRM_APP/record.html' , {'customer_record':customer_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page..")
        return redirect('home')

@login_required    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect ('home')

        return render(request, 'CRM_APP/add_record.html' , {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect ('home')

@login_required   
def update_request(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect ('home')
        return render(request, 'CRM_APP/update_record.html' , {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect ('home')
    


@login_required
def importExcel(request):
    if request.method == 'POST':
        record_resource = RecordResource()
        dataset = Dataset()
        
        try:
            new_record = request.FILES.get('my_file')
            imported_data = dataset.load(new_record.read(), format = 'xlsx')
        
            for data in imported_data:
                record = Record(
                    field1=data[0],
                    field2=data[1],
                    field3=data[2],
                    field4=data[3],
                    field5=data[4],
                    field6=data[5],
                    field7=data[6],
                    field8=data[7],
                    field9=data[8]
            )
                record.save()
        
            return render(request, 'home.html')
        except MultiValueDictKeyError:
            # Handle the case when the 'my_file' key is not found in request.FILES
            return render(request, 'import.html', {'error_message': 'No file selected.'})

    return render(request, 'import.html')



@login_required
def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Record' + \
        str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Templates')
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['student_id', 'first_name', 'last_name', 'Phone', 'Email', 'University', 'Department', 'Block_Dorm', 'Acadamics']

    for col_num, column_title in enumerate(columns):
        ws.write(row_num, col_num, column_title, font_style)

    font_style = xlwt.XFStyle()
    rows = Record.objects.filter().values_list('student_id','first_name','last_name','Phone','Email','University','Department','Block_Dorm','Acadamics')

    for row in rows:
        row_num += 1
        for col_num, data in enumerate(row):
            ws.write(row_num, col_num, str(data), font_style)

    wb.save(response)

    return response

# def searchRecord(request):
    # students = Record.objects.all()
    # filters = FilterRecord(request.GET, queryset=students)
    # context = {'filters':filters}
    # return render(request, 'student/searchStudent.html',context)








     



