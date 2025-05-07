let btnMenu = document.getElementById('btn-abrir-menu');
let menu = document.getElementById('menu-mobile');
let overlay = document.getElementById('overlay-menu');

btnMenu.addEventListener('click', () => {
    menu.classList.add('abrir-menu-mobile');
})

menu.addEventListener('click', () => {
    menu.classList.remove('abrir-menu-mobile');
})

overlay.addEventListener('click', () => {
    menu.classList.remove('abrir-menu-mobile');
})