from django.db import models
from django.contrib.auth.models import User
from django.conf.urls.static import static
from django.conf import settings

from setup.settings import BASE_DIR, BASE_URL, MEDIA_ROOT, MEDIA_URL



class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, help_text="Nome da categoria.")
    status = models.BooleanField(default=True, verbose_name="Ativo")

    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'tab_categoria'
        verbose_name_plural=u'Categorias'

class TipoImovel(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, help_text="Nome.")
    status = models.BooleanField(default=True, verbose_name="Ativo")

    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'tab_tipoImovel'
        verbose_name_plural=u'Tipos de imóveis'

class Imovel(models.Model):
    id = models.AutoField(primary_key=True)
    tipoImovel = models.ForeignKey(TipoImovel, on_delete=models.CASCADE, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=False)
    nome = models.CharField(max_length=50, help_text="Nome.")
    descricao = models.TextField(help_text="Descrição do imovel.")
    status = models.BooleanField(default=True, verbose_name="Ativo")

    def fotoCapa(self):
        fotos = Fotos.objects.filter(imovel_id=self.id)
        print()
        if len(fotos) > 0:
            print("A foto é: ",fotos[0].foto)
            return fotos[0].foto
        else:
            return ''
    def fotos(self):
        fotos = Fotos.objects.filter(imovel_id=self.id)
        if len(fotos)>0:
            ignorar = fotos[0].id
            fotos = fotos.exclude(id=ignorar)
            #print('Fotos são: ',fotos)
            return fotos
        else:
            return ''
    @property
    def categoria_nome(self):
        return self.categoria.nome
    

    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'tab_imovel'
        verbose_name_plural=u'Imóveis'

class Fotos(models.Model):
    id = models.AutoField(primary_key=True)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="fotosImoveis/%Y-%m-%d", verbose_name="Foto", help_text="Escolha uma foto.", blank=True)
    #foto = models.ImageField(blank=True)
    descricao = models.TextField(verbose_name="Descrição", help_text="Descrição", blank=True)

    #def __str__(self):
    #    return "%s - %s" % (self.imovel.nome, self.descricao)
    @property
    def url(self):
        #print("FOTO: ",self.foto)

        return str(BASE_URL+'media/')+ str(self.foto)
        #return self.foto
    class Meta:
        managed = True
        db_table = 'tab_fotosImoveis'
        verbose_name_plural=u'Fotos dos imóveis'

class Pessoa(models.Model):

    SEXO_OPCOES = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )

    id = models.AutoField(primary_key=True)
    nome = models.CharField(verbose_name="Nome", max_length=250, help_text="Nome completo.")
    dataNascimento = models.DateField(verbose_name="Data de Nascimento", help_text="dd/mm/aaaa")
    sexo = models.CharField(choices=SEXO_OPCOES, default='M', verbose_name="Sexo", help_text="Escolha o sexo", max_length=1)
    avatar = models.ImageField(upload_to= "media/avatar/%Y/%m/%d", verbose_name="Avatar", help_text="Escolha uma imagem.", blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True, verbose_name="Ativo")

    def idade(self):
        today = date.today()
        return today.year - self.dataNascimento.year - ((today.month, today.day) < (self.dataNascimento.month, self.dataNascimento.day))

    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'tab_pessoa'
        verbose_name_plural=u'Pessoas'

