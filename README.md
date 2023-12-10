# Slowly - Trazendo a experiência tradicional de amigos postais para o discord
Projetado inicialmente como um backup para cartas trocadas, oferece uma experiência personalizada de correspondência para um servidor específico. Os usuários podem escrever, enviar e manter um registro das suas trocas, proporcionando uma abordagem única à comunicação digital.


## principais tecnologias
 - [discord.py](https://github.com/Rapptz/discord.py)
 - [dynaconf](https://github.com/dynaconf/dynaconf)
 - [Discord Webhook](https://discord.com/developers/docs/resources/webhook)

## installation

1. clone o repositório:

  ```bash
  git clone https://github.com/luan-gsm/slowly
  cd slowly
  ```


2. criar um ambiente virtual (opcional, mas recomendado):

  ```bash
  python -m venv .venv --prompt=venv
  source venv/bin/activate
  ```


3. instalar as dependências:

  ```bash
  pip install -r requirements.txt
  ```


4. configurar o ambiente:

  ```bash
  touch .secrets.toml
  ```

  dentro de `.secrets.toml` deve ter:
  ```toml
  [development]
  server_id = id do servidor
  channel_id = id do canal
  webhook = "url do webhook"
  token = "token do bot"

  [production]
  server_id = id do servidor
  channel_id = id do canal
  webhook = "url do webhook"
  token = "token do bot"
  ```


## rodando o programa

1. dentro do diretório do projeto (slowly):

  ```bash
  python -m slowly
  ```
