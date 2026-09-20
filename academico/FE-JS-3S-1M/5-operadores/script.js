saida = document.querySelector("#saida"); // manipulando o conteúdo dentro do html com o ID saida
saida.innerHTML = "funciona";


//operdodres aritiméticos
const num1 = parseFloat(prompt ("Digite o número1: ")); // parseFloat -> o valor número digitado é convertido para tipo float
const num2 = parseFloat(prompt ("Digite o número2:")); // prompot -> comando de entrada de dados(user digita)
let soma;
soma=num1+num2;
saida.innerHTML="<br>Soma = "+soma; // operador soma, vai somar os 2 valores digitados pelo usuário
saida.innerHTML+="<br>Subtração = "+(num1-num2); //subtração, vai subtrair o valor 2 no primeiro
saida.innerHTML+="<br>Multiplicação = "+num1*num2; //multiplica os valores digitados
saida.innerHTML+="<br>Divisão = "+(num1/num2); // faz a divisão usando os valores digitados
saida.innerHTML+="<br>Resto = "+(num1%num2); // resto da divisão ou módulo
saida.innerHTML+="<br>Expo = "+(num1**num2); // exponencial , o segundo número se torna a potência do primeiro