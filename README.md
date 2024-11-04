# Django-Blog

## Descrição do Projeto

O Django-Blog é um projeto de blog desenvolvido com Django, um framework web em Python. Este projeto inclui funcionalidades como criação de postagens, comentários, autenticação de usuário (login/logout) e suporte a uploads de mídia.

## Estrutura do Projeto

### Diretórios e Arquivos Principais

#### `blog_main/`
Este diretório contém o aplicativo principal do blog, com a lógica central do Django para gerenciar as funcionalidades principais.

- **Funcionalidades:**
  - **Autenticação:** Login e logout de usuários.
  - **Postagens de Blog:** Criação, edição e exclusão de postagens.
  - **Usuários e Perfis:** Gerenciamento de perfis e autenticação de usuários.

#### `blogs/`
Este diretório contém funcionalidades adicionais do blog, especialmente relacionadas a comentários.

- **Funcionalidades:**
  - **Comentários:** Implementação de comentários destacados.
  - **Destaque de Conteúdo:** Suporte para destacar certos comentários ou postagens.

#### `media/uploads/2024/`
Este diretório armazena os arquivos de mídia enviados, como imagens e vídeos, organizados por ano.

- **Funcionalidades:**
  - **Uploads de Mídia:** Armazenamento e organização de imagens para postagens.
  - **Serviço de Mídia:** Configuração para servir arquivos de mídia para o blog.

#### `templates/`
Armazena os templates HTML do projeto para a interface com o usuário.

- **Funcionalidades:**
  - **Templates de Postagens e Comentários:** Exibe postagens e comentários.
  - **Templates de Autenticação:** Layouts para login, logout e registro de usuário.
  - **Outras Páginas:** Páginas principais do blog, incluindo listagem de postagens e páginas de erro.

### Arquivos de Configuração e Outros

#### `.gitignore`
Lista de arquivos e diretórios que devem ser ignorados pelo Git. Inclui o banco de dados, arquivos de mídia e outros arquivos temporários.

#### `db.sqlite3`
O banco de dados SQLite do projeto, que armazena as postagens, usuários, comentários e outras informações persistentes.

#### `manage.py`
Script de gerenciamento do Django. Permite rodar comandos como iniciar o servidor, aplicar migrações e criar um usuário administrador.

#### `requirements.txt`
Lista de pacotes Python necessários para rodar o projeto. Para instalar as dependências, execute `pip install -r requirements.txt`.

## Histórico de Commits

Os principais commits indicam as seguintes mudanças:

- **"login and logout":** Implementação de login e logout de usuários.
- **"comment featured":** Funcionalidades de comentários, incluindo destaques.
- **"deployment":** Configurações relacionadas ao deploy do projeto.

## Tecnologias Utilizadas

- **Django (Python):** Framework backend utilizado para gerenciar a lógica, banco de dados e autenticação do blog.
- **HTML e CSS:** Para estruturar e estilizar a interface do blog.
- **SQLite:** Banco de dados para armazenar as informações do projeto.

## Instruções de Instalação e Execução

1. **Clonar o repositório:**
   ```bash
   git clone <URL-do-repositório>
   cd django-blog

2. **Instalação de Dependências:**
- Utilize o arquivo requirements.txt para instalar todas as dependências do projeto. Execute o comando abaixo:
- pip install -r requirements.txt

3. #### **Aplicar migrações do banco de dados:**
   
4. #### Aplicar migrações do banco de dados:
- python manage.py migrate

5. **Criar um superusuário (opcional):**
- python manage.py createsuperuser

6. **Iniciar o servidor de desenvolvimento:**
- python manage.py runserver

**Acessar o projeto: Abra o navegador e acesse http://127.0.0.1:8000/.**


Essa estrutura em Markdown fornece um guia claro e organizado sobre como configurar e iniciar o projeto Django-Blog.




