**Capítulo 1️⃣**
## Fundamentos da Linguagem SQL

### 1 - O que é SQL:
  SQL(Structured Query Language) é a linguagem padrão para gerenciar e manipular bando de dados relacionais. É a base para a interação com sistemas como MySQL, PostgreSQL, SQL Server e Oracle.

### 2 - Por que aprender SQL?
  Essencial para desenvolvedores analistas de dados e qualquer profissional que trabalhe com informações. Permite criar, modificar e extrair dados, sendo uma habilidade universal no mercado de tecnologia.

### 3 - Tipos de Comandos
  SQL é dividida em DDL (Data Definition Language) para estrutura, DML ( Data Manipulation Language) para dos, DCL ( Data Control Language) para permissões e TCL (Transaction Control Language) para transações.
  
---

**Capítulo 2️⃣**
## Trabalhando com a Estrutura de Tabelas
A base de qualquer banco de dados relacional são as tabelas. Definir sua estrutura corretamente é crucial para a integridade e eficiência dos dados.

*  **CREATE TABLE:** Define o nome da tabela, colunas, tipos de dados e restrições (chaves primárias, estrangeiras, NOT NULL, UNIQUE, CHECK).
*  **ALTER TABLE:** Modifica a estrutura existente, adicionando, excluindo ou alterando colunas, e gerenciando restrições. É vital para evoluir o esquema do banco de dados.
*  **DROP TABLE:**  Remove uma tabela inteira do banco de dados, incluindo todos os seus dados e estruturas associadas. Use com cautela!

## Regras de Negócio e Relacionamentos
Além da estrutura básica, a integridade dos dados é garantida por regras de negócio e relacionamentos entre tabelas.

* **Chaves Primárias (PK):** Identificador único para cada registro em uma tabela, garantindo que não haja duplicidade de linhas. Essencial para a organização e recuperação de dados.
* **Chaves Estrangeiras (FK):** Estabelecem links entre tabelas, garantindo a integridade referencial. Por exemplo, ligando pedidos a clientes ou produtos a categorias. Elas impõem regras de relacionamento.
* **Índices:** Melhoram o desempenho das consultas, permitindo que o banco de dados encontre dados mais rapidamente, assim como um índice de livro.

---

**Capítulo 3️⃣**
## Manipulação de Dados: DML em ação
Uma vez que a estrutura está definida, é hora de preencher e gerenciar os dados. A DML (Data Manipulation Language) permite isso.

* **INSERT:** Adiciona novas linhas (registros) a uma tabela. Você pode inserir valores para todas as colunas ou especificar um subconjunto delas.
> exemplo:

```SQL
INSERT INTO Produtos (Nome, Preco) VALUES ('Notebook', 2500.00);
```
* **UPDATE:** Modifica dados existentes em uma ou mais linhas de uma tabela. A cláusula WHERE é crucial para especificar quais registros serão atualizados.
> exemplo:
```SQL
UPDATE Clientes SET Email = 'novo@email.com' WHERE ClienteID = 1;
```
* **DELETE:** Remove linhas de uma tabela. Assim como o UPDATE, a cláusula WHERE é fundamental para evitar a exclusão de todos os registros.
> exemplo:
```SQL
DELETE FROM Pedidos WHERE Status = 'Cancelado';
```

---

**Capítulo 4️⃣**
## Elaboração de Relatórios Essenciais

**Criação de Relatórios** 

A capacidade de extrair e analisar dados é um dos maiores poderes do SQL. Relatórios são criados principalmente com a cláusula **SELECT.**

* **SELECT:** Recupera dados de uma ou mais tabelas.
* **FROM:** Especifica as tabelas de onde os dados serão recuperados.
* **WHERE:** Filtra os resultados com base em condições, usando operadores relacionais (**=, !=, >, <**) e lógicos (**AND, OR, NOT**).
* **ORDER BY:** Classifica os resultados em ordem ascendente (ASC) ou descendente (DESC).


## Aprofundando nos Filtros e Operadores

Construir relatórios robustos exige um domínio dos filtros e operadores do SQL

* **Operadores Aritméticos**
  * Realizam cálculos em colunas numéricas: + (adição), - (subtração), * (multiplicação), / (divisão), % (módulo). Essenciais para cálculos em tempo real.
* **Operadores de Banco de Dados**
  * **LIKE:** Para pesquisa de padrões (com % e _).
  * **IN:** Para verificar se um valor está em uma lista.
  * **BETWEEN:** Para verificar se um valor está em um intervalo.
  * **IS NULL:** Para verificar valores nulos.
* **Funções de Agregação**
  * **COUNT():** Conta linhas.
  * **SUM():** Soma valores.
  * **AVG():** Calcula média
  * **MIN():** Retorna o menor valor.
  * **MAX():** Retorna o maior valor.
  > Usadas com **GROUP BY** para sumarizar dados.


## Relatórios Avançados: Subqueries e Joins
Para dados mais complexos e insights mais profundos, utilizamos subqueries e operações de JOIN.
    
