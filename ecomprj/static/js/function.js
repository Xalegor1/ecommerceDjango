$(document).ready(function (){
    $(".filter-checkbox, #price-filter-btn").on("click", function(){
        console.log("A checkbox have been clicked");
    
        let filter_object = {}

        let min_price = $("#max_price").attr("min")
        let max_price = $("#max_price").val()

        filter_object.min_price = min_price;
        filter_object.max_price = max_price;


        $(".filter-checkbox").each(function(){
            let filter_value = $(this).val()
            let filter_key = $(this).data("filter")

            // console.log("Filter value is:", filter_value);
            // console.log("Filter key is:", filter_key);

            filter_object[filter_key] = Array.from(document.querySelectorAll('input[data-filter=' + filter_key + ']:checked')).map(function(element){
                return element.value
            })
        })
        console.log("Filter object is: ", filter_object);
        $.ajax({
            url: '/filter-products',
            data: filter_object,
            dataType: 'json',
            beforeSend: function(){
                console.log("Sending Data... ");
            },
            success: function(response){
                console.log(response);
                console.log("Data filtred successfully...");
                $("#filtered-product").html(response.data)
            }
        })
    })

    $("#max_price").on("blur", function(){
        let min_price = $(this).attr("min")
        let max_price = $(this).attr("max")
        let current_price = $(this).val()

        // console.log("Current price is: ", current_price);
        // console.log("Max Price is", max_price);
        // console.log("Min Price is: ", min_price);

        if(current_price < parseInt(min_price) || current_price > parseInt(max_price)){
            console.log("Price Error");

            alert("Price Must Be Between $" +min_price + " and $" + max_price)
            $(this).val(min_price) 
            $("#range").val(min_price)
            
            $(this).focus()

            return false
        }

    })
});



/// Add to Cart functionality

$(".button.add-to-cart").on("click", function(){

    let this_val = $(this)
    let index = this_val.attr("data-index")

    let quantity = $(".product-quantity-" + index).val()
    let product_title = $(".product-title-main-" + index).val()

    let product_id = $(".product-id-" + index).val()
    let product_price = $(".current-product-price-" + index).text()

    let product_pid = $(".product-pid-" + index).val()
    let product_image = $(".product-image-" + index).val()

    console.log("Quantity:", quantity);
    console.log("Title:", product_title);
    console.log("Product Price:", product_price);
    console.log("ID:", product_id);
    console.log("PID:", product_pid);
    console.log("Image: ", product_image);
    console.log("Index: ", index);
    console.log("Current Element: ", this_val);

    $.ajax({
        url: '/add-to-cart',
        data: {
            'id': product_id,
            'pid': product_pid,
            'image': product_image,
            'qty': quantity,
            'title': product_title,
            'price': product_price,
        },
        dataType: 'json',
        beforeSend: function(){
            console.log("Adding Product To Cart...");
        },
        success: function(response){
            this_val.html("✓");
            console.log("Added Product To Cart!");
            $("#cart-items-count").text(response.totalcartitems)
            
        }
    })

});
////////
$(".link-ver1.add-cart").on("click", function(){

    let this_val = $(this)
    let index = this_val.attr("data-index")

    let quantity = $(".product-quantity-" + index).val()
    let product_title = $(".product-title-main-" + index).val()

    let product_id = $(".product-id-" + index).val()
    let product_price = $(".current-product-price-" + index).text()

    let product_pid = $(".product-pid-" + index).val()
    let product_image = $(".product-image-" + index).val()

    console.log("Quantity:", quantity);
    console.log("Title:", product_title);
    console.log("Product Price:", product_price);
    console.log("ID:", product_id);
    console.log("PID:", product_pid);
    console.log("Image: ", product_image);
    console.log("Index: ", index);
    console.log("Current Element: ", this_val);

    $.ajax({
        url: '/add-to-cart',
        data: {
            'id': product_id,
            'pid': product_pid,
            'image': product_image,
            'qty': quantity,
            'title': product_title,
            'price': product_price,
        },
        dataType: 'json',
        beforeSend: function(){
            console.log("Adding Product To Cart...");
        },
        success: function(response){
            this_val.html("✓");
            console.log("Added Product To Cart!");
            $("#cart-items-count").text(response.totalcartitems)
            
        }
    })

});


$(".remove").on('click', function(){

    let product_id = $(this).attr("data-product");
    let this_val = $(this)

    console.log("Product ID:", product_id);

    $.ajax({
        url: '/delete-from-cart',
        data: {
            'id': product_id
        },
        dataType: 'json',
        beforeSend: function(){
            this_val.hide()
        },
        success: function(response){
            this_val.show()
            $("#cart-items-count").text(response.totalcartitems)
            $("#cart-list").html(response.data);
        }    
    })

});








// $("#add-to-cart-btn").on("click", function(){

//     let this_val = $(this)
//     let index = this_val.attr("data-index")

//     let quantity = $(".product-quantity-" + index).val()
//     let product_title = $(".product-title-main-" + index).val()

//     let product_id = $(".product-id-" + index).val()
//     let product_price = $(".current-product-price-" + index).text()

//     let product_pid = $(".product-pid-" + index).val()
//     let product_image = $(".product-image-" + index).val()

//     console.log("Quantity:", quantity);
//     console.log("Title:", product_title);
//     console.log("Product Price:", product_price);
//     console.log("ID:", product_id);
//     console.log("PID:", product_pid);
//     console.log("Image: ", product_image);
//     console.log("Index: ", index);
//     console.log("Current Element: ", this_val);

//     $.ajax({
//         url: '/add-to-cart',
//         data: {
//             'id': product_id,
//             'pid': product_pid,
//             'image': product_image,
//             'qty': quantity,
//             'title': product_title,
//             'price': product_price,
//         },
//         dataType: 'json',
//         beforeSend: function(){
//             console.log("Adding Product To Cart...");
//         },
//         success: function(response){
//             this_val.html("✓");
//             console.log("Added Product To Cart!");
//             $("#cart-items-count").text(response.totalcartitems)
            
//         }
//     })

// }) 





// $("#add-to-cart-btn").on("click", function(){
//     let quantity = $("#product-quantity").val()
//     let product_title = $(".product-title").val()
//     let product_id = $(".product-id").val()
//     let product_price = $(".current-product-price").text()
//     let this_val = $(this)

//     console.log("Quantity:", quantity);
//     console.log("Title", product_title);
//     console.log("Product Price:", product_price);
//     console.log("ID:", product_id);
//     console.log("Current Element", this_val);

//     $.ajax({
//         url: '/add-to-cart',
//         data: {
//             'id': product_id,
//             'qty': quantity, 
//             'title': product_title,
//             'price': product_price,
//         },
//         dataType: 'json',
//         beforeSend: function(){
//             console.log("Adding Product To Cart...");
//         },
//         success: function(response){
//             this_val.html("Item Added To Cart");
//             console.log("Added Product To Cart!");
//             $("#cart-items-count").text(response.totalcartitems)

//         }
//     })

// }) 