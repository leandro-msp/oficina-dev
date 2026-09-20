//operadores de atribuição

let a,b,c,d;
let saida = document.getElementById("saida");
a=10; //b=10
b=2; //b=2
a+=b;//12 -> a vai receber receber o valor de a+b , ou seja, a ja vale 10, vai somar com valor de b=2 | a agora vale 12
b-=5; //b=-3  |  b=2-5 -> b=-3
saida.innerHTML="a = "+a;//12
saida.innerHTML+="<br>b = "+b; //-3
c=11;
d=6;
c%=d; //c = 5  | recebe o resto de 11 dividor por 6
d+=a; //d=18  | d=6 e a=12 , 6+12=18
saida.innerHTML+="<br>c = "+c; //5
saida.innerHTML+="<br>d = "+d;//18