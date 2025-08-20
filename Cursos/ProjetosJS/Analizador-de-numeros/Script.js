let num = document.querySelector('input#fnum')
let lista = document.querySelector('select#flista')
let res = document.querySelector('div#res')
let valores = []

function isNumero(n) {
    if (Number(n) >= 1 && Number(n) <= 100) {
        return true
    }
}

function inLista(n, l) {
    if (l.indexOf(Number(n)) != -1) {
        return true
    } else {
        return false
    }
}

function Adicionar() {

    if (isNumero(num.value) && !inLista(num.value, valores)) {
        valores.push(Number(num.value))
        let item = document.createElement('option')
        item.text = `Valor ${num.value} adicionado.`
        lista.appendChild(item)
        res.innerHTML = ''
    } else {
        window.alert('Valor inválido ou já encontrado na lista!')
    }
    num.value = ''
    num.focus()
}

function Finalizar() {
    if (valores.length == 0) {
        window.alert('Adicione valores ao vetor')
    } else {
        let tot = valores.length
        let maior = valores [0]
        let menor = valores [0]
        let soma = 0
        let media = 0
        for (let pos in valores) {
            if (valores[pos] < maior)
                maior = valores[pos]
            
            if (valores[pos] > menor)
                menor = valores[pos]
            
            soma += valores[pos]
        }
        media = soma/tot

        res.innerHTML = ''
        res.innerHTML += `<p>Ao todo, temos ${tot} numeros cadastrados</p>`
        res.innerHTML += `<p>Maior valor ${maior}</p>`
        res.innerHTML += `<p>Maior valor ${menor}</p>`
        res.innerHTML += `<p>A soma dos valores é ${soma}</p>`
        res.innerHTML += `<p>A media dos valores é ${media}</p>`
    }
}