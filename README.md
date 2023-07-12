# curso_django_devpro

Projeto desenvolvido no módulo 03 Django do [Site Dev Pro](https://www.dev.pro.br/)<br>
Os detalhes e anotações sobre o que foi praticado durante o curso estão disponíveis para consulta na minha página do [Notion](https://matheuspdf.notion.site/03-Django-DevPro-230b19c1354d427da77da23566e5aa19?pvs=4)

[![Python application](https://github.com/matheuspdf/curso_django_devpro/actions/workflows/django_ci.yml/badge.svg)](https://github.com/matheuspdf/curso_django_devpro/actions/workflows/django_ci.yml)

## Entrega contínua

* ### Pipenv
  * Pipfile
  * Pipfile.lock
  * Comandos
  * .bashrc

* ### Integração Pipenv Travis e Pyup
  * Realizada migração do Travis CI para o CI do Github Actions

* ### Setup de Projeto e Arquivo Manage
  * Ferramentas do django:
    * django-admin
    * startproject


* ### Publicação no Heroku / Deploy Automático
  * Deploy realizado no fly.io
  * Feita integração fly.io e Github Actions
  * [fly.io](https://curso-django-devpro.fly.dev/)
  
* ### Rodando Servidor no Pycharm
  * Configuração do Pycharm para rodar o django 

* ### Olá Django
   * iniciada aplicação django através do comando 'startapp'
   * integração contínua entre GA e fly.io

* ### Pytest Django
  * 'pytest-django'
  * configurado Pycharm para rodar o pytest
  * inserido linha de comando no arquivo de integração contínua

* ### Cobertura de Testes
  * pytest --cov