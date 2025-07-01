# Criando um ambiente virtual para ML

Este é um **tutorial completo para a criação de um ambiente virtual em Python** com as bibliotecas mais usadas em análise de dados e machine learning: `pandas`, `numpy`, `matplotlib`, `seaborn` e `scikit-learn (sklearn)`.

---

## 🧪 Objetivo do Tutorial

Criar um **ambiente virtual isolado** com as bibliotecas necessárias para trabalhar com:

- Manipulação de dados (`pandas`, `numpy`)
- Visualização (`matplotlib`, `seaborn`)
- Machine Learning (`scikit-learn`)

---

## 📦 Requisitos

- Python 3.x instalado
- Sistema operacional: Windows, macOS ou Linux

---

## 🛠️ Passo a Passo

### 1. **Verifique se o Python está instalado**

No terminal ou prompt de comando:

```sh
python --version
# ou
python3 --version
```

Se não estiver instalado, baixe do site oficial: https://www.python.org/downloads/

---

### 2. **Crie uma pasta para seu projeto**

Escolha um local no seu computador e crie uma nova pasta. Exemplo:

```sh
mkdir c:\_mlUc1
cd c:\_mlUc1
mkdir mlEnv
cd mlEnv
```

---

### 3. **Crie o ambiente virtual**

O Python vem com o módulo `venv` embutido, que permite criar ambientes virtuais:

#### No Windows:

```bash
python -m venv ./
```

#### No macOS/Linux:

```bash
python3 -m venv ./
```

---

### 4. **Ative o ambiente virtual**

Agora você precisa ativar o ambiente antes de instalar pacotes.

#### No Windows:

- PowerShell

```bash
.\Scripts\Activate.ps1
```

- Prompt de Comando

```bash
.\Scripts\activate.bat
```

#### No macOS/Linux:

```bash
source ./bin/activate
```

✅ Se ativado corretamente, você verá `(venv)` no início do seu prompt.

---

### 5. **Instale as bibliotecas necessárias**

Com o ambiente ativado, execute:

```bash
python.exe -m pip install --upgrade pip
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl xlsxwriter torch

## PLN
pip install nltk spacy regex keras
python -m spacy download pt_core_news_sm

# Series Temporais e Previsão
pip install pandas prophet plotly statsmodels

```

---

### 6. **(Opcional) Verifique as versões das bibliotecas instaladas**

Para garantir que tudo foi instalado corretamente, rode:

```bash
cd ..
pip list
```

Você deve ver algo parecido com isso:

```
Package           Version
----------------- --------
matplotlib        3.8.0
numpy             1.24.3
pandas            2.1.0
scikit-learn      1.3.0
seaborn           0.12.2
```

---

### 7. **(Opcional) Crie um arquivo `requirements.txt`**

Este arquivo é útil para compartilhar ou reinstalar dependências futuramente.

```bash
pip freeze > requirements.txt
```

Conteúdo exemplo:

```
pandas==2.1.0
numpy==1.24.3
matplotlib==3.8.0
seaborn==0.12.2
scikit-learn==1.3.0
```

## 🧹 Desativar o ambiente virtual

Quando terminar, você pode sair do ambiente com:

```bash
deactivate
```

---

## ✅ Resumo

| Etapa                         | Comando                                                    |
| ----------------------------- | ---------------------------------------------------------- |
| Criar ambiente                | `python -m venv venv`                                      |
| Ativar ambiente (Windows)     | `venv\Scripts\activate`                                    |
| Ativar ambiente (macOS/Linux) | `source venv/bin/activate`                                 |
| Instalar bibliotecas          | `pip install pandas numpy matplotlib seaborn scikit-learn` |
| Salvar dependências           | `pip freeze > requirements.txt`                            |
| Desativar                     | `deactivate`                                               |

---

## 💡 Dicas Extras

- Use o ambiente virtual sempre que iniciar um novo projeto.
- Nunca instale bibliotecas globalmente (evita conflitos).
- Para recriar o ambiente em outro computador, use:  
  
  ```bash
  pip install -r requirements.txt
  ```

Ótimo! Vamos **integrar o ambiente virtual Python com Jupyter Lab**. Isso é muito útil para quem trabalha com análise de dados e machine learning, pois permite usar todas as bibliotecas instaladas no seu ambiente virtual diretamente em notebooks interativos.

---

## Jupyter Lab

Integrar o ambiente virtual (`venv`) com **Jupyter Lab**, para que possamos usá-lo como um kernel (interpretador Python) dentro dos notebooks.

---

## 🔧 Passos para Integrar `venv` com Jupyter Lab

### 1. **Ative o ambiente virtual**

#### No Windows:

```bash
venv\Scripts\activate
```

#### No macOS/Linux:

```bash
source venv/bin/activate
```

✅ Você deve ver `(venv)` no início do prompt.

---

### 2. **Instale `ipykernel`**

Para que o Jupyter Lab reconheça seu ambiente virtual como um kernel, instale o `ipykernel`:

```bash
pip install ipykernel
```

---

### 3. **Adicione o ambiente ao Jupyter como novo kernel**

Execute:

```bash
python -m ipykernel install --user --name=Machine_Learning --display-name "Python ML (venv)"
```

- `--name`: nome interno do kernel (use algo identificável)
- `--display-name`: nome exibido no Jupyter Lab

> Exemplo: substitua `Machine_Learning` pelo nome do seu projeto, como `ml_ambiente`.

---

### 4. **Instale Jupyter Lab (se ainda não tiver instalado globalmente)**

Se for a primeira vez que usa Jupyter Lab, instale-o:

```bash
pip install jupyterlab
```

---

### 5. **Inicie o Jupyter Lab**

Dentro do ambiente ativado, execute:

```bash
jupyter lab
```

Isso abrirá o Jupyter Lab no navegador padrão (geralmente em `http://localhost:8888`).

---

### 6. **No Jupyter Lab: selecione o kernel correto**

Ao criar um novo notebook:

1. Clique em “**Python (venv)**” no canto superior direito.
2. Selecione o kernel `"Python (venv)"` ou o nome escolhido anteriormente.

✅ Agora você está usando o ambiente virtual dentro do Jupyter Lab!

---

## 📁 Estrutura Final da Pasta

Após seguir todos os passos, sua pasta ficará assim:

```
meu_projeto_ml/
├── venv/                  # Ambiente virtual
├── requirements.txt       # Lista de dependências
├── teste.py               # Script de teste
└── ...
```

---

## 🧹 Desinstalar o kernel (opcional)

Se quiser remover o kernel depois:

```bash
jupyter kernelspec uninstall venv_meu_projeto
```

Confirme com `y`.

---

## ✅ Resumo dos Comandos

| Tarefa              | Comando                                                                                     |
| ------------------- | ------------------------------------------------------------------------------------------- |
| Ativar ambiente     | `source venv/bin/activate` (Linux/macOS) ou `venv\Scripts\activate` (Windows)               |
| Instalar ipykernel  | `pip install ipykernel`                                                                     |
| Adicionar kernel    | `python -m ipykernel install --user --name=venv_meu_projeto --display-name "Python (venv)"` |
| Iniciar Jupyter Lab | `jupyter lab`                                                                               |






