//CLAUDIO LUIS D
let saida = document.getElementById("saida");
let tabela = "<table cellpadding='6'>"; // cria a tabela com espaçamento entre as células
for (let linha = 1; linha <= 5; linha++) {
  tabela += "<tr>";
  for (let coluna = 1; coluna <= 5; coluna++) {
    tabela += `<td>${linha * coluna}</td>`; // 
  }
  tabela += "</tr>";
}
tabela += "</table>";
tabela += "<p id='resultado'></p>";
saida.innerHTML = tabela; // escreve na página uma única vez

let resultado = document.getElementById("resultado");
saida.addEventListener("click", function (numero) {
  if (numero.target.tagName === "TD") {
    resultado.textContent = "Número clicado: " + numero.target.textContent;
  }
});
