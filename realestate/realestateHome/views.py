from django.shortcuts import render, redirect, HttpResponse
from .models import forSale, forRent, sellers
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'home.html')

def forsale(request):
    if request.method == 'POST':
        searched_city = request.POST['searched_city']

        if forSale.objects.filter(propertyCity = searched_city).exists():
            sellingProperties = forSale.objects.filter(propertyCity=searched_city)
            return render(request, 'forsale.html', {'sellingProperties': sellingProperties})
        else:
            messages.info(request, 'Search not found')
            sellingProperties = forSale.objects.all()
            return render(request, 'forsale.html', {'sellingProperties': sellingProperties})

    else:
        sellingProperties = forSale.objects.filter()

        # add_forSale()

        return render(request, 'forsale.html', {'sellingProperties': sellingProperties})

def forrent(request):
    if request.method == 'POST':
        searched_city = request.POST['searched_city']

        if forRent.objects.filter(propertyCity=searched_city).exists():
            rentingProperties = forSale.objects.filter(propertyCity=searched_city)
            return render(request, 'forrent.html', {'rentingProperties': rentingProperties})
        else:
            messages.info(request, 'Search not found')
            rentingProperties = forrent.objects.all()

            return render(request, 'forrent.html', {'rentingProperties': rentingProperties})
    else:
        rentingProperties = forRent.objects.all()

        # add_forRent()

        return render(request, 'forrent.html', {'rentingProperties': rentingProperties})


def toSell(request):
    if request.method == 'POST':
        propertyName = request.POST['propertyName']
        propertyType = request.POST['propertyType']
        propertyDesc = request.POST['propertyDesc']
        propertyCity = request.POST['propertyCity']
        propertyOwner = request.user.first_name
        businessType = request.POST['businessType']
        propertyPrice = request.POST['propertyPrice']
        ownerContact = request.POST['ownerContact']
        image = request.POST['image']

        seller = sellers(propertyName=propertyName, propertyType=propertyType, propertyDesc=propertyDesc, propertyCity=propertyCity, propertyOwner=propertyOwner, businessType=businessType, propertyPrice=propertyPrice, ownerContact=ownerContact, image=image)
        seller.save()



        return render(request, 'tosell2.html')

    else:
        return render(request, 'tosell.html')


def details(request, myid):
    property = forSale.objects.filter(id=myid)
    return render(request, 'details.html', {'property':property[0]})

def details2(request, myid):
    property = forRent.objects.filter(id=myid)
    return render(request, 'details2.html', {'property':property[0]})


def sold(request):
    return render(request, 'sold.html')


def add_forSale():
    addingProperties = sellers.objects.all()

    for addingProperty in addingProperties:

        if addingProperty.businessType == 'sell':
            propertyName = addingProperty.propertyName
            propertyType = addingProperty.propertyType
            propertyDesc = addingProperty.propertyDesc
            propertyCity = addingProperty.propertyCity
            propertyOwner = addingProperty.propertyOwner
            propertyPrice = addingProperty.propertyPrice
            ownerContact = addingProperty.ownerContact
            image = addingProperty.image

            if forSale.objects.filter(propertyName=propertyName).exists():
                pass
            else:
                property1 = forSale(propertyName=propertyName, propertyType=propertyType, propertyDesc=propertyDesc, propertyCity=propertyCity, propertyOwner=propertyOwner, propertyPrice=propertyPrice, ownerContact=ownerContact, image=image )
                property1.save()



def add_forRent():
    addingProperties = sellers.objects.all()

    for addingProperty in addingProperties:

        if addingProperty.businessType == 'rent':
            propertyName = addingProperty.propertyName
            propertyType = addingProperty.propertyType
            propertyDesc = addingProperty.propertyDesc
            propertyCity = addingProperty.propertyCity
            propertyOwner = addingProperty.propertyOwner
            propertyRent = addingProperty.propertyPrice
            ownerContact = addingProperty.ownerContact
            image = addingProperty.image

            if forRent.objects.filter(propertyName=propertyName).exists():
                pass
            else:
                property1 = forRent(propertyName=propertyName, propertyType=propertyType, propertyDesc=propertyDesc, propertyCity=propertyCity, propertyOwner=propertyOwner, propertyRent=propertyRent, ownerContact=ownerContact, image=image )
                property1.save()


