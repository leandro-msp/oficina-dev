let dia = new Date().getDay(); // Obtém o dia da semana (0-6)
let saida = document.getElementById('saida');
switch (dia) {
  case 0: saida.innerHTML = 'Hoje é Domingo!'; break;
  case 1: saida.innerHTML = 'Hoje é Segunda-feira!'; break;
  case 2: saida.innerHTML = 'Hoje é Terça-feira!'; break;
  case 3: saida.innerHTML = 'Hoje é Quarta-feira!'; break;
  case 4: saida.innerHTML = 'Hoje é Quinta-feira!'; break;
  case 5: saida.innerHTML = 'Hoje é Sexta-feira!'; break;
  case 6: saida.innerHTML = 'Hoje é Sábado!'; break;
  default: saida.innerHTML = 'Erro no cálculo do dia!';
}