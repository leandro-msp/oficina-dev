# Estudos em Python

Ambiente central para registro e organização dos meus estudos na linguagem Python. O projeto contém exercícios de fixação, scripts e pequenos algoritmos **focados** na aplicação prática de conceitos desenvolvidos nas disciplinas.

## Conteúdos do Repositório

* **Lógica & Algoritmos:** Resolução de problemas e estruturação de pensamento lógico.
* **Cenários Aplicáveis:** Casos de uso reais e simulações do dia a dia.
* **Uso de Bibliotecas:** Exploração de módulos nativos e externos.
* **Estruturas de Dados:** Manipulação de listas, dicionários, tuplas e conjuntos.
* **Pequenos Projetos:** Aplicações completas para consolidação do aprendizado.

---

### Como Executar os Scripts

Se você deseja clonar este repositório e executar os projetos localmente sem poluir o seu ambiente global do Python, siga os passos abaixo para configurar o ambiente virtual (`.venv`).
  > esta etapa é recomendada, pois há scripts que utilizam bibliotecas específicas, caso não estejam presentes, a execução do código não irá funcionar.

### 1. Clonar o repositório

**OPÇÃO 1 - Clonar o repositório completo:**
> acesse o terminal de sua preferência e execute:

```bash
git clone https://github.com/leandro-msp/oficiva-dev
```
---
**OPÇÃO 2 - Clonar somente a pasta com conteúdo python(recomendado):**
> acesse o terminal de sua preferência e execute:

```bash
git clone --filter=blob:none --sparse https://github.com/leandro-msp/oficina-dev
```
Entre na pasta do repositório clonado:

```bash
cd oficina-dev
```
Define para o Git trazer apenas a pasta desejada:

```bash
git sparse-checkout set academico/disciplinas_cPython
```
---

**2.Entre na pasta do projeto:**
```bash
cd oficina-dev/academico/disciplinas_cPython
```

### 3. Criar e ativar o Ambiente Virtual (.venv)
  Para criar o ambiente virtual digite:

  WINDOWS:
  ```bash
  python -m venv .venv
  ```
  LINUX:
  ```bash
  python3 -m venv .venv
  ```

  **Ativando o ambiente:**

  WINDOWS:
  ```bash
  .\.venv\Scripts\Activate.ps1
  ``` 
  LINUX:
  ```bash 
  source .venv/bin/activate
  ```
  
### 4. Instalar as Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas necessárias executando:
```bash
pip install -r requirements.txt
```
### Executando os Jupyter Notebooks (.ipynb) e arquivos.py com suas rescpectivas dependências

com o VSCode abra o arquivo .ipynb desejado e clique em Run(botão play no canto superior esquero da célula)

# ATENÇÃO
 > caso a .venv não seja detectada automaticamente como kernel padrão,(no canto superior direito o Kernel selecionado ainda está Python 3.x.x, em vez de .venv(V3x...)) siga as instruções abaixo:

No canto superior direito do notebook, clique em **Select Kernel (ou Selecionar Kernel)**.

Selecione **Python Environments...** e escolha a versão referente à pasta .venv do projeto.

Se ainda assim não aparecer ".venv(V3.X...)Python(3.X...):

Windows:

Caso não apareça, selecione **"Enter interpreter path..."** e aponte para **.\.venv\Scripts\python.exe.**(navegue até onde você clonou o repositório, entre na pasta .venv\Scripts\ e selecione python.exe).

Linux: 

(Forçe o registro do Kernel)
Acesse o terminal, e cole o comando abaixo. Certifique-se que seu endereço esteja aparecendo "(.venv) no início, isso significa que as manipulações, serão aplicadas dentro do ambiente virtual.

```bash
python -m ipykernel install --user --name=meu_env_linux --display-name "Python (.venv)"
``` 

Feche seu VSCode, e abra novamente e veja se sua .venv agora está listada como um kernel.
  
# Arquivos PY

Para executar arquivos.py segue-se o mesmo tratamento. Selecione/abra o arquivo desejado e no canto inferior direito do seu VS Code, na barra de status, clique onde está indicando Python 3.X.X, e procure o local onde está o executável da sua .venv:

WINDOWS:
 > ./.venv/bin/python

LINUX:
 > .\.venv\Scripts\python.exe

