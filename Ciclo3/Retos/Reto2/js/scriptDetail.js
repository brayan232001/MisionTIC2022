/* Reto 2 MisionTIC 2022 - Ciclo 3

Desarrollado por Brayan Buitrago

9/10/2021
*/

//Api for the database
const endpntAudience = "https://g3589e9cf1bb538-db202109232148.adb.sa-saopaulo-1.oraclecloudapps.com/ords/admin/audience/audience";
const endpntClient = "https://g3589e9cf1bb538-db202109232148.adb.sa-saopaulo-1.oraclecloudapps.com/ords/admin/client/client";
const endpntMessage = "https://g3589e9cf1bb538-db202109232148.adb.sa-saopaulo-1.oraclecloudapps.com/ords/admin/message/message";

//Getting the params in the url
queryString = window.location.search
const urlParams = new URLSearchParams(queryString);


//Method that creates and integrate the inputs to the form in detalle.html
function createForm(data, type) {
    let container = document.getElementById("container__form");
    let inputs = ""; 
    switch (type) {
        case "audience":
            inputs += "\
            <label for='audience__txtfield--id'>Id: \
                <input type='number' id='audience__txtfield--id' value='" + data.id + "'disabled> \
            </label> \
            \
            <label for='audience__txtfield--owner'>Propietario: \
                <input type='text' id='audience__txtfield--owner' value='" + data.owner + "'required> \
            </label> \
            \
            <label for='audience__txtfield--capacity'>Capacidad: \
                <input type='number' id='audience__txtfield--capacity' value='" + data.capacity + "'required> \
            </label> \
            \
            <label for='audience__txtfield--category-id'>Categoria-id: \
                <input type='number' id='audience__txtfield--category-id' value='" + data.category_id + "'required> \
            </label> \
            \
            <label for='audience__txtfield--name'>Nombre:\
                <input type='text' id='audience__txtfield--name' value='" + data.name + "'required>\
            </label>\
            "
            break;
        case "client":
            inputs = "\
                <label for='client__txtfield--id'>Id: \
                    <input type='number' id='client__txtfield--id' value='" + data.id + "'disabled> \
                </label> \
                \
                <label for='client__txtfield--name'>Nombre: \
                    <input type='text' id='client__txtfield--name' value='" + data.name + "'required> \
                </label> \
                \
                <label for='client__txtfield--email'>Email: \
                    <input type='email' id='client__txtfield--email' value='" + data.email + "'required> \
                </label> \
                \
                <label for='client__txtfield--id'>Age: \
                    <input type='number' id='client__txtfield--age' value='" + data.age + "'required> \
                </label> \
            "
            break;
        case "message":
            inputs = "\
            <label for='message__txtfield--id'>Id: \
                    <input type='number' id='message__txtfield--id' value='" + data.id + "'disabled> \
                </label> \
                \
                <label for='message__txtfield--message'>Mensaje: \
                    <input type='text' id='message__txtfield--text-message' value='" + data.messagetext + "'required> \
                </label> \
            "
            break;
        default:
            break;
    }

    container.innerHTML = inputs
}

//Get Method according to a specific id
function getMethod(endpnt){
    let endpoint = endpnt + "/" + urlParams.get("id");

    $.ajax({
        method: "GET",
        url: endpoint,
        dataType: "JSON",
        contentType: "application/json",
        success: function (data){
            console.log(data.items[0])
            createForm(data.items[0], urlParams.get("type"))
            
        }
    })


}

//Method that includes a form in the detail.html according to the variable type
let endpoint = ""

switch (urlParams.get("type")) {
    case "audience":
        endpoint = endpntAudience;
        break;
    case "client":
        endpoint = endpntClient;
        break;
    case "message":
        endpoint = endpntMessage;
        break;
    default:
        break;
}

getMethod(endpoint)

//Put Method
function putMethod(endpoint) {
    const objective = endpoint.split("/")
    const type = objective[objective.length-1];
    let data = {}
    switch (type) {
        case "audience":
            data = {
                id: document.getElementById("audience__txtfield--id").value,
                owner: document.getElementById("audience__txtfield--owner").value,
                capacity: document.getElementById("audience__txtfield--capacity").value,
                category_id: document.getElementById("audience__txtfield--category-id").value,
                name: document.getElementById("audience__txtfield--name").value
            }
            break;
        case "client":
            data = {
                id: document.getElementById("client__txtfield--id").value,
                name: document.getElementById("client__txtfield--name").value,
                email: document.getElementById("client__txtfield--email").value,
                age: document.getElementById("client__txtfield--age").value
            }
            break;
        case "message":
            data = {
                id: document.getElementById("message__txtfield--id").value,
                messagetext: document.getElementById("message__txtfield--text-message").value
            }
            break; 
        default:
            break;
            
    }

    let dataSend = JSON.stringify(data)

    $.ajax({
        method: "PUT",
        url: endpoint,
        data: dataSend,
        dataType: "JSON",
        contentType: "application/json",
        success:function(response){
            console.log(response)
        },
        complete: function(xhr, status){
            alert("Actualización Exitosa");
            window.location.pathname = "index.html";
        }
    })
    /* alert("Actualización exitosa"); */
}

//Reference the button in the form
const btnPut = document.getElementById("container__btn--put");

btnPut.addEventListener("click", (e) =>{
    e.preventDefault()
    putMethod(endpoint)
})