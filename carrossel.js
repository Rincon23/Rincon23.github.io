let trilho = document.getElementById('carrossel-projetos');
let pontos = document.getElementById('carrossel-pontos');
let btnAnterior = document.getElementById('carrossel-anterior');
let btnProximo = document.getElementById('carrossel-proximo');
let cards = [...trilho.children];

let posicoes = [];
let atual = 0;
let autoplay = null;
let usuarioMexeu = false;
let naTela = false;
let semMovimento = window.matchMedia('(prefers-reduced-motion: reduce)');

// Uma parada por card; no fim, onde varios cards ja cabem na tela, as paradas iguais viram uma so
function calcularPosicoes() {
    let max = trilho.scrollWidth - trilho.clientWidth;
    let recuo = parseFloat(getComputedStyle(trilho).paddingLeft);
    posicoes = [];
    for (let card of cards) {
        let alvo = Math.min(Math.max(card.offsetLeft - recuo, 0), max);
        if (posicoes.length === 0 || alvo - posicoes[posicoes.length - 1] > 1) {
            posicoes.push(alvo);
        }
    }
    desenharPontos();
    atualizarAtual();
}

function desenharPontos() {
    if (pontos.children.length === posicoes.length) return;
    pontos.innerHTML = '';
    posicoes.forEach((_, i) => {
        let ponto = document.createElement('button');
        ponto.type = 'button';
        ponto.setAttribute('aria-label', 'Ir para ' + cards[i].querySelector('.overlay').textContent);
        ponto.addEventListener('click', () => {
            pararDeVez();
            irPara(i);
        });
        pontos.appendChild(ponto);
    });
}

function atualizarAtual() {
    let x = trilho.scrollLeft;
    atual = 0;
    posicoes.forEach((p, i) => {
        if (Math.abs(p - x) < Math.abs(posicoes[atual] - x)) atual = i;
    });
    [...pontos.children].forEach((ponto, i) => {
        ponto.setAttribute('aria-current', i === atual ? 'true' : 'false');
    });
}

function irPara(i) {
    atual = (i + posicoes.length) % posicoes.length;
    trilho.scrollTo({ left: posicoes[atual], behavior: semMovimento.matches ? 'auto' : 'smooth' });
}

// O carrossel anda sozinho enquanto aparece na tela, pausa com o mouse em cima
// e para de vez quando a pessoa usa as setas, os pontos ou arrasta
function iniciarAutoplay() {
    if (autoplay || usuarioMexeu || !naTela || semMovimento.matches) return;
    autoplay = setInterval(() => irPara(atual + 1), 6000);
}

function pausarAutoplay() {
    clearInterval(autoplay);
    autoplay = null;
}

function pararDeVez() {
    usuarioMexeu = true;
    pausarAutoplay();
}

btnAnterior.addEventListener('click', () => {
    pararDeVez();
    irPara(atual - 1);
});

btnProximo.addEventListener('click', () => {
    pararDeVez();
    irPara(atual + 1);
});

let agendado = false;
trilho.addEventListener('scroll', () => {
    if (agendado) return;
    agendado = true;
    requestAnimationFrame(() => {
        agendado = false;
        atualizarAtual();
    });
});

['touchstart', 'wheel', 'keydown'].forEach((evento) => {
    trilho.addEventListener(evento, pararDeVez, { passive: true });
});

trilho.addEventListener('mouseenter', pausarAutoplay);
trilho.addEventListener('mouseleave', iniciarAutoplay);
trilho.addEventListener('focusin', pausarAutoplay);
trilho.addEventListener('focusout', iniciarAutoplay);

new IntersectionObserver((entradas) => {
    naTela = entradas[0].isIntersecting;
    naTela ? iniciarAutoplay() : pausarAutoplay();
}, { threshold: 0.4 }).observe(trilho);

// Só a largura muda as paradas; a altura muda toda vez que um badge termina de carregar
let larguraAnterior = trilho.clientWidth;
new ResizeObserver(() => {
    if (trilho.clientWidth === larguraAnterior) return;
    larguraAnterior = trilho.clientWidth;
    calcularPosicoes();
}).observe(trilho);
calcularPosicoes();
