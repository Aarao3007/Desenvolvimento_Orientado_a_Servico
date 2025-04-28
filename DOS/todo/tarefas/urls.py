from django.urls import path
from . import views

urlpatterns = [
    path('listartarefas', views.listarTarefas),
    path('listarusuarios', views.listarUsuarios),
    path('cadastroAtividade', views.cadastroAtividade),
    path('cadastroUsuario', views.cadastroUsuario),
    path('excluirAtividade/<int:id>', views.excluirAtividade),
    path('excluirUsuario/<int:id>', views.excluirUsuario),
]
