# Tipos de Dados ​🗂️​

Universo de valores que podem ser inseridos em um baco de dados de acordo com a estrutura pré-determinada na criação de cada coluna dentro da sua respectiva tabela;

### Oracle ​♨️​
    
* **Char(n):** Cadeia de caracteres de tamanho fixo, *n* pode assumir um valor máximo de 255 dígitos.
* **Varchar(n) ou Varchar2(n):** Cadeia de caracteres de tamanho variável, *n* pode assumir um valor máximo de 4000 dígitos
* **Number(x) ou Number(x,y):** Valores numéricos inteiros e reais, onde *x* representa a parte inteira e *y* as casas decimais, tamanho de até 38 posições.
* **Int**: Número inteiro, seu valor pode ser de Número inteiro, seu valor pode ser de -2147483648 a 2147483647
* **Date:** Armazenamenbto de data e hora


### MySQL ​🐬​

* **Char(n):** Cadeia de caracteres de tamanho fixo, *n* pode assumir um valor máximo de 255 dígitos
* **Varchar(n):** Cadeia de caracteres de tamanho variável, *n* pode assumir um valor máximo de 4000 dígitos
* **Int:** Número inteiro, seu valor pode ser -2147483648 a 2147483647
* **Date:** Armazenamento de data e hora

### PostgreSQL ​🐘​

* **Char(n):** Cadeia de caracteres de tamanho fixo, *n* pode assumir um valor máximo de 255 dígitos
* **Varchar(n):** Cadeia de caracteres de tamanho variável, *n* pode assumir um valor máximo de 10485760 dígitos
* **Integer:** Número inteiro, seu valor pode ser -2147483648 a 2147483647
* **Numeric (x,y):** Número real, onde *x* é a precisão total de dígitos e *y* são os dígitos após a vírgula
* **Serial:** Número inteiro auto-incrementável, usado geralmente como chave primária
* **Date:** Armazenamento de data
* **Timestamp:** Armazenamento de hora


# Constraints 🔗​

Uma constraint ou uma restrição representa um mecanismo capaz de implementar controles de garantam a consistência dos dados

* **NOT NULL:** Coluna de preenchimento obrigatório 
> exemplo
```SQL
nome VARCHAR(100) NOT NULL
```
* **UNIQUE:** Coluna que não permite valores repetidos
> exemplo
```SQL
email VARCHAR(100) UNIQUE
```
* **CHECK:** Validação de Valores
> exemplo
```SQL
idade INT CHECK (idade >= 0)
```
    * obs.: o assunto sobre o campo "idade" será abordado, isso é somente para fins de exemplo, em BD é boa prática recuperar valores de idade desta forma

* **PRIMARY KEY:** Coluna com valor único, preenchimento obrigatório, responsável pela criação de relacionamento
> exemplo
```SQL
id INT PRIMARY KEY
```
* **FOREIGN KEY:** Coluna que implementa a integridade referencial(relacionamento), conecta com a chave primária de outra tabela
> exemplo
```SQL
aluno_id INT REFERENCES aluno(id)
```