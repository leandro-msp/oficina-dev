const saida = document.querySelector("#saida");

function dataHorario() {
  const now = new Date();

  // Data formatada (DD/MM/AAAA)
  const dia = String(now.getDate()).padStart(2, '0'); 
  // transformar em string, e define qtdd de 2 caracateres, e adiciona zero caso o valor recuperado tenha somente 1 caractere
  const mes = String(now.getMonth() + 1).padStart(2, '0');
  // +1 pois na linguagem os meses começam por 0 -> ex.: Janeiro em vez de ser 1, é 0 
  const ano = now.getFullYear();
  const data = `${dia}/${mes}/${ano}`;

  // Horário local(HH:MM:SS)
  const hora = String(now.getHours()).padStart(2, '0');
  const minuto = String(now.getMinutes()).padStart(2, '0');
  const segundo = String(now.getSeconds()).padStart(2, '0');
  const horario = `${hora}:${minuto}:${segundo}`;
  
  //saida.textContent = `{data} - ${horario}`; aida em formato texto
  saida.innerHTML = `<b>${data} - ${horario}<b>`;
 
}
dataHorario();
setInterval(dataHorario, 1000);//executa a função de 1 em 1 segundo