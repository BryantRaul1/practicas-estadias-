// Registro - register

var register = function(nombre,password,repeat_password){
    document.querySelector('[href="/register"]').click();
    document.querySelector('[name="username"]').value = nombre;
    document.querySelector('[name="password"]').value = password;
    document.querySelector('[name="repeat_password"]').value = repeat_password;
    document.querySelector('button.btn').click();
}

//Login - login

var login = function(nombre,password){
    document.querySelector('[href="/login"]').click();
    document.querySelector('[name="username"]').value = nombre;
    document.querySelector('[name="password"]').value = password;
    document.querySelector('button.btn').click();
}

//Contacto - contact

var contact = function(nombre,email,mensaje){
    document.querySelector('[href="/contact"]').click();
    document.querySelector('[name="name"]').value = nombre;
    document.querySelector('[name="email"]').value = email;
    document.querySelector('[name="message"]').value = mensaje;
    document.querySelector('button.btn').click();
}

//Crear cancion - Song

//Dar click en Songs
    document.querySelector('[href="/songs"]').click();

//Dar click en link de crear cancion
    document.querySelector('[href="/songs/new"]').click();

//Creacion de cancion
var songs = function(artista,pais,cancion,duracion,letra){
    document.querySelector('[name="artist"]').value = artista;
    document.querySelector('[name="country"]').value = pais;
    document.querySelector('[name="title"]').value = cancion;
    document.querySelector('[name="duration"]').value = duracion;
    document.querySelector('[name="lyrics"]').value = letra;
    document.querySelector('button.btn').click();
}

//Dar like

    document.querySelector('[class="glyphicon glyphicon-thumbs-up"]').click();

//Editar Cancion

//Entrar al link de editar
    document.querySelector('[href="/songs/6/edit"]').click();

//editado exitosamente
var editsongs = function(artista,pais,cancion,duracion,letra){
    document.querySelector('[name="artist"]').value = artista;
    document.querySelector('[name="country"]').value = pais;
    document.querySelector('[name="title"]').value = cancion;
    document.querySelector('[name="duration"]').value = duracion;
    document.querySelector('[name="lyrics"]').value = letra;
    document.querySelector('button.btn').click();
}

//Eliminar cancion

    document.querySelector('[href="/songs/6/delete"]').click();

//Regresar a pantalla de inicio

    document.querySelector('[href="/songs"]').click();

//Cerrar sesion

    document.querySelector('[href="/logout"]').click();