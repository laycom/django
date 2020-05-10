$(document).ready(function() {
    var form = $('#form_buying_product');
    form.on('submit', function(e){
        e.preventDefault();
        var nmr = $('#number').val();
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product_id');
        var product_name = submit_btn.data('product_name');
        var product_price = submit_btn.data('product_price');
        console.log(product_id );
        console.log(name);

        $('.basket-items ul').append('<li>' + product_name + ", " + nmr + " шт." + ', ' +
            "цена: " + product_price + ' RUB ' + '<a class="delete-item" href="">x</a>'+ '</li>');

    });

    function showing_basket() {
        $('.basket-items').toggleClass('invisible');
    }

    $('.basket-container').click(function(e){
        e.preventDefault();
        showing_basket()
    })
//    $('.basket-container').mouseover(function(){
//        showing_basket()
//    })
//    $('.basket-container').mouseout(function(){
//        showing_basket()
//    })

    $(document).on('click', '.delete-item', function(e){
         e.preventDefault();
         $(this).closest('li').remove();
     })
});