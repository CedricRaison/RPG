from django.contrib import admin
from myapp.models import *

class PnjAdmin(admin.ModelAdmin):
	list_display = ('nom', 'force', 'vie', 'enigme')
	search_fields = ('nom', )

class ReponseAdmin(admin.ModelAdmin):
	model = Reponse
	list_display = ('answer', 'get_enigme')

	def get_enigme(self, obj):
		return obj.enigme.enigme
	

	# get_enigme.short_description = 'enigme'


admin.site.register(Pnj, PnjAdmin)
admin.site.register(Reponse, ReponseAdmin)
admin.site.register(Quete)
admin.site.register(Item)
admin.site.register(Personnage)
admin.site.register(Sac)
admin.site.register(Profile)
admin.site.register(Etape)
admin.site.register(Shop)