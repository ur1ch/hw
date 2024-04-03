from fastapi import FastAPI, APIRouter, status
from fastapi.responses import HTMLResponse

from views.hello import router as router_hello
from views.items import router as router_items
from views.users import router as router_users

app = FastAPI()
app.include_router(router_hello)
app.include_router(router_items)
app.include_router(router_users)


@app.get("/")
def index_page():
    return {"message": "Hello World"}


@app.get("/demo_html", response_class=HTMLResponse)
def demo_html():
    return """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
        <html>
        <head>
        <title>Title</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        </head>
        <body>
        <p>Разум — это путь, путь - судьба, а это просто труляля</p>
        </body> 
        </html>
    """


@app.get("/ping/",
         responses={
             status.HTTP_200_OK: {
                 "content": {
                     "aplication/json": {
                         "message": "pong"
                     },
                 },
             },
         },
         )
def ping():
    return {"message": "pong"}
