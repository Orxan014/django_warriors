from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Gigs
from .forms import GigsForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import CustomerSignUpForm, EmployeeSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
import json
import requests
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth.models import User
from datetime import datetime
from django.db import connection
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


def register(request):
    return render(request, 'register.html')


class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, '../templates/login.html',
                  context={'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')


def gig_index(request):
    gig_list = Gigs.objects.all()

    query = request.GET.get('q')
    if query:
        gig_list = gig_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()

    paginator = Paginator(gig_list, 5)  # Show 5 contacts per page

    page = request.GET.get('page')
    try:
        gigs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        gigs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        gigs = paginator.page(paginator.num_pages)

    return render(request, "post/index.html", {'gigs': gigs})


def gig_detail(request, slug):
    gig = get_object_or_404(Gigs, id=id)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.gig = gig
        comment.save()
        return HttpResponseRedirect(gig.get_absolute_url())

    context = {
        'gig': gig,
        'form': form
    }
    return render(request, "post/detail.html", context)


def gig_create(request):

    if not request.user.is_authenticated:
        raise Http404()

    form = GigsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        gig = form.save(commit=False)
        gig.user = request.user
        gig.save()
        messages.success(
            request, "Başarılı bir şekilde oluşturdunuz.", extra_tags='mesaj-basarili')
        return HttpResponseRedirect(gig.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, "post/form.html", context)


def gig_update(request, id):

    if not request.user.is_authenticated():
        raise Http404()

    gig = get_object_or_404(Gigs, id=id)
    form = GigsForm(request.POST or None, request.FILES or None, instance=gig)
    if form.is_valid():
        form.save()
        messages.success(request, "Başarılı bir şekilde güncellediniz.")
        return HttpResponseRedirect(gig.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, "post/form.html", context)


def gig_delete(request, id):

    if not request.user.is_authenticated():
        raise Http404()

    gig = get_object_or_404(Gigs, id=id)
    gig.delete()
    return redirect("services:index")


url = 'http://10.0.80.133:3000/oauth/getDetails'
#url = 'https://serene-wildwood-35121.herokuapp.com/oauth/changeUr/'
clientSecret = "445b354949599afbcc454441543297a9a827b477dd3eb78d1cdd478f1482b5da08f9b6c3496e650783927e03b20e716483d5b9085143467804a5c6d40933282f"


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'homepage.html')
    else:
        return HttpResponseRedirect(reverse('services:home'))


@csrf_exempt
def check_username(request):
    data = json.loads(request.body.decode('utf-8'))
    username = data['username']
    try:
        user = User.objects.get(username=username)
        if user:
            return HttpResponse('<b>Username must be unique.</b>')
    except User.DoesNotExist:
        return HttpResponse('')

@csrf_exempt
def check_email(request):
    data = json.loads(request.body.decode('utf-8'))
    email = data['email']
    try:
        if User.objects.get(email=email):
            return HttpResponse('<b>Email must be unique.</b>')
    except User.DoesNotExist:
        return HttpResponse('')


@csrf_exempt
def open_close_task(request):
    data = json.loads(request.body.decode('utf-8'))
    wt_id = data["wanted_task_id"]
    current_state = data["current"]
    task = Wanted_Task.objects.get(id=wt_id)
    task.isCompleted = not task.isCompleted
    task.save()
    return HttpResponse(str(task.isCompleted))


def send_simple_message(reciever, subject, text):
    print(">>", reciever)
    print(">>", subject)
    print(">>", text)
    fromaddr = "zekiyev014@gmail.com"
    toaddr = reciever
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    body = text
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "freelancingportal")
    text = msg.as_string()
    x = server.sendmail(fromaddr, toaddr, text)
    print(x, "sent mail")
    server.quit()
