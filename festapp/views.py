from django.shortcuts import render, redirect
from .models import LoginRecord

# -------- LOGIN CHECK --------
def check_login(request):
    return request.session.get('user')


# -------- LOGIN --------
def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        section = request.POST.get('section')
        password = request.POST.get('password')

        # ✅ Admin login
        if name == "Sai" and section == "Sr.MCA-A" and password == "12345":
            request.session['user'] = name
            request.session['admin'] = True

            LoginRecord.objects.create(name=name, section=section, password=password)

            return redirect('admin_dashboard')

        # ✅ Normal user login (anyone allowed)
        elif name and section and password:
            request.session['user'] = name
            request.session['admin'] = False

            LoginRecord.objects.create(name=name, section=section, password=password)

            return redirect('home')

        else:
            return render(request, 'login.html', {'error': 'Invalid Details ❌'})

    return render(request, 'login.html')


# -------- LOGOUT --------
def logout(request):
    request.session.flush()
    return redirect('login')


# -------- HOME --------
def home(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'home.html')


# -------- ADMIN DASHBOARD --------
def admin_dashboard(request):
    if not request.session.get('admin'):
        return redirect('login')

    data = LoginRecord.objects.all().order_by('-login_time')

    return render(request, 'admin_dashboard.html', {'data': data})


# -------- DELETE USER --------
def delete_user(request, id):
    if not request.session.get('admin'):
        return redirect('login')

    LoginRecord.objects.get(id=id).delete()
    return redirect('admin_dashboard')


# -------- ALL OTHER VIEWS --------
def tech(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/tech.html')


def nontech(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/nontech.html')


def budget(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/budget.html')


def food(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/food.html')


def soundstage(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/soundstage.html')


def photography(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/photography.html')


def decoration(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/decoration.html')


def discipline(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/discipline.html')


def gifts(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/gifts.html')


# -------- NON-TECH --------
def insta(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/insta.html')


def ludo(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/ludo.html')


def chess(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/chess.html')


def lucky(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/lucky.html')


def freefire(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/freefire.html')


def rangoli(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/rangoli.html')


def volleyball(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/volleyball.html')


# -------- TECH --------
def portfolio(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/portfolio.html')


def poster(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/poster.html')


def projectexpo(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/projectexpo.html')


def startup(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/startup.html')


def livecoding(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/livecoding.html')


def debugging(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/debugging.html')


def quiz(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/quiz.html')


def syntax(request):
    if not check_login(request):
        return redirect('login')
    return render(request, 'sections/syntax.html')