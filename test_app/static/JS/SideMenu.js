iconMenu = document.querySelector('#sideMenu'),
menu = document.querySelector('#menu'),
restWindow = document.querySelector('#Box'),
estado = false

function visibleBTN(){
    document.getElementById("sideMenu").style.visibility = "visible";
}

function countElement(option){
    var grid = document.querySelectorAll(".gridProducts .card .selectionProject")
    var count = grid.length
    if(option == 1){
        for(i=0; i<count;i++){
            grid[i].style.width = "0"
            grid[i].style.height = "0"
        }
    }else{
        for(i=0; i<count;i++){
            grid[i].style.width = "93%"
            grid[i].style.height = "93%"
        }
    }
}

window.addEventListener('click', (e) => {
    if (document.getElementById("sideMenu").contains(e.target)){
        if(estado == false){
            menu.classList.toggle('active')
            document.getElementById("sideMenu").style.visibility = "hidden"
            document.body.classList.toggle('opacity')
            countElement(1)
            estado = true
        }
        
    }else{
        if(estado){
            menu.classList.toggle('active')
            document.body.classList.toggle('opacity')
            setTimeout(visibleBTN, 0300)
            countElement(2)
            estado = false;
        }
    }
})