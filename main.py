"""
Created by Epic at 9/25/20
"""
from sanic import Sanic

app = Sanic(__name__)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)
