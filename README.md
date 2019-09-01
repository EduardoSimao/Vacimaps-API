# Vacimaps

Instruções para preparar o ambiente:
*  Criar um  ambiente virtual (venv)
    ```bash
    virtualenv venv
    ```
* Acessar o ambiente virtual **venv**
    ```bash
    source venv/bin/activate
    ```
* Saindo do ambiente virtual **venv**
    ```bash
    deactivate
    ```

* Rode o projeto
    * Executar:
    ```bash
    python run.py
    ```

### Endpoints: ###

```bash
GET - Retorna dados do usuário
/usuario
```
```bash
POST - Cadastra um usuário
/usuario

{
    "nome": "Usuário1", 
    "email": "usuario@email.com", 
    "senha": "1234"
}
```
```bash
PUT - Atualiza informações do usuário logado
/usuário

{
  "dt_nascimento": "1996-01-17",
  "email": "teste@email.com",
  "nome": "TestePUT"
}
```
```bash
POST - Enviar o email pra redefinir senha
/forgot_password

{ 
    "email": "usuario@email.com", 
}
```
```bash
PUT - Redefinir a senha
/reset_password

{ 
    "senha": "novaSenha", 
}
```
```bash
GET - Retorna dados da vacina do usuario
/usuario/vacina/<id_vacina>
```
```bash
POST - Cadastra uma vacina
/usuario/vacina

{
    "id_vacina": 1,
    "ds_local_vacina": "Postinho de mongaguá",
    "data_vacina": "2019-01-17"
}

```
```bash
PUT - Atualiza informações da vacina
/usuario/vacina/<id_vacina>

{
    "ds_local_vacina": "Postinho de mongaguá vila atlantica",
    "data_vacina": "2019-02-17"
}
```
```bash
DELETE - Deleta vacina do usuario
/usuario/vacina/<id_vacina>
```
```bash
PUT - Trocar Senha Usuario
/usuario/change_password

{
    "senha_atual": "senha_atual",
    "nova_senha": "nova_senha"
}
```

### Instruções Login usando o Postman ###

```bash

POST - Gerar token e adicionar no Headers
/login

* Aba Body:

    Selecionar o tipo *Raw* e trocar de *Text* para *JSON (application/json)*

    {
    "email": "usuario@email.com", 
    "password": "1234"
    }

    clicar em send e copiar a token gerada

* Aba Headers:

    key -> token
    value -> Token gerada
```
