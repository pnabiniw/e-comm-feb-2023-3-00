var updateBtns = document.getElementsByClassName("update-cart")

for(var i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function (){
        var productId = this.dataset.product
        var action = this.dataset.action
        if (user === "AnonymousUser"){
            console.log("Unauthenticated user")
        }
        else{
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log('User logged in. Sending data...')
    var url = '/update-item/'
    fetch(url, {
        method: "POST",
        headers:{
            "Content-Type": "application/json",
            'X-CSRFTOKEN': csrftoken
        },
        body: JSON.stringify({
            "productId": productId,
            "action": action
        })
    }).then((response) =>{
        return response.json()
    }).then((data) =>{
        console.log('data: ', data)
    })
}
