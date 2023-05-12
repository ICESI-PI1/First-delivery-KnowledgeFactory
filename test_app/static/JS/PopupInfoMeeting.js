const btnOpenModal = document.querySelector("#btn-open-modal");
const btnCloseModal = document.querySelector("#btn-close-modal");
const modal = document.querySelector("#modal");

modal.addEventListener('shown.bs.modal', ()=>{
    btnOpenModal.focus();
})

btnCloseModal.addEventListener("click",()=>{
    modal.close();
})