from medicSearch.models import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICE, default=3)
    birthday = models.DateField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)

    image = models.ImageField(null=True, blank=True)

    favorites = models.ManyToManyField(User, blank=True, related_name='favorites')
    specialties = models.ManyToManyField(Speciality, blank=True, related_name='specialties')
    addresses = models.ManyToManyField(Address, blank=True, related_name='addresses')

    # método que usamos para exibir o objeto quando quisermos acessá-lo através de sua instância.
    def __str__(self):
        return '{}'.format(self.user.username)

    '''Cria um novo perfil de usuário onde post_save informa que, em um determinado método post , create_user_profile deve
    ser acionado. Já sender=User informa qual classe Model está sendo chamada no post'''
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        # adicionado try e except para que o superusuario não quebre essa lógica
        try:
            if created:
                Profile.objects.create(user=instance)
        except:
            pass
    
    # salva qualquer alteração no perfil automaticamente
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass