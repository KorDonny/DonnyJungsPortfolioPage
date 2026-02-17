Directory structure:
- backend (root)
- Dockerfile
- manage.py #
- README.md
- requirements.txt #

- api/ #
- - __init__.py
- - admin.py # allows default administrator page (/admin) to do CRUD by registering model via maintaining UI !Removed due to no use
- - apps.py # configuration file to define this folder is Django app
- - models.py # location to define DB table (model) !Removed due to no use
- - urls.py # is routing file that connects URL directions and view
- - migrations/ # location to save DB scheme changes log !Removed due to no use
- - - __init__.py

- - tests/ # automative test code list

- - v1/ # 
- - - __init__.py
- - - views.py # logic that receives request and returns a response
- - - schemas.py # 
- - - urls.py # 

- services/
- - __init__.py
- - protects_store.py (skeleton json)
- - signed_assets.py ()

- common/
- - aws/
- - - cf_sign.py # encrpyting and sigining into AWS CloudFront (CDN)
- - - secrets.py # get secret json from CloudFront
- - logging/
- - middleware/
- - utils/

- config/
- - __init__.py
- - asgi.py
- - urls.py
- - wsgi.py
- - settings/
- - - __init__.py
- - - base.py
- - - local.py
- - - prod.py