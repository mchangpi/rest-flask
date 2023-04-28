from flask import Flask

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair", 
                "price": 15.99
            }
        ]     
    }
]

@app.get("/stores")
def get_stores():
    return {"stores": stores}