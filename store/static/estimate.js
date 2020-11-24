function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// const csrftoken = getCookie('csrftoken');

const searchform = document.querySelector('#search');

if (searchform){
    const estimate = document.querySelector('#estimate');
    estimate.onclick = function(event) {
        event.preventDefault()
        console.log("hello");
        var car_name = document.querySelector("#car_name").value;
        var image = document.querySelector("#image").value;
        var purchase_year = document.querySelector("#purchase_year").value;
        var ex_price = document.querySelector("#ex_price").value;
        var kms_driven = document.querySelector("#kms_driven").value;
        var no_owners = document.querySelector("#no_owners").value;
        var fuel_type = document.querySelector("#fuel_type").value;
        var seats = document.querySelector("#seats").value;
        var transmission = document.querySelector("#transmission").value;
        var estimated_price = document.querySelector("#estimated_price");
        var seller_type = document.querySelector("#seller_type").value;

    const req = new Request( 
          "/estimate",
          {headers: {"X-CSRFToken": getCookie("csrftoken")}}
        );
        fetch(req, {
            method: "PUT",
            mode: "same-origin", 
            body: JSON.stringify({
                  purchase_year : purchase_year,
                  ex_price : ex_price,
                  kms_driven: kms_driven,
                  no_owners: no_owners,
                  fuel_type: fuel_type,
                  transmission: transmission,
                  seller_type: seller_type,
                  seats: seats
            })
          })
        .then(response => response.json())
        .then(data => {
          if (data.status == 200){
            console.log(data.message);
            message = data.message + " " + 'lakh';
            estimated_price.innerText = message;
          }
          else {
            console.log("error");
          }
        });
    }
}   

