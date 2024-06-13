# Projeto Cachaçaria Dom Wilmar
Sistema para coleção de cachaças

Bem-vindo ao Sistema de Coleção de Cachaças! Este projeto foi desenvolvido para entusiastas da cachaça que desejam organizar, explorar e compartilhar suas coleções de forma eficiente e envolvente.

## Funcionalidades Principais

- **Cadastro de Cachaças:** Registre detalhes importantes sobre cada cachaça, como nome, marca, ano de fabricação, origem, teor alcoólico.

- **Galeria Visual:** Faça upload de imagens das suas garrafas para uma experiência visual atraente e fácil identificação.

## Como rodar o projeto

- Clonagem do Repositório:
  
```bash
git clone https://github.com/FranciscoGabrielCavalcanteCandido/cachacariadomwilmar.git
```

- Na pasta raiz do projeto executar os seguintes comandos:

```bash
python manage.py runserver
```
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
```bash
pip install crispy-bootstrap5
```

- Comandos para rodar no docker:

```bash
docker build -t cachacaria .
```
```bash
docker run -d -p 8000:8000 --name django cachacaria
```