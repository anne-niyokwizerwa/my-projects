
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
    path('deactivate-user/<int:user_id>/', deactivate_user, name='deactivate_user'),
    path('add-article/', add_article, name='add_article'),
    path('manage-users/', manage_users, name='manage_users'),
path('grant-admin/<int:user_id>/', grant_admin, name='grant_admin'),
    # path('manage-messages/', manage_messages, name='manage_messages'),
path('revoke-admin/<int:user_id>/', revoke_admin, name='revoke_admin'),

path('update-user/<int:user_id>/', update_user, name='update_user'),
    path('delete-user/<int:user_id>/', delete_user, name='delete_user'),
    path('activate-user/<int:user_id>/', activate_user, name='activate_user'),
    path('redirect-to-home/',redirect_to_home, name='redirect_to_home'),
    path('manage-news/', manage_news, name='manage_news'),
    path('articles/', articles, name='articles'),
    path('messages/', messages, name='messages'),
    path('articles/add/', add_article, name='add_article'),
    path('articles/edit/<int:article_id>/', edit_article, name='edit_article'),
    path('articles/delete/<int:article_id>/', delete_article, name='delete_article'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

