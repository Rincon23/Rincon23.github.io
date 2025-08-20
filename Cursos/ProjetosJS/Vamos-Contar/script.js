function Contar() {
    var inicio = document.getElementById('inicio').value
    var fim = document.getElementById('fim').value
    var passo = document.getElementById('passo').value
    resposta = document.getElementById(`res`)

    var respostasantigas = document.querySelectorAll('.resposta');
    respostasantigas.forEach(function (elemento) {
        elemento.remove();
    });

    if (inicio == "" || fim == "" || passo == "") {
        alert(`alguma você não passou alguma informação`)
    } else {
        inicio = Number(inicio)
        fim = Number(fim)
        passo = Number(passo)
        for (var res=inicio;res <= fim;res = res+passo){
            var p = document.createElement('span');
            p.id = `passo-${res}`; 
            p.className = 'resposta'
            p.innerText = `${res} 👉`; 
            resposta.appendChild(p)
        }
        var p = document.createElement('span');
        p.id = `passo-${res+1}`; 
        p.className = 'resposta'
        p.innerText = `🚩`; 
        resposta.appendChild(p)
    }


} 
