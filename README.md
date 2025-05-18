# Chat em Tempo Real com FastAPI
![Image](https://github.com/user-attachments/assets/15aa1ba4-678b-4d95-b3f2-48cb989d31e6)
Este projeto é um chat em tempo real construído com FastAPI (Python) no backend e HTML/JavaScript no frontend.

## Pré-requisitos

```bash
# Certifique-se de ter Python 3.7+ instalado
python --version
# Certifique-se de ter pip instalado
pip --version
```

## Configuração

1.  **Crie o arquivo `.env` na raiz do projeto:**

    ```bash
    touch .env
    ```

2.  **Edite o arquivo `.env` e adicione as variáveis de ambiente:**

    ```env
    SECRET_KEY=<SUA_CHAVE_SECRETA_AQUI>
    ALGORITHM=<ALGORITMO_DE_ENCRIPTAÇÃO_AQUI>
    DATABASEPATH=<CAMINHO_PARA_O_SEU_ARQUIVO_DE_BANCO_DE_DADOS_AQUI>
    ```

    **Substitua os placeholders** `<SUA_CHAVE_SECRETA_AQUI>`, `<ALGORITMO_DE_ENCRIPTAÇÃO_AQUI>` e `<CAMINHO_PARA_O_SEU_ARQUIVO_DE_BANCO_DE_DADOS_AQUI>` pelos seus valores desejados.

## Instalação das Dependências

1.  **Navegue até a raiz do projeto:**

    ```bash
    cd <CAMINHO_PARA_A_RAIZ_DO_SEU_PROJETO>
    ```

2.  **Instale as dependências do backend:**

    ```bash
    pip install -r requirements.txt
    ```

## Iniciando a API (Backend)

2.  **Execute o comando para iniciar o servidor FastAPI:**

    ```bash
     fastapi dev backend/main.py
    ```

    A API estará disponível em `http://127.0.0.1:8000`.

## Acessando o Frontend

1.  **Abra seu navegador web.**
2.  **Utilize a função "Abrir Arquivo"** (geralmente Ctrl+O ou Cmd+O) do seu navegador.
3.  **Navegue até a raiz do seu projeto e selecione o arquivo `index.html`.**

    ```
    <CAMINHO_PARA_A_RAIZ_DO_SEU_PROJETO>/index.html
    ```

    O frontend se conectará automaticamente à API em execução.

## Bibliotecas Utilizadas

As dependências do backend estão listadas no arquivo `requirements.txt`.

