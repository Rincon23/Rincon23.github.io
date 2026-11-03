const VELOCIDADE = 45; // pixels por segundo
let semMovimento = window.matchMedia('(prefers-reduced-motion: reduce)');

function iniciarCarrossel(carrossel) {
    let janela = carrossel.querySelector('.carrossel-janela');
    let trilho = carrossel.querySelector('.carrossel-trilho');
    let originais = [...trilho.children];
    let passo = 0;      // largura de um card mais o espaço até o próximo
    let volta = 0;      // largura de todos os cards originais; depois de andar isso a faixa fica igual ao começo
    let posicao = 0;
    let salto = 0;      // o quanto as setas ainda mandam andar
    let mouseEmCima = false;
    let focoTeclado = false;
    let pressionado = null;   // dedo ou botão do mouse em cima da faixa
    let arrastou = false;
    let quadroPedido = null;
    let anterior = null;
    let ativo = false;        // false quando todos os cards cabem na tela e a faixa fica parada
    let visivel = false;

    // Mede os cards. Se todos cabem na tela, a faixa fica parada e centralizada, sem setas.
    // Se não cabem, põe cópias atrás dos originais até a faixa cobrir a tela mais uma
    // volta inteira, para nunca aparecer um buraco no fim
    function medir() {
        let espaco = parseFloat(getComputedStyle(trilho).columnGap) || 0;
        passo = originais[0].offsetWidth + espaco;
        volta = passo * originais.length;
        let larguraDosCards = volta - espaco;
        ativo = larguraDosCards > janela.clientWidth * 0.92;
        carrossel.classList.toggle('carrossel-estatico', !ativo);

        if (!ativo) {
            desligar();
            [...trilho.children].slice(originais.length).forEach((copia) => copia.remove());
            posicao = 0;
            salto = 0;
            trilho.style.transform = '';
            return;
        }

        let copias = trilho.children.length / originais.length;
        while (copias * volta < janela.clientWidth + volta) {
            for (let card of originais) {
                let copia = card.cloneNode(true);
                copia.setAttribute('aria-hidden', 'true');
                copia.setAttribute('tabindex', '-1');
                trilho.appendChild(copia);
            }
            copias++;
        }
        ligar();
    }

    function quadro(agora) {
        let dt = anterior === null ? 0 : Math.min((agora - anterior) / 1000, 0.1);
        anterior = agora;
        if (!mouseEmCima && !focoTeclado && !pressionado && !semMovimento.matches) {
            posicao += VELOCIDADE * dt;
        }
        if (salto !== 0) {
            // anda uma fração do que falta a cada quadro: rápido no começo, suave no fim
            let parte = semMovimento.matches ? salto : salto * Math.min(1, dt * 9);
            if (Math.abs(salto - parte) < 0.5) parte = salto;
            posicao += parte;
            salto -= parte;
        }
        posicao = ((posicao % volta) + volta) % volta;
        trilho.style.transform = `translateX(${-posicao}px)`;
        quadroPedido = requestAnimationFrame(quadro);
    }

    function ligar() {
        if (ativo && visivel && quadroPedido === null) quadroPedido = requestAnimationFrame(quadro);
    }

    function desligar() {
        cancelAnimationFrame(quadroPedido);
        quadroPedido = null;
        anterior = null;
    }

    carrossel.querySelectorAll('.carrossel-seta').forEach((seta) => {
        seta.addEventListener('click', () => {
            salto += Number(seta.dataset.direcao) * passo;
        });
    });

    // Arrastar para o lado (dedo ou mouse). Só vira arraste depois de 6px, para um toque
    // simples continuar abrindo o card; ao soltar, a faixa segue um pouco no embalo
    trilho.addEventListener('pointerdown', (evento) => {
        if (!ativo || evento.button !== 0) return;
        pressionado = { id: evento.pointerId, inicioX: evento.clientX, ultimoX: evento.clientX, amostras: [] };
        arrastou = false;
        salto = 0;
    });

    trilho.addEventListener('pointermove', (evento) => {
        if (!pressionado || evento.pointerId !== pressionado.id) return;
        if (!arrastou) {
            if (Math.abs(evento.clientX - pressionado.inicioX) < 6) return;
            arrastou = true;
            trilho.setPointerCapture(evento.pointerId);
        }
        posicao -= evento.clientX - pressionado.ultimoX;
        pressionado.ultimoX = evento.clientX;
        pressionado.amostras.push({ x: evento.clientX, t: evento.timeStamp });
    });

    function soltar(evento) {
        if (!pressionado || evento.pointerId !== pressionado.id) return;
        // velocidade dos últimos 100ms do gesto; quem segurou parado antes de soltar não ganha embalo
        let recentes = pressionado.amostras.filter((a) => evento.timeStamp - a.t < 100);
        if (arrastou && recentes.length > 1) {
            let primeira = recentes[0];
            let ultima = recentes[recentes.length - 1];
            let tempo = (ultima.t - primeira.t) / 1000;
            if (tempo > 0.01) {
                let embalo = -((ultima.x - primeira.x) / tempo) * 0.25;
                salto = Math.max(-2 * passo, Math.min(2 * passo, embalo));
            }
        }
        pressionado = null;
    }
    trilho.addEventListener('pointerup', soltar);
    trilho.addEventListener('pointercancel', soltar);

    // O clique que o navegador dispara ao soltar um arraste não deve abrir o link
    trilho.addEventListener('click', (evento) => {
        if (!arrastou) return;
        evento.preventDefault();
        evento.stopPropagation();
        arrastou = false;
    }, true);
    trilho.addEventListener('dragstart', (evento) => evento.preventDefault());

    // Pausa com o mouse em cima dos cards; no celular um toque não trava a faixa
    trilho.addEventListener('pointerenter', (evento) => {
        if (evento.pointerType === 'mouse') mouseEmCima = true;
    });
    trilho.addEventListener('pointerleave', () => {
        mouseEmCima = false;
    });

    // Navegando com Tab o navegador rola a janela até o card focado; ao sair, ela volta ao lugar
    trilho.addEventListener('focusin', (evento) => {
        if (evento.target.matches(':focus-visible')) focoTeclado = true;
    });
    trilho.addEventListener('focusout', (evento) => {
        if (trilho.contains(evento.relatedTarget)) return;
        focoTeclado = false;
        janela.scrollLeft = 0;
    });

    // Só anima enquanto aparece na tela
    new IntersectionObserver((entradas) => {
        visivel = entradas[0].isIntersecting;
        visivel ? ligar() : desligar();
    }).observe(janela);

    new ResizeObserver(medir).observe(janela);
    medir();
}

document.querySelectorAll('.carrossel').forEach(iniciarCarrossel);
