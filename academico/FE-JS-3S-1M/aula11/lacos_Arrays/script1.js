const saida = document.querySelector("#saida");

let i = 0; // valor inicial
while (i <=5){ // condição
    saida.innerHTML += `<br>numero ${i}`;
    i++; // contador
}

/*
Saida : 0 1 2 3 4 5
1) valor inicial : 0
2) condição? 1<=5
3) condador I++
4) vezes que looping foi executado : 6
5) o valor que tornou a condição falsa : 6
*/

saida.innerHTML+= `<br>`;
// saida 11 12 13 14 
let a = 11;
while (a<=14){
    saida.innerHTML += `<br>numero ${a}`;
    a++; // contador
}

/*
1) valor inicial : 11
2) condição? a<=14
3) contador a++
4) vezes que looping foi executado : 4
5) o valor que tornou a condição falsa : 15
*/

saida.innerHTML+= `<br>`;
// 4 3 2 1 0

let b = 4;
while (b>=0){
    saida.innerHTML+= `<br>numero ${b}`;
    b--;
}
/*
1) valor inicial : 4
2) condição? b >=0 ou b>-1
3) contador b--
4) vezes que looping foi executado : 5
5) o valor que tornou a condição falsa : -1
 */
saida.innerHTML+= `<br>`;
// saida 0 2 4 6 8 10 

let c = 0;
while (c<=10){
    saida.innerHTML += `<br>numero ${c}`;
    c+=2;
}
/*
1) valor inicial : 0
2) condição? c <=10 ou c<12
3) contador c+=2
4) vezes que looping foi executado : 6
5) o valor que tornou a condição falsa : 12
 */