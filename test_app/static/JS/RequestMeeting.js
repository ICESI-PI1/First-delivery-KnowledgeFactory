const fechaInput = document.getElementById('InputDate');
//El minimo de fecha es a partir de mañana
const fechaMinima = new Date();
fechaMinima.setDate(fechaMinima.getDate() + 1);
fechaInput.setAttribute('min', fechaMinima.toISOString().split('T')[0]);

fechaInput.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowUp' || event.key === 'ArrowDown') {

    }
  });
fechaInput.addEventListener(Selection, (event) =>{
    event.data("17/11/2003");
})

const horaInput = document.getElementById('InputTime');

horaInput.addEventListener('keydown', (event) => {
  if (event.key === 'ArrowUp' || event.key === 'ArrowDown') {
    event.preventDefault();
  }
});
