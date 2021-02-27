from flask_restful import Resource, reqparse, inputs

from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'description',
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'imageUrl',
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'isFavorite',
        type=inputs.boolean,
        required=True,
        help="This field cannot be left blank"
    )

    def get(self, title):
        item = ItemModel.find_by_name(title)
        if item:
            return item.get_json()
        return {"message": "Item not found"}, 404

    def post(self, title):
        if ItemModel.find_by_name(title):
            return {"message": "An item with name '{}' already exists".format(title)}, 400
        data = Item.parser.parse_args()
        item = ItemModel(title, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "an error occurred inserting the item"}, 500

        return item.get_json(), 201
