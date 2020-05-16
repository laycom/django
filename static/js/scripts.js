$(document).ready(function() {
    var form = $('#form_buying_product');


    function basketUpdate(product_id, nbr, is_delete) {
        var data = {};
        data.product_id = product_id;
        data.nbr = nbr;
        var csrf_token = $('#token_form [name="csrfmiddlewaretoken"]').val();
        data['csrfmiddlewaretoken'] = csrf_token;


        if (is_delete){
            data["is_delete"] = true;
        }

        console.log(data)
        var url = '/orders/basket_adding/';
        console.log(url);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function(data) {
                console.log('OK');
                if (data.products_total_number || data.products_total_number == 0) {
                     $('#basket_total_nbr').text(' (' + data.products_total_number + ')');
                     console.log(data.products);
                     $('.basket-items ul').html('');
                     $.each(data.products, function(k ,v){
                                $('.basket-items ul').append('<li>' + v.name + ", " + v.nbr + " шт. " +
                                   v.price_per_item + ' RUB ' +
                                   '<a class="delete-item" href="" data-product_id="'+v.id+'">x</a>'+
                                   '</li>');
                     });
                };
            },
            error: function() {
                console.log('error')
            }
        })
    }

    form.on('submit', function(e){
        e.preventDefault();
        var nbr = $('#number').val();
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product_id');
        var product_name = submit_btn.data('product_name');
        var product_price = submit_btn.data('product_price');
        basketUpdate(product_id, nbr, is_delete=false)
    });

    function showing_basket() {
        $('.basket-items').toggleClass('invisible');
    }

    $('.basket-container').click(function(e){
        e.preventDefault();
        showing_basket()
    })

    $('.basket-btn').click(function(e){
        e.preventDefault();
        var nbr = 1;
        var product_id = $(this).attr('data-product_id');
        var product_name = $(this).attr('data-product_name');
        var product_price = $(this).attr('data-product_price');
        basketUpdate(product_id, nbr, is_delete=false)
    })

//    $('.basket-container').mouseover(function(){
//        showing_basket()
//    })
//    $('.basket-container').mouseout(function(){
//        showing_basket()
//    })

    $(document).on('click', '.delete-item', function(e){
         e.preventDefault();
         product_id = $(this).data("product_id");
         nbr = 0;
         basketUpdate(product_id, nbr, is_delete=true);
     })

    function calculatingBasketAmount(){
        var total_order_price = 0;
        $('.price-for-all-product').each(function() {
            total_order_price = total_order_price + parseFloat($(this).text());
        });
        $('#total-order-price').text(total_order_price);
    };


    $(document).on('click', '.product-in-basket-number', function(){
        var current_number = $(this).val();
        var current_tr = $(this).closest('tr');
        var current_price = parseInt(current_tr.find('.product-price').text());
        var total_price = current_number * current_price;
        current_tr.find('.price-for-all-product').text(total_price);

        calculatingBasketAmount();

    });



});