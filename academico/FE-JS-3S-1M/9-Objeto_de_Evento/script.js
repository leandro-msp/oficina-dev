// 1. Definição de Constantes (Referências ao DOM)
const form = document.getElementById('meuForm');
const inputNome = document.getElementById('campoNome');
const inputNota1 = document.getElementById('nota1');
const inputNota2 = document.getElementById('nota2');
const areaResultado = document.getElementById('resultado');
const btnLimpar = document.getElementById('btnLimpar');
const teste = document.getElementById('teste');
 
// 2. Eventos
// O submit só dispara se a validação nativa (required, min, max) passar
form.addEventListener('submit', function (event) {
    event.preventDefault(); // impede o envio (method="post") e o recarregamento
    calcularMedia();
});

function alterar(){
    document.querySelector("body").style.backgroundColor="lightblue";
}
teste.addEventListener('click', alterar);

btnLimpar.addEventListener('click', limparCampos);


// 3. Função para calcular a média e exibir
function calcularMedia() {
    // Captura dos valores no momento da execução
    const nome = inputNome.value.trim();
    const n1 = inputNota1.valueAsNumber;
    const n2 = inputNota2.valueAsNumber;
 
    const media = (n1 + n2) / 2;
    const situacao = media >= 6 ? "Aprovado" : "Reprovado";
 
    // Estrutura fixa (HTML escrito por nós, sem dados do usuário)
    areaResultado.innerHTML = `
        <h3>Resultado</h3>
        <p>Aluno: <span id="outNome"></span></p>
        <p>Média Final: <strong id="outMedia"></strong> - <span id="outSituacao"></span></p>
    `;
 
    // Dados inseridos com textContent (seguro contra XSS)
    document.getElementById('outNome').textContent = nome;
    document.getElementById('outMedia').textContent = media.toFixed(1);
 
    const outSituacao = document.getElementById('outSituacao'); // elemento só vai existir a partir do momento que clicar o botao calcular
    outSituacao.textContent = situacao;
    outSituacao.classList.add(media >= 6 ? 'aprovado' : 'reprovado');
}
 
// 4. Função para resetar o formulário e focar no primeiro campo
function limparCampos() {
    form.reset();
    areaResultado.replaceChildren();
    inputNome.focus();
}
