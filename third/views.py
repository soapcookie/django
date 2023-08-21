from django.shortcuts import render, get_object_or_404, redirect
from third.models import Restaurant, Review
from django.core.paginator import Paginator
from third.forms import RestaurantForm, ReviewForm
from django.http import HttpResponseRedirect

def list(request):
    restaurants = Restaurant.objects.all()
    paginator = Paginator(restaurants, 5)

    page = request.GET.get('page')
    items = paginator.get_page(page)

    context = {
        'restaurants': items
    }
    return render(request, 'third/list.html', context)

def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            new_item = form.save()
            return HttpResponseRedirect('/third/list/')
    else:
        form = RestaurantForm()
    return render(request, 'third/create.html', {'form': form})

def update(request):
    if request.method == 'POST' and 'id' in request.POST:
        item = get_object_or_404(Restaurant, pk=request.POST.get('id'))
        form = RestaurantForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return HttpResponseRedirect('/third/list/')
    elif request.method == 'GET':
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        form = RestaurantForm(instance=item)
        return render(request, 'third/update.html', {'form': form})
    return HttpResponseRedirect('/third/list/')


def detail(request, id):
    if id is not None:
        item = get_object_or_404(Restaurant, pk=id)
        reviews = Review.objects.filter(restaurant=item).all()  # Review.objects로 수정
        return render(request, 'third/detail.html', {'item': item, 'reviews': reviews})
    return HttpResponseRedirect('/third/list/')


def delete(request):
    if 'id' in request.GET:
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        item.delete()
    return HttpResponseRedirect('/third/list/')


def review_create(request, restaurant_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)  #
        if form.is_valid():  # 데이터가 form 클래스에서 정의한 조건 (max_length 등)을 만족하는지 체크합니다.
            new_item = form.save()  # save 메소드로 입력받은 데이터를 레코드로 추가합니다.
        return redirect('restaurant-detail', id=restaurant_id)  # 전화면으로 이동합니다.

    item = get_object_or_404(Restaurant, pk=restaurant_id)
    form = ReviewForm(initial={'restaurant': item})
    return render(request, 'third/review_create.html', {'form': form, 'item':item})


def review_delete(request, restaurant_id, review_id):
    item = get_object_or_404(Review, pk=review_id)
    item.delete()

    return redirect('restaurant-detail', id=restaurant_id)  # 전 화면으로 이동합니다.
