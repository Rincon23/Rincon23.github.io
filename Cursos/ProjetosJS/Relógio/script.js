function carregar(){
    var msg = document.querySelector('h1#msg')
    var boa = document.getElementById('boa')
    var img = document.getElementById('img')
    var data = new Date()
    var hora = data.getHours()
    msg.innerHTML = `Agora são ${hora} horas!`

    if (hora >= 6 && hora < 12) {
        img.src = "Img/Manha.jpg"
        boa.innerHTML = 'Bom dia!'
        document.body.style = 'background-color:#D5B162'
    } else if (hora >= 12 && hora < 18) {
        img.src = "Img/Tarde.jpg"
        boa.innerHTML = 'Boa Tarde!'
        document.body.style = 'background-color:#AE704B'
    } else {
        img.src = "Img/Noite.jpg"
        boa.innerHTML = 'Boa Noite!'
        document.body.style = 'background-color:#30383B'
    }


}



