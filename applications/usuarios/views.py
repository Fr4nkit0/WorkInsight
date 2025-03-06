from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import PersonalizadoLoginForm
from django.contrib.auth import get_user, logout
from django.shortcuts import redirect


# Create your views here.


@login_required
def prueba_config_view(request):
    return render(request, 'usuarios/pages/perfil_page.html', {})


class PersonalizacionLoginView(LoginView):
    template_name = 'usuarios/pages/login_page.html'
    form_class = PersonalizadoLoginForm
    success_url = reverse_lazy('listar_proyectos_page')

def cerrar_sesion_view(request):
    logout(request)
    return redirect('login_page')