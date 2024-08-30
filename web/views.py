import csv
from django.shortcuts import render, redirect
from django.http import FileResponse
from .models import Persona

# Create your views here.

 
def index(request):
    if request.method =='GET':
        personas = Persona.objects.all()
        return render(request, 'index.html', {'personas':personas})
    else:
        print(request.POST)
        nombre_completo = request.POST['nombre_completo']
        peso = request.POST['peso']
        talla = request.POST['talla']
        Persona.objects.create(
            nombre_completo = nombre_completo,
            peso = peso,
            talla = talla
        )
        return redirect('/')
    

def ver_datos(request,id):
    if request.method == 'GET':
        persona = Persona.objects.get(id=id)
        return render(request,'ver_datos.html',{'persona':persona})
    else:
        pk = request.POST['id']
        nombre_completo = request.POST['nombre_completo']
        peso = request.POST['peso']
        talla = request.POST['talla']
        persona = Persona.objects.filter(id=pk)
        persona.update(
            nombre_completo = nombre_completo,
            peso = peso,
            talla = talla
        )
        return redirect('/')


def eliminar_datos(request,id):
    persona = Persona.objects.get(id=id)
    persona.delete()
    return redirect('/')


def descargar_bd(request):
    personas = Persona.objects.all()
    with open('descarga_bd.csv', 'w') as file:
        HEADER = ['nombre_completo', 'peso', 'talla']
        csv_file = csv.writer(file, delimiter=';')
        csv_file.writerow(HEADER)
        for persona in personas:
            csv_file.writerow([
                persona.nombre_completo, 
                persona.peso, 
                persona.talla
            ])

    file =  open('./descarga_bd.csv', 'rb')
    return FileResponse(file)