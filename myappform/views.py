
from django.shortcuts import render, redirect
from .forms import ProductForm

def upload_product_photo(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('где_то')  
    else:
        form = ProductForm()
    return render(request, 'myappform/upload_product_photo.html', {'form': form})
