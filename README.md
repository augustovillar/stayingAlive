# Stayling Alive

- Nome do Grupo: T4A1
- Nome dos Integrantes
    * Augusto Barbosa Villar Silva - 11831853
    * Matheus Tavares de Andrade - 10346662
    * Emilly da Silva Arcanjo - 11808105
# Pré-requisitos

Para utilizar este repositório você precisa ter Python 3.7 instalado e acesso a um terminal de linha de comando.

# Instalação

Primeiramente, abra o seu prompt de comando e clone o repositório através do seguinte comando:

```sh
git clone https://github.com/augustovillar/lab_soft_proj_MEAU.git
```

Após isso, entre na pasta do repositório clonado, crie e ative o ambiente virtual:

```sh
cd stayingAlive
python -m venv env
```

Para ativar o ambiente virtual no Windows (PowerShell):
```sh
.\env\scripts\Activate.ps1
```

Para ativar o ambiente virtual no Linux e Mac:
```sh
source env/bin/activate
```
Com esse último comando, o nome do seu ambiente deve aparecer no terminal ("env").

Por fim, é necessário instalar as dependencias no ambiente com o seguinte comando:
```sh
pip install -r requirements.txt
```

# Atualização da Interface

Para criar o arquivo Python da interface, execute o seguinte comando:
```
pyside6-uic interfaceJogo.ui -o interfaceJogo.py
```
Note que caso tenha alguma lateração no arquivo interfaceJogo.ui é importante recriar o arquivo Python.
# Executando o Programa
