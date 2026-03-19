from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, CustomUserLoginForm, EmailForm, SetNewPasswordForm
from django.contrib import messages
from .models import CustomUser
from django.utils.http import urlsafe_base64_encode
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from .util import save_custom_image
from django.utils.http import urlsafe_base64_decode

# Create your views here.
# Create your views here.
def register(request):
    if request.method == 'POST':
        # print("---Зберігаємо дані користувача---")
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                if 'email' in form.cleaned_data:
                    user.username = form.cleaned_data['email']
                if 'image' in request.FILES:
                    image = request.FILES.get("image")
                    user.image_small = save_custom_image(image, size=(300,300), folder="small")
                    user.image_medium = save_custom_image(image, size=(800,800), folder="medium")
                    user.image_large = save_custom_image(image, size=(1200,1200), folder="large")
                user.save()
                login(request, user)
                return redirect('homepage')
            except Exception as e:
                messages.error(request, f"Щось пішло не так: {str(e)}")
        else:
            messages.success(request, 'Виправте помилки у формі')
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {"form": form})

def user_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data = request.POST)
        if form.is_valid():
            user = authenticate(request, username = form.cleaned_data['username'],
                                password = form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('homepage')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})
def user_logout(request):
    logout(request)
    return redirect('homepage')

def password_reset_request(request):

    if request.method == "POST":
        form = EmailForm(request.POST)


        if form.is_valid():

            email = form.cleaned_data["email"]

            try:
                user = CustomUser.objects.get(email=email)

                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)

                reset_link = request.build_absolute_uri(
                    reverse("users:password_reset_confirm", args=[uid, token])
                )
                print(f"Click the link to reset password:\n{reset_link}")
                send_mail(
                    "Password reset",
                    f"Click the link to reset password:\n{reset_link}",
                    None,
                    [email]
                )


            except CustomUser.DoesNotExist:
                pass

    else:
        form = EmailForm()

    return render(request, "password_reset_request.html", {"form": form})

def password_reset_confirm(request, uidb64, token):

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = CustomUser.objects.get(pk=uid)
    except:
        user = None

    if user and default_token_generator.check_token(user, token):

        if request.method == "POST":
            form = SetNewPasswordForm(request.POST)

            if form.is_valid():
                user.set_password(form.cleaned_data["password1"])
                user.save()

                return redirect("users:user_login")

        else:
            form = SetNewPasswordForm()

        return render(request, "password_reset_confirm.html", {"form": form})

    return render(request, "invalid_link.html")