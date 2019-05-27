from django.shortcuts import render, get_object_or_404,redirect
from .models import Event,Comment
from .forms import EventForm,CommentForm,LoginForm

# Create your views here.

def index(request):
    events=Event.objects.all
    context={
        'events':events
    }
    return render(request,'eapp/index.html',context)

def details(request, event_id):
    event=get_object_or_404(Event, pk=event_id)
    return render(request,'eapp/details.html',{'event':event})


def add_Event(request):
    formEvent=EventForm(request.POST or None, request.FILES or None)
    if formEvent.is_valid():
        event=formEvent.save(commit=False)
        event.save()
        return render(request,'eapp/details.html',{'event':event})
    return render(request,'eapp/event_adding.html',{'formEvent':formEvent})

def comment(request,event_id):
    event=get_object_or_404(Event, pk=event_id)
    formComment=CommentForm(request.POST or None, request.FILES or None)
    if formComment.is_valid():
        user_comment=formComment.save(commit=False)
        user_comment.event_name=event
        user_comment.save()
        return render(request,'eapp/details.html',{'event':event})
    return render(request,'eapp/commenting.html',{'formComment':formComment})

def login_edit(request,event_id):
    event_name=get_object_or_404(Event, pk=event_id)

    formEvent=EventForm(request.POST or None, request.FILES or None, instance=event_name)
    formLogin=LoginForm(request.POST or None)
    if formLogin.is_valid():
        name=formLogin.cleaned_data[
            'event_creator'
        ]
        password=formLogin.cleaned_data[
            'event_password'
        ]
        if name==event_name.event_creator and password==event_name.event_password:
            if formEvent.is_valid():
                update_details=formEvent.save(commit=False)
                update_details.save()
                return redirect('eapp:index')
            return render(request,'eapp/event_adding.html',{'formEvent':formEvent})

        else:
            message = {'message': ' Invalid Credentials ', 'formLogin': formLogin}
            return render(request, 'eapp/login.html', message)

    return render(request,'eapp/login.html',{'formLogin':formLogin})


def delete(request,event_id):
    event_name=get_object_or_404(Event, pk=event_id)
    formLogin=LoginForm(request.POST or None)
    if formLogin.is_valid():
        name=formLogin.cleaned_data[
            'event_creator'
        ]
        password=formLogin.cleaned_data[
            'event_password'
        ]
        if name==event_name.event_creator and password==event_name.event_password:
            event_name.delete()
            return redirect('eapp:index')
    return render(request,'eapp/login.html',{'formLogin':formLogin})
