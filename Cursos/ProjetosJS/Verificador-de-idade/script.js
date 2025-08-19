function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var anodenas = document.getElementById('anodenas')
    var res = document.getElementById('res')
    if (anodenas.value.length == 0 || anodenas.value.length > ano) {
        alert('Verifique os dados e tente novamente')
    } else {
        var sex = document.getElementsByName('sex')
        var idade = ano - Number(anodenas.value)
        var gen = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (gen = sex[0].checked) {
            sex = 'masculino'
            if (idade >= 0 && idade <= 13) {
                img.setAttribute('src', './img/bebe homem.png')
            } else if (idade >= 14 && idade <= 21) {
                img.setAttribute('src', './img/adolecente homem.png')
            } else if (idade >= 18 && idade <= 60) {
                img.setAttribute('src', './img/Homem.png')
            } else {
                img.setAttribute('src', './img/velho.png')
            }

        } else {
            sex = 'feminino'
            if (idade >= 0 && idade <= 13) {
                img.setAttribute('src', './img/bebe mulher.png')
            } else if (idade >= 14 && idade <= 17) {
                img.setAttribute('src', './img/adolecente mulher.png')
            } else if (idade >= 18 && idade <= 60) {
                img.setAttribute('src', './img/Mulher.png')
            } else {
                img.setAttribute('src', './img/velha.png')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${sex} com ${idade} anos`
        res.appendChild(img)
        img.style.borderRadius = '50%'
        img.style.width = '200px'  
        img.style.height = '200px'
        
    } 


} 
