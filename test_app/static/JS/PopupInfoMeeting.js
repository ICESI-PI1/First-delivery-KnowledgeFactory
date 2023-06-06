const modalContentTemplate = document.querySelector('#modalContentTemplate');
const infoMeetingButtons = document.querySelectorAll('.infoMeeting');
console.log(infoMeetingButtons)
infoMeetingButtons.forEach(button => {
    button.addEventListener('click', () => {
      // Obtener los datos de la cita desde los atributos del botón
      const title = button.getAttribute('data-title');
      const date = button.getAttribute('data-date');
      const status = button.getAttribute('data-status');
      const description = button.getAttribute('data-description');
  
      // Llamar a la función createDynamicModal con los datos de la cita
      createDynamicModal(title, date, status, description);
    });
  });
  

function createDynamicModal(title, date, status, description) {
    const dynamicModal = document.querySelector('#dynamic-modal');

    // Actualiza los elementos del modal con los datos de la cita
    const modalTitle = dynamicModal.querySelector('.modal-title');
    modalTitle.textContent = title;

    const modalDate = dynamicModal.querySelector('.row:nth-child(1) .card_text_modal:nth-child(2)');
    modalDate.textContent = date;

    const modalStatus = dynamicModal.querySelector('.row:nth-child(2) .card_text_modal:nth-child(2)');
    modalStatus.textContent = status;

    const modalDescription = dynamicModal.querySelector('.row:nth-child(3) .card_text_modal:nth-child(2)');
    modalDescription.textContent = description;


    // Abre el modal usando Bootstrap
    const modal = new bootstrap.Modal(dynamicModal);

    // Abre el modal
    modal.show();
  }