# runserver.py
import os
import uvicorn

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vigyanraksha_project.settings")

if __name__ == "__main__":
    uvicorn.run("vigyanraksha_project.asgi:application", host="127.0.0.1", port=8000, reload=True)
