from django.shortcuts import redirect

def login_redirect(reques):
    return redirect('/account/login')