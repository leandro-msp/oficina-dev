// 1. Definição de Constantes (Referências ao DOM)
const inputNome = document.getElementById('campoNome');
const inputNota1 = document.getElementById('nota1');
const inputNota2 = document.getElementById('nota2');
const areaResultado = document.getElementById('resultado');
 
// 2. Função para capturar os dados, calcular a média e exibir
function calcularMedia() {
    // Captura dos valores no momento da execução
    const nome = inputNome.value; // pega um valor q está em um campo
    const n1 = Number(inputNota1.value);
    const n2 = Number(inputNota2.value);
 
    // Validação simples
    if (nome === "" || inputNota1.value === "" || inputNota2.value === "") {
        areaResultado.innerHTML = "<p style='color:red'>Preencha todos os campos!</p>";
        return;
    }
 
    const media = (n1 + n2) / 2;
     
    // Exibição dos dados
    areaResultado.innerHTML = `
        <h3>Resultado</h3>
        <p>Aluno: <strong>${nome}</strong></p>
        <p>Média Final: <strong>${media.toFixed(1)}</strong></p>
    `;
}
 
// 3. Função para resetar o formulário e focar no primeiro campo
function limparCampos() {
    // Limpando os valores
    inputNome.value = "";
    inputNota1.value = "";
    inputNota2.value = "";
    areaResultado.innerHTML = "";
 
    // Direcionando o cursor (foco) para o campo nome
    inputNome.focus();
}
