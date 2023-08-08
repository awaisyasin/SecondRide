from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .form import AdForm
from .models import *

# Create your views here.

def HomeView(request):
    brands = Brand.objects.all()
    models = Model.objects.all()
    ads = Ad.objects.all().order_by("-id")

    brand_filter = request.GET.get('brand')
    model_filter = request.GET.get('model')
    date_filter = request.GET.get('date')

    if brand_filter:
        ads = ads.filter(model__brand_id=brand_filter)

    if model_filter:
        ads = ads.filter(model_id=model_filter)

    if date_filter:
        ads = ads.filter(published_at__date=date_filter)

    return render(request, "Ads/home.html", {"ads": ads, "brands": brands, "models": models})

@login_required
def AdView(request):
    if request.method == "POST":
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Ads:home")
    else:
        form = AdForm()

    return render(request, "Ads/form.html", {"form": form})

def AdDetailView(request, ad_id):
    ad = Ad.objects.get(id=ad_id)
    form = AdForm(instance=ad)
    return render(request, "Ads/adDetail.html", {"ad": ad, "form": form})