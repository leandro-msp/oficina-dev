let a,b,c,res,res1,res2;
let saida = document.getElementById("saida");
a=9;
b=10;
c=200;
res=(a<b);
res1=(a<b) && (c>a);
res2 = (a>b) || (c>b);
saida.innerHTML=`a = ${a} , b = ${b} <br>
                a < b : ${(a<b)} <br>
                !( a < b) : ${!(a<b)}<br>
                res : ${typeof(res)}<br>
                res1 : ${res1}<br>
                res2 : ${res2}<br>
`;

