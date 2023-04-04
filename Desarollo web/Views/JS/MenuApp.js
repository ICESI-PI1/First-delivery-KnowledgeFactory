const iconMenu = document.querySelector('#icon_menu'),
        menu = document.querySelector('#menu')

iconMenu.addEventListener('click', (e) => {
    menu.classList.toggle('active');
    document.body.classList.toggle('opacity');

    const actualSrc = e.target.getAttribute('src');

    if(actualSrc == '..\\Images\\Íconos\\icons8-búsqueda-50.svg'){
        e.target.getAttribute('src','..\\Images\\Íconos\\icons8-búsqueda-50.svg')
    }else{
        e.target.getAttribute('src','..\\Images\\Íconos\\icons8-búsqueda-50.svg')
    }
})