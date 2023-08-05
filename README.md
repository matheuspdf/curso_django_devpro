# curso_django_devpro 

Projeto desenvolvido no módulo 03 Django do [Site Dev Pro](https://www.dev.pro.br/)<br>
Os detalhes e anotações sobre o que foi praticado durante o curso estão disponíveis para consulta na minha página do [Notion](https://matheuspdf.notion.site/03-Django-DevPro-230b19c1354d427da77da23566e5aa19?pvs=4)

[![Python application](https://github.com/matheuspdf/curso_django_devpro/actions/workflows/django_ci.yml/badge.svg)](https://github.com/matheuspdf/curso_django_devpro/actions/workflows/django_ci.yml)

## Entrega contínua

* ### Pipenv
  * Como utilizar o pipenv para instalar e gerenciar as dependências de um projeto.


* ### Integração Pipenv Travis e Pyup
  * Realizada migração do Travis CI para o CI do Github Actions


* ### Setup de Projeto e Arquivo Manage
  * Ferramentas do django e como criar a 
  estrutura inicial de arquivos do projeto.


* ### Publicação no (~~Heroku~~)  |  Deploy Automático
  * Como publicar a aplicação na Plataforma Fly.io
  * Feita integração fly.io e Github Actions
  * [fly.io](https://curso-django-devpro.fly.dev/)
  
* ### Rodando Servidor no Pycharm
  * Como rodar o servidor local do django pelo Pycharm.

* ### Olá Django
   * iniciada aplicação django através do comando 'startapp'
   * integração contínua entre GA e fly.io
   * Primeira app criada

* ### Pytest Django
  * 'pytest-django'
  * configurado Pycharm para rodar o pytest
  * inserido linha de comando no arquivo de integração contínua

* ### Cobertura de Testes
  * Relatório de cobertura de testes. pytest --cov.


## Configurações de Projeto
Neste segundo capítulo, o objetivo foi desacoplar as configurações de instância do projeto e instalar ferramentas básicas de log, banco de dados e arquivos estáticos.
* ### Lib Python Decouple
  * separação das configurações de instância da aplicação.
* ### Secret Key
  * assinatura criptográfica
* ### Domínio e ALLOWED_HOSTS
  * configuração de domínio, servidor DNS e configuração de hosts permitidos.
* ### Endereço de Banco de Dados
  * configuração do endereço do banco de dados no servidor. (Postgre)
* ### Testando PostgreSQL no GitHub Actions - CI
  * Setup do servidor de CI para rodar os testes de forma similar ao ambiente de produção.
* ### Língua e Fuso Horário
  * configurado padrão de idioma e fuso horário.