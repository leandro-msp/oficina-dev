const saida = document.getElementById('saida');
const cor = document.getElementById('cor');
const enviar = document.getElementById('btn');

enviar.addEventListener('click', semaforo);

function semaforo(){
    switch(cor.value){
        case "vermelha": saida.innerHTML = `Pare!`; break;
        case "amarela" : saida.innerHTML =  `Atenção!` ; break;
        case "verde" : saida.innerHTML = `Siga!`; break;
}
}

