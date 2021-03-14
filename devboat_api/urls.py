from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('users.urls')),
    path('api/v1/',include('education.urls')),
    path('api/v1/',include('interests.urls')),
    path('api/v1/',include('job.urls')),
    path('api/v1/',include('projects.urls')),
    path('api/v1/',include('skills.urls')),
    path('api/v1/',include('connections.urls')),
    path('api/v1/',include('requests.urls')),
    path('api/v1/',include('posts.urls')),
    path('api/v1/',include('upvotes.urls')),
    path('api/v1/',include('comments.urls')),
    path('api/v1/',include('books.urls')),
    path('api/v1/',include('comment_upvotes.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('api/v1/auth/', include('rest_auth.urls'))
]
