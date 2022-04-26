from django.contrib import admin
from django.urls import path, re_path as url

from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import include

# Altere a linha a seguir adicionando o + e todos os itens que vem a seguir dele.
# Aqui estamos dizendo ao Django que dentro do admin poderemos acessar o diretório de imagens (media) e o static
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('medicSearch.urls.HomeUrls')),
    path('', include('medicSearch.urls.AuthUrls')),
    path('profile/', include('medicSearch.urls.ProfileUrls')),
    path('medic/', include('medicSearch.urls.MedicUrls')),

] + static(settings
        .STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings
            .MEDIA_URL, document_root=settings.MEDIA_ROOT)