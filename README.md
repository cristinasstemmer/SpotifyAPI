# Rankings de Artistas e Gêneros - Usando a API do Spotify

## Descrição

Este projeto é uma aplicação web que exibe um ranking de artistas pop e os gêneros musicais mais comuns usando a API do Spotify. A aplicação permite visualizar os artistas pop mais seguidos e a contagem de gêneros mais populares.

## Funcionalidades

- Exibe uma lista de artistas pop ordenados pelo número de seguidores.
- Mostra os 5 gêneros musicais mais comuns e a quantidade de artistas em cada gênero.

## Tecnologias Utilizadas

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **API:** Spotify Web API

## Pré-requisitos

Antes de rodar a aplicação, certifique-se de ter o Python e o Flask instalados. Você também precisa de um token de acesso válido da API do Spotify.

## Instalação

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/cristinasstemmer/SpotifyAPI.git
    cd seu-repositorio
    ```

2. **Instale as dependências do Python:**

    Instale Flask e Requests:

    ```bash
    pip install Flask requests
    ```
3. **Configure o token de acesso da API do Spotify:**

   No arquivo `main.py`, substitua o valor de `YOUR_TOKEN` pelo seu token de acesso da API do Spotify.

## Execução

1. **Inicie o servidor Flask:**

    ```bash
    python app.py
    ```

2. **Abra seu navegador e acesse:**

    ```
    http://127.0.0.1:5000/
    ```
