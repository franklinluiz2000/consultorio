from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from medicSearch.models import Profile
from django.core.paginator import Paginator
from medicSearch.forms.UserProfileForm import UserProfileForm, UserForm

def list_profile_view(request, id=None):
    profile = None
    # Caso o usuário não passe nenhum id a consulta é feita no usuário que está logado
    if id is None and request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
    # Caso o usuario passe o id a consulta do perfil é feita pelo ai passado
    elif id is not None:
        profile = Profile.objects.filter(user__id=id).first()
    # Caso em que nem o usuario passou o id nem estar logado no sistema
    elif not request.user.is_authenticated:
        return redirect(to='/')
    # Caso em que o usuário passe um id que não existe
    if profile == None:
        return redirect(to='/')

    # mostra o perfil buscado
    favorites = profile.show_favorites()
    if len(favorites) > 0:
        paginator = Paginator(favorites, 8)
        page = request.GET.get('page')
        favorites = paginator.get_page(page)



    ratings = profile.show_ratings()
    if len(ratings) > 0:
        paginator = Paginator(ratings, 8)
        page = request.GET.get('page')
        ratings = paginator.get_page(page)

    context = {
        'profile': profile,
        'favorites': favorites,
        'ratings': ratings
    }

    return render(request, template_name='profile/profile.html',context=context, status=200)


@login_required
def edit_profile(request):
    # Usamos esse método para fazer uma consulta no Django. 
    # O primeiro parâmetro é a model que queremos consultar
    # Usado para retornar os dados do usuario e renderizar na página
    profile = get_object_or_404(Profile, user=request.user)
    emailUnused = True
    message = None

    if request.method == 'POST':
        # Ao adicionar o request.FILES como parâmetro da classe UserProfileForm , 
        # estamos dizendo ao Django que queremos salvar arquivos enviados via formulário.
        profileForm = UserProfileForm(request.POST, request.FILES, instance=profile)        
        userForm = UserForm(request.POST, instance=request.user)

        # Verifica se o e-mail que o usuário está tentando utilizar em seu perfil já existe em outro perfil
        verifyEmail = Profile.objects.filter(user__email=request.POST['email']).exclude(user__id=request.user.id).first()
        emailUnused = verifyEmail is None
    else:
        profileForm = UserProfileForm(instance=profile)
        userForm = UserForm(instance=request.user)

    if profileForm.is_valid() and userForm.is_valid() and emailUnused:
        profileForm.save()
        userForm.save()
        message = { 'type': 'success', 'text': 'Dados atualizados com sucesso' }    
    else:
    # Aqui verificamos se é do tipo post, para que na primeira vez que a página 
    # carregar a mensagem não apareça, já que no primeiro carregamento não enviamos 
    # um post, o form é dado como inválido e entra aqui.
        if request.method == 'POST':
            if emailUnused:
                # Se o e-mail não está em uso mas o formulário tiver algum dado inválido.
                message = { 'type': 'danger', 'text': 'Dados inválidos' }
            else:
                # Se o e-mail que o usuário tentou usar já está em uso por outra pessoa.
                message = { 'type': 'warning', 'text': 'E-mail já usado por outro usuário' }


    context = {
        'profileForm': profileForm,
        'userForm': userForm,
        'message': message
    }
    
    return render(request, template_name='user/profile.html', context=context, status=200)