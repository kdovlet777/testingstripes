from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import stripe
from items.models import Item
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def buy_item(request, id):
    item = Item.objects.get(pk=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
        'price_data' :{
            'product_data':{
                'name': item.name,
            },
            #'description': item.description,
            'unit_amount': item.price,
            'currency': 'usd',
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success/',
        cancel_url='http://localhost:8000/cancel/',
    )
    return JsonResponse({'sessionId': session.id})

def item_detail(request, id):
    item = Item.objects.get(pk=id)
    return render(request, 'item.html', {
        'item': item,
        'stripe_public_key':settings.STRIPE_PUBLIC_KEY
        })