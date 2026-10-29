    let hora = new Date().getHours(); // Obtém a hora atual
    let saida = document.getElementById('saida');
    // Verifica se a hora é menor que 12
    hora = 13;
    if (hora < 12) saida.innerHTML = `Bom dia! - ${hora}`;
    else if (hora >= 12 && hota < 18) saida.innerHTML = `Boa tarde - ${hora}`;
    else saida.innerHTML = `Boa noite! - ${hora}`; // se tiver somente uma instrução, inserir as chaves se torna opcional
    