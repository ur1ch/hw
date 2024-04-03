__all__ = ("app",)

from app import app
""""
how to start app
docker build . -t web
--no-cache if needed fresh follow for files after build

docker run -p 8000:8000 -it web 

"""