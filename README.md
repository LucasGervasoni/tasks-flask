# API de Gerenciamento de Tarefas 📝

Uma API simples para gerenciar uma lista de tarefas, desenvolvida com Python e Flask.

## Funcionalidades ✨

* **Criar** uma nova tarefa.
* **Listar** todas as tarefas.
* **Obter** uma tarefa específica por ID.
* **Atualizar** uma tarefa existente.
* **Excluir** uma tarefa.

## Pré-requisitos ⚙️

* Python 3.x
* Flask

## Instalação e Execução 🚀

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/LucasGervasoni/tasks-flask.git
    ```

2.  **Instale as dependências:**
    ```bash
    pip install Flask
    ```

3.  **Crie o arquivo `models/task.py`:**
    Este código assume que existe uma classe `Task` em um arquivo `models/task.py`. Crie esse diretório e arquivo com o seguinte conteúdo:

    ```python
    # models/task.py
    class Task:
        def __init__(self, id, title, description='', completed=False):
            self.id = id
            self.title = title
            self.description = description
            self.completed = completed

        def to_dict(self):
            return {
                "id": self.id,
                "title": self.title,
                "description": self.description,
                "completed": self.completed
            }
    ```

4.  **Execute a aplicação:**
    Salve o código principal como `app.py` e execute o comando:
    ```bash
    python app.py
    ```
    O servidor estará rodando em `http://127.0.0.1:5000`.

## Documentação da API 📖

As seguintes rotas estão disponíveis para interação com a API:

---

### **Criar Tarefa**

Cria uma nova tarefa.

* **URL:** `/tasks`
* **Método:** `POST`
* **Corpo da Requisição (JSON):**
    ```json
    {
      "title": "Minha nova tarefa",
      "description": "Descrição opcional da tarefa"
    }
    ```
* **Resposta de Sucesso (200):**
    ```json
    {
      "message": "Nova tarefa criada com sucesso"
    }
    ```

---

### **Listar Todas as Tarefas**

Retorna uma lista com todas as tarefas existentes.

* **URL:** `/tasks`
* **Método:** `GET`
* **Resposta de Sucesso (200):**
    ```json
    {
      "tasks": [
        {
          "id": 1,
          "title": "Comprar pão",
          "description": "Ir à padaria da esquina",
          "completed": false
        },
        {
          "id": 2,
          "title": "Estudar Flask",
          "description": "Ver a documentação da API",
          "completed": true
        }
      ],
      "total_tasks": 2
    }
    ```

---

### **Obter Tarefa por ID**

Busca uma tarefa específica pelo seu ID.

* **URL:** `/tasks/<id>`
* **Método:** `GET`
* **Parâmetros da URL:**
    * `id` (integer): O ID da tarefa.
* **Resposta de Sucesso (200):**
    ```json
    {
      "id": 1,
      "title": "Comprar pão",
      "description": "Ir à padaria da esquina",
      "completed": false
    }
    ```
* **Resposta de Erro (404):**
    ```json
    {
      "message": "Tarefa não encontrada"
    }
    ```

---

### **Atualizar Tarefa**

Atualiza os dados de uma tarefa existente.

* **URL:** `/tasks/<id>`
* **Método:** `PUT`
* **Parâmetros da URL:**
    * `id` (integer): O ID da tarefa a ser atualizada.
* **Corpo da Requisição (JSON):**
    ```json
    {
      "title": "Novo título da tarefa",
      "description": "Nova descrição",
      "completed": true
    }
    ```
* **Resposta de Sucesso (200):**
    ```json
    {
      "message": "Tarefa atualizada com sucesso"
    }
    ```
* **Resposta de Erro (404):**
    ```json
    {
      "message": "Tarefa não encontrada"
    }
    ```

---

### **Excluir Tarefa**

Remove uma tarefa da lista.

* **URL:** `/tasks/<id>`
* **Método:** `DELETE`
* **Parâmetros da URL:**
    * `id` (integer): O ID da tarefa a ser excluída.
* **Resposta de Sucesso (200):**
    ```json
    {
      "message": "Tarefa excluída com sucesso"
    }
    ```
* **Resposta de Erro (404):**
    ```json
    {
      "message": "Tarefa não encontrada"
    }
    ```