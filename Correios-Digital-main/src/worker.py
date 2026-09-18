from workers import wsgi

from postoffice.presentation import criar_app


app = criar_app("dados")

Default = wsgi.entrypoint(app)
