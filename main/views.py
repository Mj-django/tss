from django.shortcuts import render
from django.views import View
from .models import user, user_as
from django.http import Http404, JsonResponse
from django.core import serializers


# Create your views here.
class main_slug(View):

    def get(self, request, slug):
        request.session['username'] = 'mjgh'
        request.session['pk'] = 4
        request.session['password'] = 'tisno'
        print(request.session['username'])
        if slug == 'users':
            try:
                print('s')
                if f := user_as.objects.get(username=user.objects.get(username=request.session['username']),
                                            password=request.session['password'], is_active=True, is_admin=True):
                    print(f)
                    return render(
                        request,
                        'main.html',
                        {
                            'ad_ac': True,
                            'user': f,
                            'filter': 'all',
                            'users': user_as.objects.all() if len(
                                user_as.objects.all()) < 50 else user_as.objects.all()[-1:-20:-1]
                        }
                    )
                else:
                    return Http404
            except:
                return Http404


class main(View):
    def post(self, request):
        if (name_form := request.POST['name_form']) == 'edit_user':
            if user_as.objects.get(
                    username=user.objects.get(username=request.session['username']),
                    password=request.session['password'],
                    is_active=True,
                    is_admin=True
            ):
                request.session['select_username'] = request.POST['wed']
                return JsonResponse(
                    {
                        'username': (
                            h := user_as.objects.get(
                                username=user.objects.get(
                                    pk=int(request.POST['wed'])
                                )
                            )
                        ).username.username,
                        'admin': h.is_admin,
                        'active': h.is_active
                    }
                )

        elif name_form == 'edit_user_tk':
            if user_as.objects.get(
                    username=user.objects.get(username=request.session['username']),
                    password=request.session['password'],
                    is_active=True,
                    is_admin=True
            ):
                print('d', user.objects.filter(username=request.POST['username']),
                      user.objects.get(pk=int(request.session['select_username'])).username == request.POST['username'],
                      request.POST['username'], request.session['select_username'])
                if request.POST['active'] and request.POST['admin'] and request.POST['username'] and not (j := not (
                        user.objects.get(pk=request.session['select_username']).username == request.POST[
                    'username'] or not user.objects.filter(username=request.POST['username']))):
                    print(j)

                    the_user = user_as.objects.get(
                        username=user.objects.get(pk=int(request.session['select_username'])))
                    print(the_user)
                    x = the_user.username
                    x.username = request.POST['username']
                    x.save()
                    print('ss')
                    the_user.is_admin = True if request.POST['admin'] == 'true' else False
                    the_user.is_active = True if request.POST['active'] == 'true' else False
                    print('t')
                    the_user.save()
                    print('sdf')
                    print(int(request.session['pk']),
                          int(request.session['select_username']) == int(request.session['pk']),
                          int(request.session['select_username']))
                    if int(request.session['select_username']) == int(request.session['pk']):
                        print('sd')
                        request.session['username'] = request.POST['username']
                        print(request.session['username'], request.POST['username'])
                    request.session['select_username'] = user.objects.get(username=request.POST['username']).pk

                    is_success = True
                else:
                    is_success = False
                if is_success:
                    return JsonResponse(
                        {
                            'success': True,

                        }

                    )
                else:
                    return JsonResponse(
                        {
                            'success': False,
                            'username_found': not j,
                            'username_kh': True if not request.POST['username'] else False,
                            'active_kh': True if not request.POST['active'] else False,
                            'admin_kh': True if not request.POST['admin'] else False,

                        }
                    )
        elif name_form == 'del_user':
            if user_as.objects.get(
                    username=user.objects.get(username=request.session['username']),
                    password=request.session['password'],
                    is_active=True,
                    is_admin=True
            ):
                try:
                    the_user = user_as.objects.get(username=(u := user.objects.get(pk=int(request.POST['user']))))
                    the_user.delete()
                    u.delete()
                    s = True
                except:
                    s = False
                return JsonResponse(
                    {
                        'succes':s
                    }
                )
