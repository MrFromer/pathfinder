
from urllib import request
from venv import create
from django.shortcuts import render, redirect
from .models import character
from .forms import CharacterForm
from django.views.decorators.csrf import csrf_exempt
import random
from django.shortcuts import get_list_or_404, get_object_or_404



#страница abc 
@csrf_exempt
def saveforms (request, id=None):
    
    form = CharacterForm(request.POST or None)
    context = {'id': None}   
    if request.method=="POST" and form.is_valid():
        #a = character.objects.get()
        a = form.save(commit=False)
        auto_correct(a) #передаёт значения из формы в функции автоподсчёта
        a.author = request.user
        a.save()
        context = {
        'id' : a.id,
        'form': form,
        }   
        print(a.id, 'АААААААААААААААААААААААААА')
        #if id==None:
            #redirect('edit')
        return redirect("saveforms")
        
    if context:
        return render(request,"main.html", context )
    else:
        return render(request,"main.html" )    

#основная страница
def index (request):
    return  render(request,"index.html",{})

#страница main
def main (request):
    return  render(request,"main.html",{})
#страница выбор действий
def page_choice (request):
    return render(request,"page_choice.html",{})

#выбор персонажа
def list(request):
    person = character.objects.filter( author = request.user)
    return render(request, 'list.html', {'person': person})

#изменение персонажа
def edit(request, id):
    character_edit = get_object_or_404(character, id=id)
    if character_edit.author != request.user:
        return redirect('index')
    form = CharacterForm(request.POST or None, instance=character_edit)
    if form.is_valid():
        form.save(commit=False)
        auto_correct(form.instance)
        form.save()
    character_edit = get_object_or_404(character, id=id)
    form = CharacterForm(instance=character_edit)
    context = {
        'id' : id,
        'form': form,
    }    
    return render(request, "main.html", context)
    
#изменение персонажа вторая страница
def edit_1_2(request, id):
    character_edit = get_object_or_404(character, id=id)
    if character_edit.author != request.user:
        return redirect('index')
    form = CharacterForm(request.POST or None, instance=character_edit)
    if form.is_valid():
        form.save(commit=False)
        auto_correct(form.instance)
        form.save()
    character_edit = get_object_or_404(character, id=id)
    form = CharacterForm(instance=character_edit)
    context = {
        'id' : id,
        'form': form,
    }    
    return render(request, "main_1_2.html", context)
#изменение персонажа третья страница
def edit_1_3(request, id):
    character_edit = get_object_or_404(character, id=id)
    if character_edit.author != request.user:
        return redirect('index')
    form = CharacterForm(request.POST or None, instance=character_edit)
    if form.is_valid():
        form.save(commit=False)
        auto_correct(form.instance)
        form.save()
    character_edit = get_object_or_404(character, id=id)
    form = CharacterForm(instance=character_edit)
    context = {
        'form': form,
    }    
    return render(request, "main_1_3.html", context)    

#о сайте
def about_site(request):
     return render(request,"about_site.html",{})   
       

 #Автоподсчёт
def auto_correct(a):
    #подсчёт модификатора характеристики таблица на странице 19 книги правил
    fields = {
    "srtength_ability_score": "srtength_ability_modifier",
    "dexterity_ability_score": "dexterity_ability_modifier",
    "constitution_ability_score": "constitution_ability_modifier",
    "intelligence_ability_score": "intelligence_ability_modifier",
    "wisdom_ability_score": "wisdom_ability_modifier", 
    "charisma_ability_score": "charisma_ability_modifier",}
    for field in fields:
        if getattr(a, field) == 1:
            setattr(a, fields[field], -5)
        elif getattr(a, field) == 2 or getattr(a, field) == 3:
            setattr(a, fields[field], -4)     
        elif getattr(a, field) == 4 or getattr(a, field) == 5:
            setattr(a, fields[field], -3)
        elif getattr(a, field) == 6 or getattr(a, field) == 7:
            setattr(a, fields[field], -2)  
        elif getattr(a, field) == 8 or getattr(a, field) == 9:
            setattr(a, fields[field], -1)
        elif getattr(a, field) == 10 or getattr(a, field) == 11:
            setattr(a, fields[field], 0)      
        elif getattr(a, field) == 12 or getattr(a, field) == 13:
            setattr(a, fields[field], 1)
        elif getattr(a, field) == 14 or getattr(a, field) == 15:
            setattr(a, fields[field], 2) 
        elif getattr(a, field) == 16 or getattr(a, field) == 17:
            setattr(a, fields[field], 3)   
        elif getattr(a, field) == 18 or getattr(a, field) == 19:
            setattr(a, fields[field], 4)  
        elif getattr(a, field) == 20 or getattr(a, field) == 21:
            setattr(a, fields[field], 5)   
        elif getattr(a, field) == 22 or getattr(a, field) == 23:
            setattr(a, fields[field], 6)    
        elif getattr(a, field) == 24 or getattr(a, field) == 25:
            setattr(a, fields[field], 7)  
        elif getattr(a, field) == 26 or getattr(a, field) == 27:
            setattr(a, fields[field], 8)
        elif getattr(a, field) == 28 or getattr(a, field) == 29:
            setattr(a, fields[field], 9)
        elif getattr(a, field) == 30 or getattr(a, field) == 31:
            setattr(a, fields[field], 10)   
        elif getattr(a, field) == 32 or getattr(a, field) == 33:
            setattr(a, fields[field], 11)
        elif getattr(a, field) == 34 or getattr(a, field) == 35:
            setattr(a, fields[field], 12)
        elif getattr(a, field) == 36 or getattr(a, field) == 37:
            setattr(a, fields[field], 13)
        elif getattr(a, field) == 38 or getattr(a, field) == 39:
            setattr(a, fields[field], 14)
        elif getattr(a, field) == 40 or getattr(a, field) == 41:
            setattr(a, fields[field], 15)
        elif getattr(a, field) == 42 or getattr(a, field) == 43:
            setattr(a, fields[field], -16)  
        elif getattr(a, field) == 44 or getattr(a, field) == 45:
            setattr(a, fields[field], 17)
        elif getattr(a, field) == 46 or getattr(a, field) == 47:
            setattr(a, fields[field], 18)
        elif getattr(a, field) == 48 or getattr(a, field) == 49:
            setattr(a, fields[field], 19)
        elif getattr(a, field) == 50 or getattr(a, field) == 51:
            setattr(a, fields[field], 20)
        elif getattr(a, field) == 52 or getattr(a, field) == 53:
            setattr(a, fields[field], 21)   
        elif getattr(a, field) == 54 or getattr(a, field) == 55:
            setattr(a, fields[field], 22)
        elif getattr(a, field) == 56 or getattr(a, field) == 57:
            setattr(a, fields[field], 23)            
    if a.race == "Гном" or a.race == "гном" or a.race == "ГНОМ":
        a.constitution_ability_score = a.constitution_ability_score + 2
        a.charisma_ability_score = a.charisma_ability_score + 2
        a.srtength_ability_score = a.srtength_ability_score - 2
            

            

