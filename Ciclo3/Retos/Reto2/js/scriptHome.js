/* Reto 2 MisionTIC 2022 - Ciclo 3

Desarrollado por Brayan Buitrago

8/10/2021
*/

const endpntAudience = "https://g3589e9cf1bb538-db202109232148.adb.sa-saopaulo-1.oraclecloudapps.com/ords/admin/audience/audience";
const endpntClient = "https://g3589e9cf1bb538-db202109232148.adb.sa-saopaulo-1.oraclecloudapps.com/ords/admin/client/client";
const endpntMessage = "https://g3589e9cf1bb538-db202109232148.adb.sa-saopaulo-1.oraclecloudapps.com/ords/admin/message/message";

//All buttons in the home page
const btnGetAudience = document.getElementById("audience__btn--get");
const btnGetClient = document.getElementById("client__btn--get");
const btnGetMessage = document.getElementById("message__btn--get");
const btnPostAudience = document.getElementById("audience__btn--post");
const btnPostClient = document.getElementById("client__btn--post");
const btnPostMessage = document.getElementById("message__btn--post");
const btnPutAudience = document.getElementById("audience__btn--put");
const btnPutClient = document.getElementById("client__btn--put");
const btnPutMessage = document.getElementById("message__btn--put");
const btnDeleteAudience = document.getElementById("audience__btn--delete");
const btnDeleteClient = document.getElementById("client__btn--delete");
const btnDeleteMessage = document.getElementById("message__btn--delete");
//Container for the tables that present the data
const tblAudience = document.getElementById("audience__table");
const tblClient = document.getElementById("client__table");
const tblMessage = document.getElementById("message__table");
//Text inputs in the forms
const inputAudienceId = document.getElementById("audience__txtfield--id");
const inputAudienceOwner = document.getElementById("audience__txtfield--owner");
const inputAudienceCapacity = document.getElementById("audience__txtfield--capacity");
const inputAudienceCategory = document.getElementById("audience__txtfield--category-id");
const inputAudienceName = document.getElementById("audience__txtfield--name");
const inputClientId = document.getElementById("client__txtfield--id");
const inputClientName = document.getElementById("client__txtfield--name");
const inputClientEmail = document.getElementById("client__txtfield--email");
const inputClientAge = document.getElementById("client__txtfield--age");
const inputMessageId = document.getElementById("message__txtfield--id");
const inputMessageText = document.getElementById("message__txtfield--text-message");


function cleanTextFields(endpoint){
    const objective = endpoint.split("/")
    const type = objective[objective.length-1];

    switch (type) {
        case "audience":
                document.getElementById("audience__txtfield--id").value = "";
                document.getElementById("audience__txtfield--owner").value = "";
                document.getElementById("audience__txtfield--capacity").value = "";
                document.getElementById("audience__txtfield--category-id").value = "";
                document.getElementById("audience__txtfield--name").value = "";
            break;
        case "client":
                document.getElementById("client__txtfield--id").value = "";
                document.getElementById("client__txtfield--name").value = "";
                document.getElementById("client__txtfield--email").value = "";
                document.getElementById("client__txtfield--age").value = "";
            break;
        case "message":
                inputMessageId.value = "";
                inputMessageText.value = "";
            break; 
        default:
            break;
            
    }
}

function createUrl(object, type){
    return "<a href='detalle.html?type=" + type + "&id=" + object.id + "'>" + object.id +"</a>"
}

function presentInfo(itemsList, type){
    let table = "<table class='table'>"
    switch (type) {
        case "audience":
            table += "<tr> <th>Id</th> <th>Name</th> <th>Owner</th> <th>Capacity</th> <th>Category_id</th></tr>"
            itemsList.forEach(item => {
                table+= "<tr> <td>"+ createUrl(item, type) + "</td>" +
                        "<td>"+ item.name + "</td>" +
                        "<td>"+ item.owner + "</td>" +
                        "<td>"+ item.capacity + "</td>" +
                        "<td>"+ item.category_id + "</td>" +
                        "</tr>"
            });
            break;
        case "client":
            table += "<tr class='table'> <th>Id</th> <th>Name</th> <th>Email</th> <th>Age</th> </tr>"
            itemsList.forEach(item => {
                table+= "<tr> <td>"+ createUrl(item, type) + "</td>" +
                        "<td>"+ item.name + "</td>" +
                        "<td>"+ item.email + "</td>" +
                        "<td>"+ item.age + "</td>" +
                        "</tr>"
            });
            break;
        case "message":
            table += "<tr class='table'> <th>Id</th> <th>Message</th> </tr>"
            itemsList.forEach(item => {
                table+= "<tr> <td>"+ createUrl(item, type) + "</td>" +
                        "<td>"+ item.messagetext+ "</td>" +
                        "</tr>"
            });
            break;
        default:
            break;
    }
    table += "</table>"
    return table
}

