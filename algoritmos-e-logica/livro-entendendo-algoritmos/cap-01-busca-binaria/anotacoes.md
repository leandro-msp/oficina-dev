### Pesquisa Binária

Uma pesquisa binária consiste em você chegar na resolução de uma operação/problema/tarefa com a menor quantidade de tentativas possíveis. Diferente da pesquisa simples, onde dada uma operação ela realiza uma tentativa de cada vez, levando mais tempo para chegar ao resultado, e quanto maior for a pesquisa/operação a ser realizada, o número de etapas aumenta drasticamente.

---

> Exemplo:
Dado a tarefa de descobrir um número escolhido dentro de uma lista de **100 números**, a pessoa que escolheu responda a cada tentativa: *"baixo"* se o valor dito esteja distante do escolhido ou, *"alto"*  caso o valor dito tenha ultrapassado o valor escolhido.

---

**Pesquisa Simples:**
A pesquisa simples poderia levar até 100 tentativas, caso o número escolhido seja o número 100, pois ela vai sendo feita gradativamente(1,2,3,4..) 
* 1 = Baixo , 2 = baixo , 7 = baixo 19 = baixo ...

---

**Pesquisa Binária:**
Já a pesquisa binária busca quebrar essa operação, diminuindo a quantidade de tentativas. Matendo a mesma lista de 100 e o número escolhido fosse o 100, se usarmos esse método de pesquisa teremos a seguinte performance:

> [!TIP]
> Começaríamos pela metade **(50)**, e a pessoa que escolheu disser que valor é "baixo", já **eliminamos** a metade de tentativas, pois os números de 1 a 50 foram descartados. Sobrando ainda 50, tentamos a metade do que resta (25), 50 é nosso atual ponto de partida, então temos o 75 (50+25), se ainda sim o valor for "baixo" ainda nos resta 25 números, e veja bem, apenas com duas tentativas já eliminamos 75 tentivas que seriam erradas. Seguindo essa lógica de quebrar pela metade, para descobrir um valor escolhido de 1 a 100 e fosse exatamente o 100, com a pesquisa binária levaríamos no máximo **7 tentativas.** (50, 25, 13, 7, 4, 2, 1)



Uma pesquinsa binária só funciona quando a sua lista está ordenada. Por exemplo, os nomes em uma agenda telefônica estão em ordem alfabética, então podemos utilizar a pesquisa binária para procurar um nome. O que aconteceria se a lista não tivesse ordenada? Certamente seria uma busca que resultaria em desistência.

O algoritmo montado neste capítulo representa exatamente esse tipo de operação.