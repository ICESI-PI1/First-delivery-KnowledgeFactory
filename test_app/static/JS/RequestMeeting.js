fechaInput = document.getElementById('InputDate');
//El minimo de fecha es a partir de mañana
const fechaMinima = new Date();
fechaMinima.setDate(fechaMinima.getDate() + 1);
fechaInput.setAttribute('min', fechaMinima.toISOString().split('T')[0]);

// Ya funciona el bloqueo de flechas para el inputDate
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

adminField = document.getElementById('admin');

horaInput.addEventListener('change', getAvailableOptions);
fechaInput.addEventListener('change', getAvailableOptions);

function getAvailableOptions() {
  const date = fechaInput.value;
  const time = horaInput.value;
  if (date && time) {
    url = '/get_available_admins/?date=' + encodeURIComponent(date) + '&time=' + encodeURIComponent(time);
    fetch(url)
      .then(response => response.json())
      .then(data => {
        adminField.innerHTML = '';
        if(data.available_admins.length==0){
          const option = document.createElement('option');
          option.value = -1;  
          option.textContent = "No hay administradores disponibles";
          adminField.appendChild(option);
        }else{
          for (admin of data.available_admins) {
            const option = document.createElement('option');
            option.value = admin.id;  
            option.textContent = admin.name;
            adminField.appendChild(option);
          }
        }
      })
      .catch(error => console.error(error));
  }
}
