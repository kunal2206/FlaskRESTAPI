from flask import Flask
from flask_restful import Api

from resources.item import Item

app = Flask(__name__)
app.secret_key = 'kunal@22061994'
api = Api(app)

api.add_resource(Item, '/item/<string:title>')

if __name__ == "__main__":
    app.run(port=5000, debug=True)



