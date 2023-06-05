fechaInput = document.getElementById('InputDate');

const fechaMinima = new Date();
fechaMinima.setDate(fechaMinima.getDate() + 1);
fechaInput.setAttribute('min', fechaMinima.toISOString().split('T')[0]);

fechaInput.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowUp' || event.key === 'ArrowDown' || event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
      event.preventDefault();
    }
});

horaInput = document.getElementById('InputTime');

horaInput.addEventListener('keydown', (event) => {
  if (event.key === 'ArrowUp' || event.key === 'ArrowDown') {
    event.preventDefault();
  }
});


// Manejador de evento beforeinput para bloquear fechas específicas
fechaInput.addEventListener('input', async (event) => {
    const inputDate = event.target.value;
    if (!await fechaDisponible(inputDate)) {
        fechaInput.value = ''; // Limpia la fecha si está bloqueada
    }
});

async function fechaDisponible(date){
    const binnacle =document.getElementById("adminIDInput").value;
    if (date && binnacle) {
        const url = '/freeDate/?date=' + encodeURIComponent(date) + '&binnacle=' + encodeURIComponent(binnacle);
        try {
          const response = await fetch(url);
          const data = await response.json();
          return data.ans;
        } catch (error) {
          console.error(error);
        }
    }    
}

fechaInput.addEventListener("change", actualizarHorasDisponibles);

function actualizarHorasDisponibles() {
    const dateInput = document.getElementById("InputDate");
    const selectedDate = dateInput.value;
    
    
    const binnacle =document.getElementById("adminIDInput").value;
    if (selectedDate && binnacle) {
        const url = '/getFreeHours/?date=' + encodeURIComponent(selectedDate) + '&binnacle=' + encodeURIComponent(binnacle);
        fetch(url)
            .then(response => response.json())
            .then(data => {
                const timeList = document.getElementById("time_list");
                // Eliminar todas las opciones existentes
                while (timeList.firstChild) {
                    timeList.removeChild(timeList.firstChild);
                }
                // Crear nuevas opciones según las horas disponibles
                for (var j = 0; j < data.freeHours.length; j++) {
                    const horaDisponible = data.freeHours[j];
                    const option = document.createElement('option');
                    option.value = horaDisponible;
                    option.textContent = horaDisponible;
                    timeList.appendChild(option);
                }
            })
        .catch(error => console.error(error));
    }
  }
  //Falta generar lista de dias bloqueados y terminar de variar la lista de horas para elegir segun el dia
