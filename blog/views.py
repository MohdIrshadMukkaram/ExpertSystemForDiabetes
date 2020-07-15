from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework import authentication, permissions
from django.utils import timezone
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import prescription_form
from .neural import initializing_fe
from  users.models import Profile
from django.http import JsonResponse


#/home/mohd/Environments/django_project/blog
res = 'nothing'
dosage = 'none'
p_fasting = 0
p_posting = 0
p_medicine_taken = 'not'
user = ''


def homepage(request):
    return render(request,"blog/homepage.html")

class DietView(LoginRequiredMixin,ListView):
    model = prescription_form
    template_name = 'blog/diet.html'  # <app>/<model>_<viewtype>.html
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        user = self.request.user
        context['user'] = user
        context['res'] = res
        context['dosage'] = dosage
        return context


class ResultView(LoginRequiredMixin,ListView):
    model = prescription_form
    template_name = 'blog/result.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'reports'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        user = self.request.user
        age = Profile.objects.filter(user=user).values_list('age', flat=True)[0]
        email = Profile.objects.filter(user=user).values_list('email', flat=True)[0]
        context['user'] = user
        context['age'] = age
        context['email'] = email
        context['res'] = res
        context['dosage'] = dosage
        return context
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return prescription_form.objects.filter(author=user).order_by('-date_posted')[0]

class ReportView(LoginRequiredMixin,ListView):
    model = prescription_form
    template_name = 'blog/user_reports.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'reports'
    #ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        user = self.request.user
        context['user'] = user
        return context
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return prescription_form.objects.filter(author=user).order_by('-date_posted')[:5]   



class PostCreateView(LoginRequiredMixin, CreateView):
    model = prescription_form
    template_name = 'blog/home.html'
    fields = ['fasting', 'posting','diabetic_exp','medicine_taken',]
    context_object_name = 'res'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['user'] = self.request.user
        global user
        user = self.request.user    
        try:
            global p_fasting,p_posting,p_medicine_taken
            p_fasting = prescription_form.objects.filter(author = user).order_by('-date_posted').values_list('fasting', flat=True)[0]
            p_posting = prescription_form.objects.filter(author = user).order_by('-date_posted').values_list('posting', flat=True)[0]
            p_medicine_taken = prescription_form.objects.filter(author = user).order_by('-date_posted').values_list('medicine_taken', flat=True)[0]
        except:
            p_fasting = 0
            p_posting = 0
        return context


    def form_valid(self, form):
        form.instance.author = self.request.user
        answer_1 = form.cleaned_data.get('fasting')
        answer_2 = form.cleaned_data.get('posting')
        global p_fasting,p_posting,p_medicine_taken
        answer_3 = p_fasting
        answer_4 = p_posting
        answer_5 = p_medicine_taken
        global dosage
        if(40 <= answer_1 <= 70 and 70 <= answer_2 <= 110):
            dosage = 'DosageLow' 
        elif(40 <= answer_1 <= 70 and 110 <= answer_2):
            dosage = 'Fasting' 
        elif(70 <= answer_1 <= 110 and 180 <= answer_2):
            dosage = 'Posting'               
        elif(110 <= answer_1 and 180 <= answer_2):
            dosage = 'DosageHigh'
        else:
            dosage = 'same'     
        global res
        res = initializing_fe(answer_1,answer_2,answer_3,answer_4,answer_5)
        return super().form_valid(form)

def bars(request):
    return render(request,'blog/charts.html',{'title':'Diabetes Bars'})




class ListUsers(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
   

    def get(self, request, format=None): 
        labels = ['Vist 1', 'Vist 2', 'Visit 3', 'Visit 4', 'Visit 5']
        user = User.objects.get(username=request.user.username)
        fasting_ranges = prescription_form.objects.filter(author = user).order_by('-date_posted').values_list('fasting', flat=True)[:5]
        posting_ranges = prescription_form.objects.filter(author = user).order_by('-date_posted').values_list('posting', flat=True)[:5]
        default_items = [40,50,40]   
        data = {
            "fasting": fasting_ranges,
            "posting": posting_ranges,
            "labels": labels,
            "default": posting_ranges,
        }
        return Response(data)   



def glycemic(request):
    return render(request,'blog/glycemic.html',{'title':'Glycemic Index'})






#class call_model(APIView):

 #   def get():
            # predict method used to get the prediction
  #          response = BlogConfig.inputs_to_network(1)
            
            # returning JSON response
   #         return JsonResponse(response)
