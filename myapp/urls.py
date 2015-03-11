from django.conf.urls import patterns, url

urlpatterns = patterns('myapp.views',
    url(r'^$', 'register', name='register'),
    url(r'^login$', 'connexion', name='login'),
    url(r'^logout$', 'logout_view', name='logout'),
    url(r'^account$', 'account', name='account'),
    url(r'^personnage/new$', 'addPersonnage'),
    url(r'^changeperso/(?P<id>\d+)$', 'changePerso'),
    url(r'^quete/(?P<id>\d+)$', 'quest'),
    url(r'^fight/(?P<id>\d+)$', 'fight'),
    url(r'^finish_quest/(?P<id>\d+)$', 'finish_quest'),
    url(r'^changeitem/(?P<id>\d+)$', 'changeItem'),
    url(r'^shop$', 'shop'),
)
