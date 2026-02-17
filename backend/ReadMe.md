Directory structure:
- backend (root)
- Dockerfile
- manage.py #
- README.md
- requirements.txt #

- api/ #
- - __init__.py
- - admin.py #
- - apps.py #
- - models.py #
- - tests.py #
- - views.py #
- - migrations/ #
- - - __init__.py

- apps/
- - about/
- - blog/
- - contact/
- - portfolio/
- - - __init__.py
- - - admin.py # allows default administrator page (/admin) to do CRUD by registering model via maintaining UI
- - - apps.py # configuration file to define this folder is Django app
- - - models.py # location to define DB table (model)
- - - tests.py # automative test code
- - - urls.py # is routing file that connects URL directions and view
- - - views.py # logic that receives request and returns a response
- - - migrations/ # location to save DB scheme changes log
- - - - __init__.py

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