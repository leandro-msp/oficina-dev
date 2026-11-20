  let saida = document.getElementById('saida');
    let tabela = "<table cellpadding='6'>";
    for (let linha = 1; linha <= 5; linha++) {
        tabela += '<tr>';
        for (let coluna = 1; coluna <= 5; coluna++) {
            tabela += `<td>${linha * coluna}</td>`;
        }
        tabela += '</tr>';
    }
    tabela += '</table>';
    saida.innerHTML = tabela; 