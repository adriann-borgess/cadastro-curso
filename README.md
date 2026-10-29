# 🎓 Sistema de Gerenciamento de Cursos

Aplicação web desenvolvida com **Python e Django** para o gerenciamento de cursos, com cadastro de informações acadêmicas, organização dos registros e controle de acesso por usuários e permissões.

O projeto foi desenvolvido como atividade prática para aplicar conceitos do framework Django, modelagem de dados, painel administrativo e gerenciamento de usuários.

## 🚀 Tecnologias utilizadas

* **Python** — linguagem de programação.
* **Django** — framework web.
* **SQLite** — banco de dados utilizado por padrão no ambiente de desenvolvimento.
* **HTML** — estrutura das páginas, incluindo a interface administrativa do Django.

## 📋 Funcionalidades

### Gerenciamento de cursos

O sistema possui um modelo `Curso` com os seguintes atributos:

| Campo           | Descrição                                         |
| --------------- | ------------------------------------------------- |
| `nome`          | Nome do curso.                                    |
| `codigo`        | Código único de identificação do curso.           |
| `descricao`     | Descrição do curso.                               |
| `carga_horaria` | Carga horária total em horas.                     |
| `modalidade`    | Modalidade de ensino: presencial, EAD ou híbrida. |
| `data_inicio`   | Data de início do curso.                          |
| `ativo`         | Indica se o curso está ativo.                     |
| `cadastrado_em` | Data e hora de criação do registro.               |

### Painel administrativo

O painel administrativo foi personalizado para facilitar a gestão dos cursos, incluindo:

* Listagem organizada dos cursos.
* Pesquisa por nome e código.
* Filtros por modalidade, situação e data de início.
* Ordenação dos registros pelo nome.
* Alteração do status dos cursos diretamente na listagem.
* Hierarquia de navegação por data.
* Organização dos campos em seções.
* Exibição da data de cadastro como campo somente leitura.
* Paginação dos resultados.

### Controle de acesso

O projeto utiliza os recursos de autenticação e autorização do Django para controlar o acesso às operações administrativas.

Foi criado um grupo de usuários chamado **Secretaria**, com permissões para:

* Visualizar cursos.
* Cadastrar cursos.
* Alterar informações dos cursos.

O grupo não possui permissão para excluir cursos, demonstrando a aplicação do princípio do menor privilégio.

## ⚙️ Como executar o projeto

### 1. Pré-requisitos

Certifique-se de ter instalado:

* Python 3.11 ou superior compatível com a versão do Django utilizada.
* Git.

### 2. Clone o repositório

```bash
git clone https://github.com/adriann-borgess/cadastro-curso

Entre na pasta do projeto:

```bash
cd cadastro-curso
```

### 3. Crie um ambiente virtual

**Windows — PowerShell:**

```powershell
python -m venv venv
```

Ative o ambiente virtual:

```powershell
.\venv\Scripts\Activate.ps1
```

**Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instale as dependências


```bash
pip install -r requirements.txt
```

### 5. Execute as migrações

```bash
python manage.py migrate
```

### 6. Crie um usuário administrador

```bash
python manage.py createsuperuser
```

Siga as instruções do terminal para definir as credenciais de acesso.

### 7. Inicie o servidor

```bash
python manage.py runserver
```

A aplicação ficará disponível localmente em:

`http://127.0.0.1:8000/`

O painel administrativo poderá ser acessado em:

`http://127.0.0.1:8000/admin/`

## 📁 Estrutura do projeto

```text
cadastro-curso/
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── cursos/
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    └── tests.py

```
## 🎯 Objetivos de aprendizagem

Este projeto permite praticar conceitos importantes do desenvolvimento web com Django:

* Criação e configuração de projetos e aplicações.
* Modelagem de dados com Django ORM.
* Definição de campos, restrições e opções de escolha.
* Criação e execução de migrações.
* Personalização do Django Admin.
* Pesquisa, filtros, ordenação e paginação.
* Autenticação, grupos e permissões.
* Versionamento de código com Git.

## 👨‍💻 Autor

Desenvolvido como projeto acadêmico para praticar desenvolvimento web com Python e Django.
