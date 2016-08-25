# Curso Welcome to the Django

Deploy em:
---
https://eventex-fhferreira.herokuapp.com/


Heroku
---

heroku login  
heroku apps:create eventex-fhferreira  
heroku plugins:install heroku-config  
> criar seu arquivo .env na raiz da aplicação com suas configurações de ambiente

heroku config:push  
git push heroku master --force  
