const fechaInput = document.getElementById('InputDate');
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

const horaInput = document.getElementById('InputTime');

horaInput.addEventListener('keydown', (event) => {
  if (event.key === 'ArrowUp' || event.key === 'ArrowDown') {
    event.preventDefault();
  }
});
