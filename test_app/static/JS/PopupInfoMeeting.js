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
        // Clonar la plantilla del contenido del modal
        const modalContent = modalContentTemplate.innerHTML;
        const dynamicModalContent = document.createElement('div');
        dynamicModalContent.innerHTML = modalContent;
        // Actualizar los elementos del modal con los datos de la cita
        const modalTitle = dynamicModalContent.querySelector('.modal-title');
        modalTitle.textContent = title;

        const modalDate = dynamicModalContent.querySelector('.row:nth-child(1) .card_text_modal:nth-child(2)');
        modalDate.textContent = date;

        const modalStatus = dynamicModalContent.querySelector('.row:nth-child(2) .card_text_modal:nth-child(2)');
        modalStatus.textContent = status;

        const modalDescription = dynamicModalContent.querySelector('.row:nth-child(3) .card_text_modal:nth-child(2)');
        modalDescription.textContent = description;

        // Crear el modal usando Bootstrap
        const modal = new bootstrap.Modal(document.querySelector('#dynamic-modal'));

        // Limpiar el contenido anterior del modal
        const modalBody = document.querySelector('#dynamic-modal .modal-content');
        modalBody.innerHTML = '';

        // Agregar el contenido dinámico al modal
        modalBody.appendChild(dynamicModalContent);

        // Abrir el modal
        modal.show();
  }