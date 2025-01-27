
from django.contrib import admin
from django.urls import path
from newsapp.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    #path('news/', index, name='index'),
    path('login/',login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('search/', search_results, name='search_results'),


    path('logout/', lambda request: logout(request) or redirect('login'), name='logout'),
    path('admin/', admin.site.urls),
    path('contact/', contact_us, name='contact_us'),
    path('about/', about, name='about'),


    path('news/',news_list, name='news_list'),          # List of all news
    path('news/<slug:url>/', news_detail, name='news_detail'), # Single news detail
    path('', home, name='home'),# Single news detail
path('password_reset/', password_reset_request, name='password_reset'),

    path('password_reset/', password_reset_request, name='password_reset_request'),
    path('password_reset_verify/', password_reset_verify, name='password_reset_verify'),
  path('dashboard/', dashboard, name='dashboard'),
    path('add-news/', add_news, name='add_news'),
    path('add-article/', add_article, name='add_article'),
    path('manage-users/', manage_users, name='manage_users'),
    path('manage-messages/', manage_messages, name='manage_messages'),
path('update-user/<int:user_id>/', update_user, name='update_user'),
    path('delete-user/<int:user_id>/', delete_user, name='delete_user'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

