from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from myapp.forms import *
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.forms.util import ErrorList
from django.http import HttpResponse

def not_loggedin_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(account)
        else:
            return function(request, *args, **kwargs)
    return wrap

@not_loggedin_required
def register(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user = User.objects.create_user(username, email, password)
			request.session['msg'] = 'inscription réussi'
			return redirect(connexion)
	else:
		form = UserForm()
	return render(request, 'myapp/register.html', locals())


@not_loggedin_required
def connexion(request):
	if request.method =='POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect(account)
				else:
					msg = 'compte banni'
			else:
				msg = 'invalid password'
	else:
		form = LoginForm()
	return render(request, 'myapp/login.html', locals())

def logout_view(request):
	logout(request)
	return redirect(connexion)


@login_required
def account(request):
	quetes = Quete.objects.all()
	personnages = Personnage.objects.filter(user__username__contains=request.user.username)
	test = getattr(request.user.profile.perso, 'cape')
	try:
		inventory = Sac.objects.filter(personnage=request.user.profile.perso)
	except:
		pass
	return render(request, 'myapp/account.html', locals())

@login_required
def addPersonnage(request):
	if request.method == 'POST':
		f = NewPersonnageForm(request.POST)
		if f.is_valid():
			perso = Personnage()
			perso.nom = f.cleaned_data['nom']
			perso.force = f.cleaned_data['force']
			perso.vie = f.cleaned_data['vie']
			perso.level = 1
			perso.xp = 0
			perso.user = request.user
			if perso.vie + perso.force > 10:
				errors = f._errors.setdefault('__all__', ErrorList())
				errors.append(u"Vous pouvez attribuer seulement 10 points")
			perso.save()
			msg = 'personnage créé'
	else:
		f = NewPersonnageForm()
	return render(request, 'myapp/addPersonnage.html', locals())

@login_required
def changePerso(request, id):
	perso = get_object_or_404(Personnage, id=id)
	if perso.user != request.user:
		return redirect(connexion)
	try:
		request.user.profile.perso = perso
		request.user.profile.save()
	except:
		profile = Profile()
		profile.user = request.user
		profile.perso = perso
		profile.save()
	return redirect(account)

@login_required
def quest(request, id):
	quete, pnjs, etape, pnj = getQueteData(request, id)
	if pnj == False:
		return redirect(finish_quest, id)
	if request.method == 'POST':
		send = True
		f = reponseForm(request.POST)
		if f.is_valid():
			reponse = f.cleaned_data['reponse']
			result = pnj.reponse_set.first().answer
			if reponse != result:
				f.add_error(None, 'mauvaise réponse !')
				return render(request, 'myapp/quete.html', locals())
			updateEtape(request, etape, quete)
			return redirect(quest, id)
	else:
		f = reponseForm()
	return render(request, 'myapp/quete.html', locals())

def getQueteData(request, id):
	quete = get_object_or_404(Quete, id=id)
	pnjs = quete.pnj_set.all()
	etape = Etape.objects.filter(personnage=request.user.profile.perso).filter(quete=quete)

	if not etape:
		pnj = pnjs[0]
	else:
		try:
			pnj = pnjs[etape[0].etape]
		except:	
			pnj = False
	return quete, pnjs, etape, pnj

def combat(perso, pnj):
	persoLife = perso.vie
	pnjLife = pnj.vie
	msg = []
	i = 0
	while i != 1:
		pnjLife -= perso.force
		msg.append(perso.nom + ' enlève ' + str(perso.force) + ' pv !')  
		if pnjLife <= 0:
			pnjLife = 0
		msg.append(pnj.nom + ' a ' + str(pnjLife) + ' pv') 
		if pnjLife <= 0:
			msg.append(pnj.nom + 'est ko') 
			msg.append('Vous avez gagné') 
			result = True
			return msg, result
		persoLife -= pnj.force
		msg.append(pnj.nom + ' enlève ' + str(pnj.force) + ' pv !') 
		if persoLife <= 0:
			persoLife = 0
		msg.append(perso.nom + ' a ' + str(persoLife) + ' pv') 
		if persoLife <= 0:
			msg.append('Vous êtes ko')
			msg.append('Vous avez perdu') 
			result = False
			return msg, result

def updateEtape(request, etape, quete):
	if etape:
		etape[0].etape += 1
		etape[0].save()
	else:
		etape = Etape()
		etape.personnage = request.user.profile.perso
		etape.quete = quete
		etape.etape = 1
		etape.save()
	return

@login_required
def fight(request, id):
	quete, pnjs, etape, pnj = getQueteData(request, id)
	perso = request.user.profile.perso
	msg, result = combat(perso, pnj)
	if result == True:
		updateEtape(request, etape, quete)
		
	return render(request, 'myapp/fight.html', locals())


@login_required
def finish_quest(request, id):
	quete = get_object_or_404(Quete, id=id)
	xp = quete.xp
	item = quete.item
	perso = request.user.profile.perso
	perso.xp += xp
	perso.save()
	bag = Sac()
	bag.personnage = perso
	bag.item = item
	bag.save()
	return render(request, 'myapp/finish_quest.html', locals())


@login_required
def changeItem(request, id):
	item = Sac.objects.get(id=id)
	typeOf = item.item.typeOf
	perso = request.user.profile.perso
	oldItem = getattr(perso, typeOf)
	setattr(perso, typeOf, item)
	if oldItem is not None:
		perso.force -= oldItem.item.force
		perso.vie -= oldItem.item.vie
	perso.vie += item.item.vie
	perso.force += item.item.force
	perso.save()
	return redirect(account)

@login_required
def shop(request):
	if request.method == 'POST':
		itemId = request.POST['item']
		inventaire = get_object_or_404(Sac, id=itemId)
		item = inventaire.item
		article = Shop()
		article.item = item
		article.inventaire = inventaire
		article.save()



	itemsToBuy = Shop.objects.all()
	myItems = Sac.objects.filter(personnage = request.user.profile.perso)


	return render(request, 'myapp/shop.html', locals())