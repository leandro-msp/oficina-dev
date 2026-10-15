**Desenvolvimento Web - Aula 4 - 10/09/26**

# Cores, Unidades de Medidas, Elemento textuais, decoração e alinhamento.
---

# Cores em CSS

* **Propriedades:** Background-color, color, border-color, entre outras aceitam uma cor como valor
* **Maneiras de Aplicar:** Sintaxe por Palavras Chave, Sintaxe RGB, Sintaxe Hexadecimal.


## Métodos de aplicação:

**Método Simples - Palavra CHave:** a sintaxe por palavra chave consiste em colocar os nomes predefinidos dessas cores como valor dos atributos(para variações de cores exatas é um médo incomum).
> sintaxe:
```bash
h1 { 
    color:red;
}
h2{
    background-color: yellow;
}
```

**Método RGB:**é um sistema de cor que permite especificar até 16 milhoes de cores com uma combinação de três cores bases:
Vermelho(Red), Verde(Green), Azul(Blue).
Podemos escolher a intensidade de cada um desses trÊs canais básicos, numa escala de 0 a 255.
> sintaxe:
```bash
h2{
    color:rgb(255,200,0);
    background-color: rgb(255,0,0);
}
```

**Método Hexadecimal:** O sistema hexadecimal é amplamente utilizado pelo fato de que é suportado pela maioria dos navegadores, e possuie uma sintaxe mais curta, e possibilita a definição de cores totalmente precisas.
A notação hexadecimal começa com um # (hashtag) e possui 6 caracteres em sequência, os 2 primeiros indical canal Red, os 2 seguintes, o Green, e os dois últimos Blue, ou seja RGB. (#RRGGBB):
> sintaxe:
```bash
h1{
    color: #5108cf;
    background-color: #6fd0ed;
}
```
### Resumo das cores:

**Palavra-Chave:**: color: red;
**RGB:** color: rgb(255,255,255)
**Hexadecimal:** color : #FF0000;
---

## Unidades de Medida:

* **Unidades Relativas:** As unidades possuem esse nome pelo fato de que especifica um comprimento relativo a outra propriedade de medida.
As unidades relativas que abordaremos são:
    * **em :** na unidade de medida relativa é aplicada uma mutiplicidade a uma outra unidade definida anteriormente.
        * ex.: se você  deseja aplicar um tamanho de fonte em um parágrafo e o tamanho da fonte de um outro parágrafo tiver de ser o dobro do primeiro parágrafo, podemos indicar isso aplicando a multiplicidade do tamanho de fonte definido aos parágrafos.
> considerando que o tamanho de fonte padrão do navegador é de 16 pixels, assim será a aplicação da unidade relativda "em":
* para indicar alteração de tamanho de fonte, utiliza-se o atributo "font-size" para especificar a propriedade:
```bash
    .fonte1{
        font-size: 1em;
    }
    .fonte2{
        font-size: 2em;
    }
    .fonte3{
        font-size: 0.5em;
    }
```
1em,2em,0.5em relação ao tamanho padrãoo
    * **%:** de forma análoga da unidade relativa, o mesmo pode ser aplicado utilizando-se valores percenutais à unidades já definidas anteriormente.
    * aplicando valores percentuais no código anteriormente dado, é possível obter os memos resultados utilizando os valores adequados:
```bash
    .fonte1{
        font-size: 100%;
    }
    .fonte2{
        font-size: 200%;
    }
    .fonte3{
        font-size: 50%;
    }
```
> considerando o tamanho padrão(16pixels), 100% seria exatamente o valor padrão, 200% seria o dobro, e 50% a metade.

* **Unidades Absolutas:** As unidades de medidas absolutas não possuem dependencia em relação a outras unidades, elas são fixas e são apresentadas da forma como são determinadas, não sendo necessários valores de referência.
**Sendo elas:**
* **cm (centímetros):** Podemos determinar os comprimentos e tamanhos dos elemetnos que desejamos formatar utilizando essa unidade de medida.
* **mm (milímetros):** Dez milímetros equivalem a um centímetro, as uniddes são múltiplas entre si. o Uso é análogo, e a necessidade do uso vai da precisão do tamanho no projeto.
* **in: (polegadas, do inglês "inches"):** A polegada, ou inch, é uma unidade de equivale 2,54cm ou 96 pixels.
* **px (pixels):** o pixel(px) corresponde à menor unidade que forma uma imagem na nossa tela, ele equivale a (1/96) polegada.
* **pt (pontos):** os pontos, ou pt, é uma unidade de media que equivale a 1/72 polegada.

**ex.:**
```bash
h1{
    font-size: 1.5cm;
}
h2{
    font-size: 15mm;
}
h3{
    font-size: 0.3in;
}
h4{
    font-size: 35px;
}
```
**RESUMO:**
    * Medidas Absolutas: Independentes e imutáveis. Não mudam de tamanho não importa o contexto da tela.
    * Medidas Relativas: Proporcionais e flexíveis. Ideais para design responsivo e adaptação de diferentes dipositivos.
