from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse
from django.shortcuts import render
from .models import Location,Image,Category


# Create your views here.

def welcome(request):
    images = Image.get_photos()
    return render(request, 'index.html', {"images":images})

def photos_today(request):
    date = dt.date.today()
    return render(request, 'all-photos/today-photos.html', {"date": date,})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_photos(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_of_day)

    return render(request, 'all-photos/past-photos.html', {"date": date})
 
def location(request,location_id):
    photos=Image.objects.filter(location_id=location_id)

    return render(request,'location.html',{"photos":photos})


def category(request,category_id):
    photos=Image.objects.filter(category_id=category_id)

    return render(request,'category.html',{"photos":photos})

def imagedetails(request,image_id):
    try:
        image = Image.objects.get(id=image_id)
    except DoesNotExist:
         raise Http404()
    return render(request,"image.html",{"image":image})

def copy_image(from_model, to_model):
    to_model.image.save(from_model.image.url.split('/')[-1],from_model.image.file,save=True)

# def search_results(request):

#     if 'image' in request.GET and request.GET["image"]:
#         search_term = request.GET.get("image")
#         searched_images = Image.search_by_category(search_term)
#         message = f"{search_term}"

#         return render(request, 'search.html',{"message":message,"images": searched_images})

#     else:
#         message = "You haven't searched for any image"
#         return render(request, 'search.html',{"message":message})