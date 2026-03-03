#  Projeto Lista de Tarefas (Django)

Aplicação web desenvolvida com Django para gerenciamento de tarefas organizadas por dia da semana.

##  Funcionalidades

-  Criar tarefas
-  Listar tarefas por dia da semana
-  Editar tarefas
-  Excluir tarefas
-  Persistência em banco de dados

##  Tecnologias utilizadas

- Python
- Django
- SQLite
- HTML e CSS básico

##  Conceitos aplicados

- Estrutura de projetos Django
- Separação de URLs com `include`
- Padrão CRUD (Create, Read, Update, Delete)
- Uso de `get_object_or_404`
- Uso de decorators (`require_POST`)
- Uso de `choices` no model
- Proteção CSRF

## ▶ Como executar o projeto

```bash
# Clonar o repositório
git clone https://github.com/GuilhermeMarques649/todo-django-api

# Entrar na pasta
cd todolist

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual (Windows)
.\.venv\Scripts\Activate.ps1

# Instalar dependências
pip install -r requirements.txt

# Rodar migrações
python manage.py migrate

# Executar servidor
python manage.py runserver

Acesse no navegador:

http://127.0.0.1:8000/