from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Actor, Director, DirectedBy, Like, Movie, PlayedBy, Review, User, Has
from django.db import connection
import sqlite3
import pip
#pip.main(["install","omdb"])
#import omdb
import sys


actor_name = set()
director_name = set()
'''
def main():
    global actor_name
    global director_name

    file_name = open('input.txt', 'r').readlines()
    file_name = [line[:-1] for line in file_name]

    for i in file_name:
        search = omdb.get(title=i, timeout=5)
        if search is None or search.title is None:
            continue
        title = search.title
        length = search.runtime
        length = (int(length[:-4]))
        year = int(search.year)
        rating = float(search.imdb_rating)
        description = search.plot
        category = (search.genre)
        actors = (search.actors).split(", ")
        directors = (search.director).split(", ")
        for a in actors:
            if(a is not None):
                actor_name.add(a)
        for d in directors:
            if (a is not None):
                director_name.add(d)

main()

'''
def index(request):
    all_movies = Movie.objects.all()
    context = {'all_movies': all_movies,}
    return render(request, 'movie/index.html', context)


def review(request):
    all_reviews = Review.objects.all()
    context = {'all_reviews': all_reviews,}
    return render(request, 'movie/review.html', context)


def reviewChange(request, review_id):
    review = Review.objects.get(pk=review_id)
    return render(request, 'movie/reviewchange.html', {'review': review})


def detail(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("movie does not exist")
    return render(request, 'movie/detail.html', {'movie': movie})


temp = Movie.objects.raw('SELECT ')


def advsearch(request, ):
    all_movies = Movie.objects.all()
    context = {'all_movies' : all_movies,}
    return render(request, 'movie/advsearch.html', context)


def like(request, ):
    all_movies = Movie.objects.all()
    context = {'all_movies' : all_movies,}
    return render(request, 'movie/mymlike.html', context)


def loginpage(request, ):
    all_movies = Movie.objects.all()
    context = {'all_movies' : all_movies,}
    return render(request, 'movie/loginpage.html', context)


def create_user(request, ):
    all_movies = Movie.objects.all()
    context = {'all_movies' : all_movies,}
    return render(request, 'movie/create_user.html', context)

''''''
def find_movie_rating(request, moviename):
    try:
        movie = Movie.objects.get(name = moviename)
    except Movie.DoesNotExist:
        raise Http404("movie does not exist")
    find_rating = Movie.objects.raw('SELECT rating FROM Movie WHERE name = %s', str(moviename))
    #find_rating = Movie.objects.raw(find_rating)
    context = {'movie_rating' : find_rating}
    return render(request, 'movie/find_movie_rating.html', context)
''''''


def reviewfads(request, review_id):
    try:
        review = Review.objects.get(pk=review_id)
    except Review.DoesNotExist:
        raise Http404("review does not exist")
    return render(request, 'movie/review.html', {'review': review})


def find_movie_rating(request, moviename):
    try:
        mymovie = Movie.objects.get(name = moviename)
    except Movie.DoesNotExist:
        raise Http404("movie does not exist")

    cursor = connection.cursor()
    cursor.execute('SELECT rating FROM movie_Movie WHERE name = %s', (str(moviename),))
    result = cursor.fetchone()[0]

    context = {'movie_rating' : result,}
    return render(request, 'movie/find_movie_rating.html', context)


def reviewAdd(request):
    try:
        myuser = User.objects.get(email=request.POST['email'])
    except User.DoesNotExist:
        raise Http404("User does not exist")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO movie_Review(email, content) VALUES(%s, %s)', (str(request.POST['email']), str(request.POST['content']),))
    all_reviews = Review.objects.all()
    return render(request, 'movie/review.html', {'all_reviews': all_reviews})

def reviewUpdate(request, review_id):
    try:
        myreview = Review.objects.get(pk = review_id)
    except Review.DoesNotExist:
        raise Http404("Review does not exist")
    cursor = connection.cursor()
    cursor.execute('UPDATE movie_Review SET content = %s WHERE id = %s', (str(request.POST['content']), str(review_id)))
    review = Review.objects.get(pk=review_id)
    return render(request, 'movie/reviewChange.html', {'review': review})


def reviewDelete(request, review_id):
    try:
        myreview = Review.objects.get(pk=review_id)
    except Review.DoesNotExist:
        raise Http404("Review does not exist")
    cursor = connection.cursor()
    cursor.execute('DELETE FROM movie_Review WHERE id = %s', (str(review_id),))
    all_reviews = Review.objects.all()
    return render(request, 'movie/review.html', {'all_reviews': all_reviews})


def actorSearch(request,):
    actorname = request.POST.get('actor_name', False)
    try:
        myactor = Actor.objects.get(name = str(actorname))
    except Actor.DoesNotExist:
        raise Http404("Actor does not exist")

    cursor = connection.cursor()
    cursor.execute('SELECT AVG(rating) FROM movie_Movie WHERE name IN (SELECT movie_name FROM movie_PlayedBy WHERE movie_PlayedBy.actor_name = %s)', \
              (str(actorname),))

    result = cursor.fetchone()[0]
    context = {'actor_avg_rating': result, }
    return render(request, 'movie/advsearch.html', context)


def directorSearch(request, ):
    directorname = request.POST.get('director_name', False)
    try:
        mydirector = Director.objects.get(name = str(directorname))
    except Director.DoesNotExist:
        raise Http404("Director does not exist")
    cursor = connection.cursor()
    cursor.execute('SELECT name, MAX(rating) FROM movie_Movie, movie_DirectedBy WHERE movie_Movie.name = movie_DirectedBy.movie_name AND director_name = %s', (str(directorname),))
    result = str(cursor.fetchone()[0])
    print(result)
    context = {'directorsMovie': result, }
    return render(request, 'movie/advsearch.html', context)


def like_movie(request, ):

    context = {'like_condition': 'like', }
    return render(request, 'movie/detail.html', context)


def unlike_movie(request, ):

    context = {'like_condition': 'unlike', }
    return render(request, 'movie/detail.html', context)

def load_data(request):

    global actor_name
    global director_name

    file_name = open('input.txt', 'r').readlines()
    file_name = [line[:-1] for line in file_name]

    for i in file_name:
        client = Client()
        search = omdb.get(title=i, timeout = 5)
        if search is None or search.title is None:
            continue
        title = search.title
        length = search.runtime
        length = (int(length[:-4]))
        year = int(search.year)
        rating = float(search.imdb_rating)
        description = search.plot
        category = (search.genre)
        actors = (search.actors).split(", ")
        directors = (search.director).split(", ")
        m = Movie(name = title, year = year, description = description, length = length, rating = rating, category = category)
        m.save()
        for a in actors:
            p = PlayedBy(movie_name = title, movie_year = year, actor_name = a)
            p.save()
            if(a not in actor_name):
                a = Actor(name = a)
                a.save()
            actor_name.add(a)
        for d in directors:
            d = DirectedBy(movie_name = title, year = year, director_name = d)
            d.save()
            if (a not in actor_name):
                d = Director(name = d)
                d.save()
            director_name.add(d)


    context = {'success': 1,}
    return render(request, 'movie/advsearch.html', context)


