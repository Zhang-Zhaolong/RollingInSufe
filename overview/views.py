from django.shortcuts import render, get_object_or_404
from userprofile.models import Profile
# Create your views here.


def index(request):
    user_pk = request.user.pk
    profile = get_object_or_404(Profile, user_id=user_pk)
    return render(request, 'overview/index.html', context={
        'profile': profile,
    })

