function GerarTabuada() {
    let num = document.getElementById("num");
    let tabuada = document.getElementById("tabuada");

    if (num.value.length == 0) {
        alert(`Por favor digite um numero!`)
        
    } else {
        let  n = Number(num.value)
        tabuada.innerHTML = ``
        for(let v = 1;v<=10;v++) {
        let item = document.createElement(`option`)
        item.text = `${n} X ${v} = ${v*n}`
        tabuada.appendChild(item)
    }
    }

    

}
