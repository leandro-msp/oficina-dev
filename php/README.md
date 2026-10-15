# Ambiente PHP
# [![PHP](https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white)](https://www.php.net/)

## Conteúdo da Pasta
Aqui está presente um resumo do conteúdo aprendido em aulas acadêmicas e também em cursos. Possui pequenos scripts e testes utilizando as particularidades da linguagem e de vez em quando algumas integrações básicas com banco de dados.

**PARA UM CONTEÚDO MAIS ABRANGENTE** tenho um repositório onde registro meu aprendizado completo utilizando ferramentas para o desenvolvimento web, sendo elas, o próprio PHP, integração com banco de dados MySQL, gerenciamento de dependências com o Composer, arquitetura e organização com conceitos da Programação Orientada a Objetos (POO), e criação de projetos práticos, basta **[CLICAR AQUI](https://github.com/leandro-msp/curso-php-mysql).**

---

### Testando o ambiente 

Para facilitar o desenvolvimento e os testes locais em qualquer máquina sem a necessidade de instalar servidores pesados (como XAMPP ou WAMP), utilizaremos o **Servidor Embutido do PHP (*CLI Server*)**.

**Requisitos:**
* Ter o **PHP (versão 8.0 ou superior)** instalado na máquina e adicionado às Variáveis de Ambiente (`PATH`).
* MySQL ( para rodar projetos integrados com bancos de dados)


## Como Executar os exemplos:

1. Clone o repositório (Opção 1 - Repositório Completo): 

```bash
git clone https://github.com/leandro-msp/oficina-dev
```

Caso opte em não baixar **todo o conteúdo do repositório geral(todas as pastas)**, pode clonar apenas a pasta específica (Opção 2 - **somente pasta PHP**)(*RECOMENDADO*):

```bash
git clone --filter=blob:none --sparse https://github.com/leandro-msp/oficina-dev
```
Entre na pasta do repositório clonado:

```bash
cd oficina-dev
```
Define para o Git trazer apenas a pasta desejada:

```bash
git sparse-checkout set php
```

2. Acesse o diretório do projeto: 
```bash
cd oficina-dev/php
```

#### 3. Iniciando o servidor embutido do PHP:

O projeto conta com scripts de **inicialização rápida** (start e start.bat) que sobem o servidor automaticamente na **porta 8000**.

Escolha a instrução de acordo com o seu **sistema operacional e terminal preferido**: 

**Linux / macOS / Git Bash (Windows):**
> No terminal, certifique-se de estar dentro desta pasta e execute:

```bash
./start
```

**Windows (Prompt de Comando / CMD):**
> Se estiver utilizando o terminal CMD do Windows
```bash
start 
```
> ou 
```bash
start.bat
```

**Windows (PowerShell):**
> Se estiver utilizando o terminal PowerShell
```bash
.\start.bat
```

**Método Manual (Qualquer Terminal):**
> Caso prefira não usar os scripts de atalho, você pode rodar o comando nativo do PHP diretamente:
```bash
php -S localhost:8000
```

4. Após iniciar o servidor por qualquer um dos métodos acima, acesse no navegador: http://localhost:8000 , o servidor abrirá automaticamente o painel/menu principal (index.php)

 > Para encerrar o servidor a qualquer momento, volte ao terminal e pressione Ctrl + C.
    
