# 🏠 Sistema de Aluguel de Casas

Este repositório contém o código-fonte de um sistema de gerenciamento de aluguel de imóveis, desenvolvido como requisito avaliativo para a disciplina de **Programação Web 2** no **Instituto Federal do Piauí (IFPI) - Campus Parnaíba**.

A plataforma conecta proprietários e inquilinos, permitindo o cadastro de imóveis, gerenciamento de disponibilidade e realização de aluguéis de forma simples e intuitiva.

## 📋 Sobre o Projeto

O sistema foi projetado para atender a dois perfis de usuários distintos:

1. **Proprietários:** Podem cadastrar suas propriedades, adicionar fotos, descrições e definir preços, além de gerenciar o status de ocupação.
2. **Inquilinos:** Podem navegar pelas casas disponíveis no catálogo e realizar o aluguel.

## 📊 Modelagem do Banco de Dados

Abaixo está o diagrama de entidade-relacionamento que representa a estrutura das tabelas e relacionamentos do sistema:
![Diagrama do Banco de Dados](readme_itens/diagrama.png)

## 🚀 Funcionalidades Principais

* **Autenticação e Autorização**:
* Login utilizando e-mail como identificador.
* Controle de acesso baseado em tipos de usuário (Inquilino ou Proprietário).


* **Gestão de Propriedades**:
* Cadastro completo de imóveis com upload de imagens.
* Visualização e edição de disponibilidade (Alugar/Desalugar).


* **Fluxo de Aluguel**:
* Listagem de imóveis disponíveis para inquilinos.
* Sistema de confirmação de aluguel que atualiza automaticamente o status do imóvel.


* **Interface**:
* Layout responsivo utilizando **Bootstrap 5**.



## 🛠️ Tecnologias Utilizadas

* **Linguagem**: Python 3.x
* **Framework Web**: Django 6.0
* **Banco de Dados**: MySQL
* **Bibliotecas Auxiliares**:
* `pillow`: Manipulação de imagens.
* `mysqlclient`: Conector para o banco de dados MySQL.
* `asgiref`, `sqlparse`, `tzdata`.



## ⚙️ Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

* [Python](https://www.python.org/) (versão compatível com Django 6.0)
* [MySQL Server](https://dev.mysql.com/downloads/installer/)
* [Git](https://git-scm.com/)

## 🔧 Instalação e Configuração

Siga os passos abaixo para executar o projeto em seu ambiente local:

### 1. Clonar o Repositório

```bash
git clone https://github.com/Eynz6002/Aluguel-de-Casas.git
cd Aluguel-de-Casas

```

### 2. Configurar o Ambiente Virtual

Crie e ative um ambiente virtual para isolar as dependências do projeto:

**Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate

```

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate

```

### 3. Instalar Dependências

Com o ambiente virtual ativo, instale os pacotes listados no `requirements.txt`:

```bash
pip install -r requirements.txt

```

### 4. Configurar o Banco de Dados

1. Crie um banco de dados no seu servidor MySQL.
2. Abra o arquivo `core/settings.py` e localize a configuração `DATABASES`.
3. Atualize os campos com as credenciais do seu banco de dados local:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_seu_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

```

### 5. Executar Migrações

Crie as tabelas no banco de dados executando as migrações do Django:

```bash
python manage.py migrate

```

### 6. Criar Superusuário (Opcional)

Para acessar o painel administrativo do Django (`/admin`), crie um superusuário:

```bash
python manage.py createsuperuser

```

### 7. Executar o Servidor

Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver

```

O sistema estará acessível em: `http://127.0.0.1:8000/`

## 👤 Autor

Desenvolvido por **Enzo Ytalo** ([@Eynz6002](https://github.com/Eynz6002)).
