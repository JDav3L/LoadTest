from app.routers import products, categories, carts, users, auth, accounts
from fastapi import FastAPI


app = FastAPI(
    title="E-commerce API for Load and Testing IT4B SECTION",
    version="1.0.0",
    
    swagger_ui_parameters={
        "syntaxHighlight.theme": "monokai",
        "layout": "BaseLayout",
        "filter": True,
        "tryItOutEnabled": True,
        "onComplete": "Ok"
    },
)


app.include_router(products.router)
app.include_router(categories.router)
app.include_router(carts.router)
app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(auth.router)