function getMethod(endpoint){
    let container = null
    const objective = endpoint.split("/")
    const type = objective[objective.length-1];
    switch (type) {
        case "audience":
            container = tblAudience;
            break;
        case "client":
            container = tblClient;
            break;
        case "message":
            container = tblMessage;
            break;
        default:
            break;
    }

    $.ajax({
        method: "GET",
        url: endpoint,
        dataType: "JSON",
        contentType: "application/json",
        success: function (data){
            container.innerHTML = presentInfo(data.items, type);
        }
    })
}

function postMethod(endpoint){
    const objective = endpoint.split("/")
    const type = objective[objective.length-1];
    let data = {}
    switch (type) {
        case "audience":
            data = {
                id: inputAudienceId.value,
                owner: inputAudienceOwner.value,
                capacity: inputAudienceCapacity.value,
                category_id: inputAudienceCategory.value,
                name: inputAudienceName.value
            }
            break;
        case "client":
            data = {
                id: inputClientId.value,
                name: inputClientName.value,
                email: inputClientEmail.value,
                age: inputClientAge.value
            }
            break;
        case "message":
            data = {
                id: inputMessageId.value,
                messagetext: inputMessageText.value
            }
            break; 
        default:
            break;
            
    }

    let dataSend = JSON.stringify(data)

    $.ajax({
        method: "POST",
        url: endpoint,
        data: dataSend,
        dataType: "JSON",
        contentType: "application/json",
        success:function(response){
            console.log(response)
        },
        complete: function(xhr, status){
            alert("Registro Exitoso");
            getMethod(endpoint)
            cleanTextFields(endpoint)
        }
    })
    
}

function putMethod(endpoint){
    const objective = endpoint.split("/")
    const type = objective[objective.length-1];
    let data = {}
    switch (type) {
        case "audience":
            data = {
                id: inputAudienceId.value,
                owner: inputAudienceOwner.value,
                capacity: inputAudienceCapacity.value,
                category_id: inputAudienceCategory.value,
                name: inputAudienceName.value
            }
            break;
        case "client":
            data = {
                id: inputClientId.value,
                name: inputClientName.value,
                email: inputClientEmail.value,
                age: inputClientAge.value
            }
            break;
        case "message":
            data = {
                id: inputMessageId.value,
                messagetext: inputMessageText.value
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
            getMethod(endpoint)
            cleanTextFields(endpoint)
        }
    })
}

function deleteMethod(endpoint){
    const objective = endpoint.split("/")
    const type = objective[objective.length-1];
    let data = {}
    switch (type) {
        case "audience":
            data = {
                id: inputAudienceId.value
            }
            break;
        case "client":
            data = {
                id: inputClientId.value
            }
            break;
        case "message":
            data = {
                id: inputMessageId.value
            }
            break; 
        default:
            break;
            
    }

    let dataSend = JSON.stringify(data)

    $.ajax({
        method: "DELETE",
        url: endpoint,
        data: dataSend,
        dataType: "JSON",
        contentType: "application/json",
        success:function(response){
            console.log(response)
        },
        complete: function(xhr, status){
            alert("Eliminación Exitosa");
            getMethod(endpoint)
            cleanTextFields(endpoint)
        }
    })
}



//--------Event listeners for the respectives buttons
//Get Buttons
btnGetAudience.addEventListener("click", (e) => {
    e.preventDefault()
    getMethod(endpntAudience)
})
btnGetClient.addEventListener("click", (e) => {
    e.preventDefault()
    getMethod(endpntClient)
})
btnGetMessage.addEventListener("click", (e) => {
    e.preventDefault()
    getMethod(endpntMessage)
})
//Post Buttons
btnPostAudience.addEventListener("click", (e) => {
    e.preventDefault()
    postMethod(endpntAudience)
})
btnPostClient.addEventListener("click", (e) => {
    e.preventDefault()
    postMethod(endpntClient)
})
btnPostMessage.addEventListener("click", (e) => {
    e.preventDefault()
    postMethod(endpntMessage)
})
//Put Buttons
btnPutAudience.addEventListener("click", (e) => {
    e.preventDefault()
    putMethod(endpntAudience)    
})
btnPutClient.addEventListener("click", (e) => {
    e.preventDefault()
    putMethod(endpntClient)
})
btnPutMessage.addEventListener("click", (e) => {
    e.preventDefault()
    putMethod(endpntMessage)
})
//Delete Buttons
btnDeleteAudience.addEventListener("click", (e) => {
    e.preventDefault()
    deleteMethod(endpntAudience)
})
btnDeleteClient.addEventListener("click", (e) => {
    e.preventDefault()
    deleteMethod(endpntClient)
})
btnDeleteMessage.addEventListener("click", (e) => {
    e.preventDefault()
    deleteMethod(endpntMessage)
})