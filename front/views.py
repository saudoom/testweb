from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from .models import S_achievement,en_word
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
'''
class ToLoginMixin(UserPassesTestMixin):
    def test_func(self):
        user=self.request.user
        return user!=None
    def handle_no_permission(self):
        return redirect('login')
'''
class Log1(TemplateView):
    template_name='front/log1.html'
class Log2(TemplateView):
    template_name='front/log2.html'
class Log3(TemplateView):
    template_name='front/log3.html'
class Pfront(TemplateView):
    template_name='front/pfront.html'
@login_required
def Plist(request):
    object_list=S_achievement.objects.all()
    return render(request,'front/plist.html',{'object_list':object_list})
class Pcreate(LoginRequiredMixin,CreateView):
    template_name='front/pcreate.html'
    model=S_achievement
    fields=('title','content','picture')
    success_url=reverse_lazy('plist')
@login_required
def Pdetail(request,pk):
    object=S_achievement.objects.get(pk=pk)
    return render(request,'front/pdetail.html',{'object':object})

class Pdelete(LoginRequiredMixin,DeleteView):
    template_name='front/pdelete.html'
    model=S_achievement
    success_url=reverse_lazy('plist')
class Pupdate(LoginRequiredMixin,UpdateView):
    template_name='front/pupdate.html'
    model=S_achievement
    fields=('title','content','picture')
    success_url=reverse_lazy('plist')
def loginview(request):
    if request.method=='POST':
        username_data=request.POST['username_data']
        password_data=request.POST['password_data']
        user=authenticate(request,username=username_data,password=password_data)
        if user is not None:
            login(request,user)
            return redirect('plist')
        else:
            return redirect('login')
    return render(request,'front/login.html')
def logoutview(request):
    logout(request)
    return redirect('login')


class Encreate(CreateView):
    template_name='front/encreate.html'
    model=en_word
    fields=('spell','rank')
    success_url=reverse_lazy('plist')
