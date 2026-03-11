





from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)

            if 'image' in request.FILES:
                image = request.FILES.get("image")
                user.image_small = image
                user.image_medium = image
                user.image_big = image

            user.save()
            return redirect('homepage')

        else:
            messages.error(request, 'Виправте помилки у формі')

    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {"form": form})
