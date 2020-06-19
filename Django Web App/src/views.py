from django.shortcuts import render, redirect
from .models import *
from django.db.models import Max, Min
import random

# Create your views here.
def index(request):
    if request.method == "POST":
        form = Issue_Form(request.POST)
        if form.is_valid():
            mode = form.cleaned_data['mode']
            roles = form.cleaned_data['roles']
            agents = Agent.objects.filter(is_available=True,roles__in=roles).distinct()
            max_id = agents.aggregate(max_id=Max("id"))['max_id']
            min_id = agents.aggregate(min_id=Min("id"))['min_id']
            pk = random.randint(min_id, max_id)

            if mode == "random":
                return render(request,'src/index.html',{
                    'form': Issue_Form(), 'agents': Agent.objects.get(pk=pk),'mode':mode, 'roles':roles
                }) 

            elif mode == "available":    
                return render(request,'src/index.html',{
                        'form': Issue_Form(), 'agents':agents, 'available':True,'mode':mode, 'roles':roles
                    })
            
            return render(request,'src/index.html',{
                        'form': Issue_Form(), 'agents':agents.earliest('available_since'),'mode':mode, 'roles':roles
                    })

        else:
            return redirect('src:index')

    return render(request,'src/index.html',{
        'form': Issue_Form()
    })

def view_agents(request):
    if request.method == "POST":
        form = Agent_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('src:agents')

    return render(request, 'src/agents.html',{
        'form':Agent_Form(), 'agents': Agent.objects.all()
    })


def edit_agent(request, id):
    agent = Agent.objects.get(pk=id)
    form = Agent_Form(instance=agent)

    if request.method == 'POST':
        update_form = Agent_Form(request.POST, instance=agent)
        if update_form.is_valid():
            update_form.save()
            return redirect('src:agents')
    
    return render(request,'src/edit_agent.html',{
        'form': form, 'agent':agent
    })

def del_agent(request, id):
    agent = Agent.objects.get(pk=id)
    agent.delete()
    return redirect('src:agents')