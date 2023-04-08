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
})
