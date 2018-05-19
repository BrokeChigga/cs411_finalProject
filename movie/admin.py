from django.contrib import admin
from .models import Actor, Director, DirectedBy, Like, Movie, PlayedBy, Review, User, Has
# Register your models here.

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(DirectedBy)
admin.site.register(Like)
admin.site.register(Movie)
admin.site.register(PlayedBy)
admin.site.register(Review)
admin.site.register(User)
admin.site.register(Has)
