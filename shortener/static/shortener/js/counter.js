let form = document.forms.calculator;

form.size.onchange = calculate;
form.quantity.oninput = calculate;

function calculate() {
  document.getElementById('price').innerHTML = form.size.options[form.size.selectedIndex].dataset.price * form.quantity.value;
  document.getElementById('id_total_price').value = form.size.options[form.size.selectedIndex].dataset.price * form.quantity.value
};
calculate();