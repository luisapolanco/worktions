function getOptions() {
  return [];
}

var selectElement = document.getElementById("barrio");

var opciones = getOptions();

for (var i = 0; i < opciones.length; i++) {
    var option = document.createElement("option");
    option.value = opciones[i][0];
    option.text = opciones[i][1];
    selectElement.appendChild(option);
}