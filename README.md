# 🏠 Sistema de Aluguel de Casas

Este projeto é um sistema de gerenciamento de aluguel de imóveis desenvolvido como requisito para a disciplina de **Programação Web 2** no **IFPI Campus Parnaíba**. A plataforma permite que proprietários cadastrem suas casas e inquilinos realizem o aluguel de propriedades disponíveis.

## 📊 Modelagem do Banco de Dados

Abaixo está o diagrama de entidade-relacionamento que representa a estrutura das tabelas do sistema:

![Diagrama do Banco de Dados](readme_itens/diagrama.png)

---

## 🚀 Funcionalidades

* **Autenticação Personalizada**: Sistema de login utilizando e-mail como identificador único.
* **Níveis de Acesso**: Distinção entre **Inquilinos (I)** e **Proprietários (P)**.
* **Gestão de Imóveis**: Cadastro de propriedades com upload de fotos e gerenciamento de disponibilidade.
* **Fluxo de Aluguel**: Inquilinos podem visualizar casas disponíveis e confirmar o aluguel.

## 🛠️ Tecnologias

* **Framework**: Django 6.0.
* **Banco de Dados**: MySQL.
* **Imagens**: Pillow para processamento de fotos.

---

## 🔧 Instalação e Configuração

### 1. Preparar o Ambiente Virtual

Clone o repositório e crie o ambiente isolado:

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
