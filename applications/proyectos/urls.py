from django.urls import path
from .views import (listar_proyectos_page_view,
                    listar_proyectos_ajax_view,
                    crear_proyecto_ajax_view,
                    eliminar_proyecto_ajax_view,
                    actualizar_proyecto_ajax_view,
                    crear_pizarra_ajax_view,
                    listar_notas_page_view,
                    listar_notas_ajax_view

                    )
urlpatterns = [
    path('',
         listar_proyectos_page_view,
         name='listar_proyectos_page'),
    path('ajax/crear-proyectos',
         crear_proyecto_ajax_view,
         name='crear_proyecto_ajax_view'
         ),
    path('ajax/eliminar-proyecto',
         eliminar_proyecto_ajax_view,
         name='eliminar_proyecto_ajax_view'
         ),
    path('ajax/actualizar-proyecto',
         actualizar_proyecto_ajax_view,
         name='actualizar_proyecto_ajax_view'
         ),
    path('ajax/crear-pizarra',
         crear_pizarra_ajax_view,
         name='crear_pizarra_ajax_view'
         ),
    path('ajax/listar-proyectos',
         listar_proyectos_ajax_view,
         name='listar_proyectos_ajax_view'
         ),
    path('listar-notas/<int:pizarra_id>',
         listar_notas_page_view,
         name='listar_notas_page'
         ),
    path('ajax/listar-notas/<int:pizarra_id>',
         listar_notas_ajax_view,
         name='listar_notas_ajax_view'
         ),
]