---

# Elementos Textuais, Alinhamento e decoração de texto

## LISTAS

A lista mais comum é a **lista não-ordenada**, que criamos usando a tag <ul></ul>. Para cada item na lista não ordenada, utilizamos uma maracação de item de lista <li></li>.
> exemplo lista não-ordenada:
```bash
<ul>
    <li>Primeiro item da lista</li>
    <li>Segundo item da lista
        <ul>
            <li>Primeiro item da lista aninhada</li>
            <li>Segundo item da lista aninhada</li>
        </ul>
    </li>
    <li>Terceiro Item da Lista</li>
</ul>
```
Na **lista ordenada**, a mesma tag de item de lista <li> é utilizada.
> exemplo losta ordenada:

```bash
<ol>
    <li>Primeiro item da lista</li>
    <li>Segundo item da lista</li>
    <li>Terceiro item da lista</li>
</ol>
```
    * As listas ordenadas também podem ter estrutura composta por outras listas ordenadas como no exemplo que temos para as listas não-ordenadas.
    * Também é possível ter listas ordenadas aninhadas em um item de uma lista não-ordenada e vice-versa.

## GLOSSÁRIO

Existe um terceiro tipo de lista que devemos utilizar para dmarcar um glossário, quando listamos termos e seus significados.
Essa lista é a lista de definição onde usamos as tags <dl>,<dt> e <dd> com seus respectivos fechamentos.
> ex.:
```bash
<dl>
    <dt>ADS</dt>
    <dd>
        Análise e Desenvolvimento de Sistemas é um curso do modelo tecnólogo que abrange conceitos da Tecnologia da Informação, como, programação, redes de computadores, ciência de dados, banco de dados, entre outros.
    </dd>
</dl>

```

## FORMATANDO ELEMENTOS TEXTUAIS

**Fonte-family**
Assim como alteramos cores pelo CSS, podemos alterar o texto com o uso da propriedade **font-family**. Esta propriedade pode receber seu valor com ou sem aspas.
    * no primeiro caso, passaremos o nome do arquivo de fonte a ser utilizado, e no último passaremos a família da fonte.
> ex.:
```bash
h1 {
    font-family: serif;
}
h2 {
    font-family: sans-serif;
}
body {
    font-family: "Arial", "Helvetica", sans-serif;
}
```
> no caso do body, primeiro vai verificar se tem a fonte Arial instalado se sim utiliza-a, caso contrário parte pra próxima, se nenhuma das opções iniciais não estiverem instalaas, passa a considerar qualquer fonte da família "sans-serif"

* **font-size:** especifica o tamanho de uma fonte aplicada a um elemento.
* **font-style:** especifica os estilos italic(itálico-inclinado), oblique(oblíqua) ou normal para o elemento.
    * italic: utiliza glifos itálicos projetados pelo designer da fonte, que podem ter formas diferentes(como um 'a' ou 'f' mais caligráfico).
    * oblique: inclina a versão romana (reta) da fonte usando o navegador, sem alterar o desenho das letras.
* **font-variant:** define a fonte como minúsculas ou Versalete(maiúsculas). Opções: normal e samll-caps.
* **font-weight:** define o peso da fonte, tais como bold (negrito) ou normal.

> ex:
```bash
h1 {
    font-family: serif;
    font-size: 50px;
    font-style: italic;
}

h2 {
    font-family: sans-serif;
    font-style: oblique;
    font-variant: small-caps;
}

body {
    font-family: "Arial", "Helvetica", sans-serif;

}

p {
    font-style: normal;
}

.negrito {
    font-weight: bold;
}
```
* **line-height:** define a altura de uma linha.
* **text-align:** alinha os textos na horizontal no centro(center), esquerda(left), justificado(justify) e direita(right).
* **text-decoration:** define a decoração do texto para os elementos. Podem ser none(nenhum), underline(linha de baixo), overline(linha de cima) ou line-through(linha através).

* **text-indent:** recua a primeira linha, cirnado recuo de um parágrafo
* **text-transform:** transforma o texto em uppercase (maiúscula), lowercase(minúscula) e capitalize (primeira letra de cada palavra maiúscula). O valor none tbm é aplicável.
* **letter-spacing:** tamanho do espaço entre cada letra.
* **word-spacing:** tamanho do espaço entre cada palavra.

> ex:
```bash
h1 {
    font-family: serif;
    font-size: 50px;
    font-style: italic;
    text-align: left;
    text-decoration: underline;
    text-indent: 30px;
}

h2 {
    font-family: sans-serif;
    font-style: oblique;
    font-variant: small-caps;
    text-align: center;
    text-decoration: overline;
}

body {
    font-family: "Arial", "Helvetica", sans-serif;

}

p {
    font-style: normal;
    line-height: 30px;
    text-align: right;
}

.negrito {
    font-weight: bold;
     text-decoration: line-through;
}

.maiuscula{
    text-transform: uppercase;
}
```