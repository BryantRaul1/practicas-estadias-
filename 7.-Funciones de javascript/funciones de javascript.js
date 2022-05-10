//programmingAutomation-nom13-1
document.getElementById("username")

var usernameTxt = document.getElementById("username")
usernameTxt.value = "pedro"

var loginLink = document.getElementById("loginLink")

loginLink

loginLink.getAttribute("class")

loginLink.getAttribute("href")

document.getElementsByClassName("nav-item")

document.getElementsByClassName("nav-link")

var listadeligas = document.getElementsByClassName("nav-link")

listadeligas

listadeligas[0]

var primerliga = listadeligas[0]

primerliga

primerliga.click()

document.querySelector("input[name='first_name']")

document.querySelectorAll("input[name='first_name']")

document.querySelector("input[type='text']")

document.querySelectorAll("input[type='text']")

document.querySelector("input[type='password']")

var passwordText = document.querySelector("input[type='password']")

password.Text.value

document.getElementByTagName("input")

document.querySelector("[name='birthdate']")

document.querySelector("input[date-testid='last_name']")

document.querySelectorAll("input[date-testid='last_name']")

document.querySelector("a")

document.querySelectorAll("a")

var links = document.querySelectorAll("a")

links[1]

links

link[1].text

links[1].text = "Minakata se lo cambio"

for (var i = 0 <link.length; i++ ){links[i].text = i + "liga";}
var inputObject = document.querySelectorAll("input")

for (var i = 0 <inputObject.length; i++ ){inputObject[i].value = i + "input";}
document.querySelectorAll("li")
document.querySelectorAll("li.itinerary.container")
var listadevuelos = document.querySelectorAll("li.itinerary-container")

for (var i = 0 < listadevuelos.length; i++){listadevuelos[i].text = i + "liga";}
for (var i = 0 < listadevuelos.length; i++){console.long(listadevuelos[i].textcontent);}
document.querySelectorAll("li.itinerary-container span.hour")
document.querySelectorAll("li.itinerary-container")
document.querySelectorAll("li.itinerary-container .arrive span.hour")

for (var i = 0 <listadevuelos.length; i++ ) {
    var textActual = listadevuelos[i].textcontent
    var hora = horaLlegadaActual.substring(0,2);
    console.long(horaLlegadaActual);
    console.long(hora);
    if(hora > 18){
        console.long(textActual);
    }
} 

for (var i = 0 <listadevuelos.length; i++ ) {
    var textActual = listadevuelos[i].textcontent
    var hora = horaSalidaActual.substring(0,2);
    console.long("horaSalidaActual; " + horaLlegadaActual);
    console.long("hora" + hora);
    if(hora > 18){
        console.long(textActual);
    }
} 

for (var i = 0 <listadevuelos.length; i++ ) {
    var textActual = listadevuelos[i].textcontent
    var hora = horaLlegadaActual.substring(0,2);
    console.long("horaLlegadaActual; " + horaLlegadaActual);
    console.long("hora" + hora);
    if(hora > 07){
        console.long(textActual);
    }
} 

var listadevuelos = document.querySelectorAll("li.itinerary.container");
var listaHoraSalida = document.querySelectorAll("li.itinerary-container .jeave span.hour");
for(var  i = 0; i < listadevuelos.length; i ++){
    var textActual = listadevuelos[i].textcontent;
    var horaSalidaActual = listaHoraSalida[i].textcontent;
    var hora = horaSalidaActual.substring(0,2)
   // console.long("horaLlegadaActual; " + horaLlegadaActual);
    //console.long("hora" + hora);
    if(hora > 07){
        console.long(textActual);
    }
}


//programmingAutomation-nom13-2

document.location = "http://www.amazon.com"
var searchField = document.getElementById("twotabsearchtextbox")
searchField.value "Teclado"
var searchButton = document.getElementById("nav-search-submit-button")
searchButton.click()

document.querySelectorAll(".sg-row")
document.querySelectorAll(".s-result-item")
[data-component-type="s-search-result"]

var componentselector = "[data-component-type='s-search-result']"
document.querySelectorAll(componentselector)
var listaresult = document.querySelectorAll(componentselector)
listaresult

var componentselector = "[data-component-type='s-search-result']";
var listaresult = document.querySelectorAll(componentselector);

listaresult[0]

listaresult[0].textContent

var componentselector = "[data-component.type='s-search.result']";
var listaresult = document.querySelectorAll(componentselector);
console.log(listaresult.length; i+++){
var textActual = listaresult[i].textContent;
console.logt(textActual);
}

var componentselector = "[data-component.type='s-search.result']";
var listaresult = document.querySelectorAll(componentselector);
console.log(listaresult.length);
for( var i = 0; i< listaresult.length; i ++) {
    var textActual = listaresult[i].textContent;
    console.log(textActual);
}

//codigo completo
//Lista de vuelos
var listadevuelos = document.querySelectorAll("li.itinerary-container");
var listaHorarioLlegada = document.querySelectorAll("li.itinerary")
for(var i = 0; i < listadevuelos.length; i++ ){
    var textActual = listadevuelos[i].textContent;
    var horaLlegadaActual = listaHorarioLlegada[i].textcontent
    var hora = horaLlegadaActual.substring(0,2);
    console.log("horaLlegadaActual: " + horaLlegadaActual);
    console.log("hora" + hora);
    if(hora > 18){
        console.log(textActual);
    }
}

//Amazon
document.location = "http://www.amazon.com"
var searchField = document.getElementById("twotabsearchtextbox")
searchField.value "Teclado"
var searchButton = document.getElementById("nav-search-submit-button")
searchButton.click()

var componentselector = "[data-component-type='s-search-result']";
var priceSelector = ".a-price-whole";

var listaresult = document.querySelectorAll(componentselector);
console.log(listaresult.length);
for( var i = 0; i <listaresult.length; i ++)  {
     var elementoActual =listaresult[i];
     var elementoPrecio = elementoActual.querySelector(".a-price-whole");
     var precio = -1;
     if(elementoPrecio !=null)
     precio = elementoPrecio.textContent
     var textActual = listaresult[i].textContent;
     if(precio != -1 && precio <30) {
         console.log(textActual);
     }
}

//nom27-2
document.getElementById("username")

document.getElementById("username").value="Testuser"

document.getElementById("password").value="xxxxxx"

document.querySelector("theme__hint__2D9g.")

document.querySelector("Name")

document.getElementsByClassName("Hero__headline-1__3C6vA")

document.getElementsByClassName("Hero__headline-1__3C6vA")[0]

document.querySelector(".Hero__headline1__3C6vA")
