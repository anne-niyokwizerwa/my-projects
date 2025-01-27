from django.shortcuts import render, get_object_or_404
from.models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from  django.contrib import messages
from django.contrib.auth import get_user_model
import random
import string
from django.shortcuts import render, redirect
from .models import News, Article, Contact
from .forms import NewsForm, ArticleForm, ContactForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.hashers import make_password
from datetime import datetime, timedelta
from django.contrib import messages
from django.contrib.auth.models import User
User = get_user_model()

def index(request):
    return render(request, 'index.html', {'articles': Article.objects.all()})
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page after login
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Redirect to login page after successful sign-up
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# @login_required
# def home_view(request):
#     return render(request, 'home.html')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Thank you! Your message has been sent.')
            return redirect('contact_us')  # Redirect back to the contact page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})




def news_list(request):
    news_lists = News.objects.order_by('-date')  # Fetch news sorted by latest date
    return render(request, 'new_list.html', {'news_list': news_lists})

def news_detail(request, url):
    news = get_object_or_404(News, url=url)
    return render(request, 'news_detail.html', {'news': news})
def about(request):
    return render(request, 'about.html')
def home(request):
    return render(request, 'home.html')

from django.shortcuts import render
from .models import NewsArticle
from .forms import SearchForm

def home(request):
    return render(request, 'home.html')

def search_results(request):
    form = SearchForm(request.GET)
    news_list = None
    if form.is_valid():
        query = form.cleaned_data['query']
        news_list = News.objects.filter(title__icontains=query) | News.objects.filter(content__icontains=query)
    return render(request, 'base.html', {'form': form, 'news_list':news_list})
VERIFICATION_CODES = {}


def send_verification_code(email):
    """Generate and send a verification code to the given email."""
    code = ''.join(random.choices(string.digits, k=6))  # 6-digit OTP
    expiration_time = datetime.now() + timedelta(minutes=10)  # Expires in 10 minutes
    VERIFICATION_CODES[email] = {'code': code, 'expires_at': expiration_time}

    # Send email
    send_mail(
        subject='Password Reset Verification Code',
        message=f'Your verification code is: {code}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )


def password_reset_request(request):
    """Step 1: User requests a password reset."""
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            send_verification_code(email)
            messages.success(request, 'A verification code has been sent to your email.')
            return redirect('password_reset_verify')
        else:
            messages.error(request, 'No user found with this email address.')

    return render(request, 'password_reset_request.html')


def password_reset_verify(request):
    """Step 2: User enters verification code and new password."""
    if request.method == 'POST':
        email = request.POST.get('email')
        code = request.POST.get('code')
        new_password = request.POST.get('password')

        # Check if the code is valid
        stored_data = VERIFICATION_CODES.get(email)
        if stored_data and stored_data['code'] == code:
            if datetime.now() > stored_data['expires_at']:
                messages.error(request, 'Verification code has expired.')
            else:
                # Reset the password
                user = User.objects.filter(email=email).first()
                if user:
                    user.password = make_password(new_password)
                    user.save()
                    messages.success(request, 'Your password has been reset successfully.')
                    return redirect('login')
        else:
            messages.error(request, 'Invalid verification code.')

    return render(request, 'password_reset_verify.html')
# from django.shortcuts import render, redirect
# from .models import News, Article, Message
# from .forms import NewsForm, ArticleForm, MessageForm
# from django.contrib.auth.models import User

def dashboard(request):
    total_news = News.objects.count()
    total_articles = Article.objects.count()
    total_users = User.objects.count()
    total_messages = Contact.objects.count()
    return render(request, 'dashboard.html', {
        'total_news': total_news,
        'total_articles': total_articles,
        'total_users': total_users,
        'total_messages': total_messages,
    })

def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})

def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ArticleForm()
    return render(request, 'add_article.html', {'form': form})

def manage_users(request):
    users = User.objects.all()
    return render(request, 'manage_users.html', {'users': users})

def manage_messages(request):
    messages = Contact.objects.all()
    return render(request, 'manage_messages.html', {'messages': messages})
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('manage_users')
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'update_user.html', {'form': form, 'user': user})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('manage_users')