from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import re
from django.http import JsonResponse
from .models import *
# Create your views here.

@login_required(login_url='core:login')
def index(request):
    # movies = Movies.objects.all().order_by('-created_date')
    movies = Movies.objects.all()


    args = {
        'movies': movies,
    }

    return render(request, 'core/index.html', args)



@login_required(login_url='core:login')
def movie(request, pk):
    movie_uuid = pk
    movie_details = Movies.objects.get(uu_id=movie_uuid)

    context = {
        'movie_details':movie_details
    }

    return render(request, 'core/movie.html', context)

@login_required(login_url='core:login')
def my_list(request):
  pass
   
@login_required(login_url='core:login')
def add_to_list(request):
    if request.method == 'POST':
        movie_url_id = request.POST.get('movie_id')
        # using regex (regular expression)
        uuid_pattern = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
        match = re.search(uuid_pattern, movie_url_id)
        movie_id = match.group() if match else None

        movie = get_object_or_404(Movies, uu_id=movie_id)
        movie_list, created = MovieList.object.get_or_create(owner_user=request.user, movie=movie)

        if created:
            response_data = {'status': 'success', 'message': 'Added _/'}
        else:
            response_data = {'status':'info', 'message': 'Movie already in list'}

        return JsonResponse(response_data)
    else:
         return JsonResponse ({'status':'error', 'message': 'Invalid request'}, status=400) 
    

@login_required(login_url='core:login')
def search(request):

    if request.method == 'POST':
        search_term = request.POST['search_term']
        movies = Movies.objects.filter(title__icontains=search_term)

        context = {
            "movies": movies,
            "search_term": search_term,
        }
        return render(request, 'core/search.html', context)

    else:
        return redirect('/')


@login_required(login_url='core:login')  
def genre(request, pk):

    movie_genre = pk 

    movies = Movies.objects.filter(genre=movie_genre)

    data = {
        'movies': movies,
        'movie_genre': movie_genre,
    }

    return render(request, 'core/genre.html', data)


















# LOGIN AND REGISTER

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user )
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('core:login')

    else:
        return render(request, 'core/login.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('core:signup')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
                return redirect('core:signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # Log the user in
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                return redirect('/')

        else:
            messages.info(request, 'Password not matching')
            return redirect('core:signup')



    else:
        return render(request, 'core/register.html')


@login_required(login_url='core:login')
def logout(request):
    auth.logout(request)
    return redirect('core:login')
