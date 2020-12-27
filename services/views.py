from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Gigs
from .forms import GigsForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import CustomerSignUpForm, EmployeeSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

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
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})

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
