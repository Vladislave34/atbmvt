from django.shortcuts import render, redirect

from categories.forms import CategoryForm
from categories.utils import save_image
from categories.models import Category


# Create your views here.
def add_category(request):

    if request.method == 'POST':

        form = CategoryForm(request.POST, request.FILES)

        if form.is_valid():

            category = form.save(commit=False)

            if 'image' in request.FILES:

                image = request.FILES.get("image")
                category.image_medium = save_image(image, size=(800, 800), folder="medium")


            category.save()

            return redirect('/')

    else:
        form = CategoryForm()

    return render(request, 'add_form.html', {'form': form})

def categories_list(request):

    categories = Category.objects.all()

    return render(request, "categories_list.html", {
        "categories": categories
    })
