# ⚙️ O que é um SBGD?

**SGBD - Sistema Gerenciador de Banco de Dados**: é um conjunto de softwares que gerencia o acesso aods dados, garantindo segurança, concorrência(múltiplos usuários) e integridade. Também conhecido como DBMS (Database Management System).


## 🌐 Modelo ACID
Para garantir a confiabilidade, um SGBD deve seguir quatro princípios:
* **Atomicidade:** A transação é uma unidade indivisível(tudo ou nada), ou seja, um processo (manipulação,requisição) não é feito pela metade ou funciona completamente ou nada é realizado.
* **Consistência:** Os dados devem respeitar todas as regras de itegridade.
* **Isolamento:** Uma transação não interfre em outra que ocorre simultaneamente.
* **Durabilidade:** Uma vez gravado, o dado não se perde em falhas de sistema.

## 🖥️ Principais SGBDs do Mercado

### Oracle
* **Tipo:** Relacional (Enterprise)
* **Foco:** Ambientes corporativos de alto desempenho e missões críticas.

### MySQL
* **Tipo:** Relacional (OpenSource/Oracle)
* **Foco:** Aplicações Web, rapidez e facilidades de uso

### PostgreeSQL
* **Tipo:** Relacional (Objeto-Relacional)
* **Foco:** Robustez, conformidade com padrões SQL e extensibilidade.

### SQLite
* **Tipo:** Relacional (Serverless)
* **Foco:** Dispositivos móveis e aplicações locais (não requer instação de servidor)



## 🔧​ Ferramentas Práticas

### Ambientes Multi-SGBD
* **DB Fiddle:** Testes rápidos em MySQL, PostgreSQL e SQLite
* **SQK Fiddle:** Ótimo para comparar o mesmo código em diferentes motores.
* **SQLite Online:** Interface limpa e suporte a arquivos locais
* **Onecompiler:** MySQL, PostgreSQL, Oracle

### Ambientes Específicos e Avançados
* **Oracle Live SQL:** Plataforma oficial gratuita Oracle para estudantes.
* **Google Cloud Shell:** Terminal Linux no navegador para usuários avançados.

### Ambientes com API-PostgreS
* **Neon:** Postgres com API e Serverless
* **Supabase:** Postgress com API e Authentication