from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from .models import Product #Product ==> classe product
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

products = [
        {'name': 'Prodotto 1', 'price': 10},
        {'name': 'Prodotto 2', 'price': 20},
        {'name': 'Prodotto 3', 'price': 30},
        {'name': 'Prodotto 4', 'price': 30},
        {'name': 'Prodotto 5', 'price': 308},
        {'name': 'Prodotto 6', 'price': 309},
        {'name': 'Prodotto 7', 'price': 67},
        {'name': 'Prodotto 8', 'price': 980},
        {'name': 'Prodotto 9', 'price': 680},
        {'name': 'Prodotto 10', 'price': 3},
        {'name': 'Prodotto 11', 'price': 650},
        {'name': 'Prodotto 12', 'price': 30450},
        {'name': 'Prodotto 13', 'price': 1},
        {'name': 'Prodotto 14', 'price': 560},
        {'name': 'Prodotto 15', 'price': 900},
        {'name': 'Prodotto 16', 'price': 90},
        ]

def holla(request):
    return render(request,'store/benvenidos.html')

#ritorna tutti i prodotti disponibili
def product_list(request):
   # products = Product.objects.all()
   #questa è la mia finta database dei prodotti
    return render(request, 'store/product_list.html', {'products': products})



#aggiunto con l'aiuto di chatgpt
def cart_view(request):
    # Supponiamo che tu abbia un modello Carrello con articoli e quantità
    cart = [
        {'product': {'name': 'Prodotto 1', 'price': 10}, 'quantity': 2},
        {'product': {'name': 'Prodotto 2', 'price': 20}, 'quantity': 1},
    ]

    # Calcolare il totale del carrello
    cart_total = sum(item['product']['price'] * item['quantity'] for item in cart)

    return render(request, 'store/cart.html', {'cart': cart, 'cart_total': cart_total})


def analisi(request):
    df = pd.DataFrame(products, columns=['name', 'price'])
    colonna1 = df['name']
    colonna2 = df['price']
    plt.scatter(colonna1, colonna2) 
    plt.xlabel('Nome') 
    plt.ylabel('prezzo_in_euro') 
    plt.title('Grafico a dispersione') 
    
    # Salva il grafico in un oggetto in memoria
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Ritorna il grafico come risposta HTTP (in formato immagine)
    return HttpResponse(buffer, content_type='image/png')
