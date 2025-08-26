# Calculadora Simples em Python

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)

## Sobre

Este projeto consiste em uma calculadora de console simples, desenvolvida em Python. O programa solicita ao usuário dois números e uma operação (soma, subtração, multiplicação ou divisão) e exibe o resultado.

O foco deste projeto não é apenas na funcionalidade, mas também na qualidade do código, implementando práticas como validação robusta de entradas do usuário e uma suíte completa de testes automatizados com **Pytest** para garantir a confiabilidade e a manutenibilidade da aplicação.

## Funcionalidades

- **Operações Básicas**: Realiza soma, subtração, multiplicação e divisão.
- **Validação de Entrada**: Garante que o usuário insira apenas valores numéricos para os cálculos.
- **Tratamento de Erros**: Previne a execução de operações inválidas, como a divisão por zero.
- **Interface de Console Clara**: Guias interativas para o usuário escolher a operação desejada.
- **Testes Automatizados**: Suíte de testes completa cobrindo lógica de negócio, casos de borda e integração.

## Tecnologias Utilizadas

- **[Python 3.10+](https://www.python.org/)**
- **[Pytest](https://docs.pytest.org/)** - Para testes automatizados.

## Como Instalar e Configurar

Para executar este projeto em sua máquina local, siga os passos abaixo.

### Pré-requisitos

- Python 3.10 ou superior.
- `pip` (gerenciador de pacotes do Python).

### Passos para Instalação

1.  **Clone o repositório** (ou simplesmente crie uma pasta com os arquivos `calculadora.py` e `test_calculadora.py`).
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Crie e ative um ambiente virtual** (altamente recomendado):
    ```bash
    # Criar o ambiente
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\activate

    # Ativar no macOS/Linux
    source venv/bin/activate
    ```

3.  **Crie o arquivo de dependências**:
    Crie um arquivo chamado `requirements.txt` na raiz do projeto com o seguinte conteúdo:
    ```txt
    pytest
    ```

4.  **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

## Como Usar

Para executar a calculadora, utilize o seguinte comando no seu terminal:

```bash
python calculadora.py

O programa irá solicitar interativamente que você digite os números e a operação desejada.

--- Calculadora Simples em Python ---
Digite o primeiro número: 10
Digite o segundo número: 5
Digite o código da operação desejada:
               Soma:          Digite 1
               Subtração:     Digite 2
               Multiplicação: Digite 3
               Divisão:       Digite 4
3

-------------------------------------
O resultado é: 50.0
-------------------------------------

## Como Rodar os Testes
Este projeto utiliza pytest para garantir a qualidade do código. Para executar a suíte de testes completa, navegue até a pasta raiz do projeto e execute:

'''bash
pytest
Para uma saída mais detalhada (verbose):

'''bash
pytest -v

Você deverá ver uma saída indicando que todos os testes passaram com sucesso:

============================= test session starts ==============================
...
collected 5 items

test_calculadora.py .....                                                [100%]

============================== 5 passed in 0.02s ===============================

Autor
Feito por Renan H. B. Amancio.