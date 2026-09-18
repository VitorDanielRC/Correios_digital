from workers import WorkerEntrypoint, wsgi

_app = None


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        global _app

        if _app is None:
            from postoffice.presentation import criar_app

            _app = criar_app("dados")

        return await wsgi.fetch(_app, request, self.env)
