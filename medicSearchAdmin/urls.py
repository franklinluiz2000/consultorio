from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

# Altere a linha a seguir adicionando o + e todos os itens que vem a seguir dele.
# Aqui estamos dizendo ao Django que dentro do admin poderemos acessar o diretório de imagens (media) e o static
urlpatterns = [
    path('admin/', admin.site.urls),] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, 
document_root=settings.MEDIA_ROOT)