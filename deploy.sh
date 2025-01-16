#!/bin/bash

# Navegue até o diretório do projeto
cd /caminho/para/seu/projeto

# Atualize o repositório
git pull origin main

# Instale as dependências
pip install -r requirements.txt

# Reinicie o serviço (ajuste conforme necessário)
sudo systemctl restart seu-servico
