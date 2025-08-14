from django.core.management.base import BaseCommand
import uvicorn
# import gunicorn

class Command(BaseCommand):

    def handle(self, *args, **options):
        return uvicorn.run("uv.asgi:application",host="127.0.0.1",port=8000,reload=True)