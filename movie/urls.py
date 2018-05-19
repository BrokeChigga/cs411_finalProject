from django.conf.urls import url
from . import views
app_name = 'movie'

urlpatterns = [
    # /movie/
    url(r'^$', views.index, name='index'),

    # /movie/98723/
    url(r'^(?P<movie_id>[0-9]+)/$',views.detail, name='detail'),

    # /movie/review
    url(r'^review/$', views.review, name='review'),

    #reviewcontent
    # /movie/review/reviewid
    url(r'^review/(?P<review_id>[0-9]+)/$', views.reviewChange, name='reviewChange'),

    # /movie/reviewAdd
    url(r'^review/reviewAdd/$', views.reviewAdd, name='reviewAdd'),

    # /movie/reviewUpdate
    url(r'^review/reviewUpdate/(?P<review_id>[0-9]+)/$', views.reviewUpdate, name='reviewUpdate'),

    # /movie/reviewDelete
    url(r'^review/reviewDelete/(?P<review_id>[0-9]+)/$', views.reviewDelete, name='reviewDelete'),


    # /movie/advsearch
    url(r'^advsearch/$', views.advsearch, name='advsearch'),

    #
    url(r'^actorSearch/$', views.actorSearch, name='actorSearch'),

    #
    url(r'^directorSearch/$', views.directorSearch, name='directorSearch'),

    # /movie/like
    url(r'^like/$', views.like, name='like'),


    # /movie/loginpage
    url(r'^loginpage/$', views.loginpage, name='loginpage'),


    # /movie/create_user
    url(r'^create_user/$', views.create_user, name='create_user'),

    #
    url(r'^load_data/$', views.load_data, name='load_data'),

    #
    url(r'^like_moive/$', views.like_movie, name='like_movie'),

    #
    url(r'^unlike_movie/$', views.unlike_movie, name='unlike_movie'),

    # /movie/moviename
    url(r'^(?P<moviename>.+)/$',views.find_movie_rating, name='find_movie_rating'),

]
