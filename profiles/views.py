#views of profiles_app
from django.shortcuts import render, Http404, redirect
users = [
]


# profiles/?name=qwer&password=qwe
def start_profile(request):
    if request.GET.get('name', None):
        info = request.GET.get('name')
        return redirect('profiles', name=info)
        # return profiles(request, info)
    context = {}
    return render(request, 'profiles/start_profiles.html', context)

def profiles(request, name):
    context = {}
    context['user'] = name
    context['users'] = users
    return render(request, 'profiles/profiles.html',context)
