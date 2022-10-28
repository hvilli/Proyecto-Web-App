from email.message import EmailMessage
from django.shortcuts import render, redirect

from .forms import FormularioContacto

# Create your views here.

def contacto(request):

    formulario_contacto = FormularioContacto()

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Mensaje desde App Django",
            "EL usuario con nombre {} con la direccion {} escribe lo siguiente: \n\n {}".format(nombre,email,contenido),
            "",["hvilli.perez.99@gmail.com"], replay_to = [email])

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?")

            

    return render(request, "contacto/contacto.html", {'miFromulario':formulario_contacto})