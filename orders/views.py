from django.shortcuts import render
from .models import ProductInBasket
from django.http import JsonResponse


def basket_adding(request):
    return_dict = {}
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get('product_id')
    nbr = data.get('nbr')
    is_delete = data.get('is_delete')
    print(data)


    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key,  is_active=True,
                                                                     product_id=product_id, defaults={'nbr': nbr})
        if not created:
            new_product.nbr += int(nbr)
            new_product.save(force_update=True)

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    products_total_number = products_in_basket.count()
    return_dict['products_total_number'] = products_total_number

    return_dict['products'] = []
    for item in products_in_basket:
        products_dict = {}
        products_dict['id'] = item.id
        products_dict['name'] = item.product.name
        products_dict['price_per_item'] = item.price_per_item
        products_dict['nbr'] = item.nbr
        return_dict['products'].append(products_dict)
    return JsonResponse(return_dict)
