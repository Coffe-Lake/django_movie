from django.contrib import admin

from .models import Actor, Category, Reviews, RatingStars, Rating, Genre, Movie, MovieShots
# Register your models here.
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStars)
admin.site.register(Reviews)
