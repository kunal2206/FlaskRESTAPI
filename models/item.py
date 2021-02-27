from db import collection


class ItemModel:
    def __init__(self, title, description, price, imageUrl, isFavorite):
        self.title = title
        self.description = description
        self.price = price
        self.imageUrl = imageUrl
        self.isFavorite = isFavorite

    def get_json(self):
        return {
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "imageUrl": self.imageUrl,
            "isFavorite": self.isFavorite
        }

    @classmethod
    def find_by_name(cls, title):
        item = collection.find_one({"title": title})
        return cls(item['title'], item['description'], item['price'], item['imageUrl'], item['isFavorite']) if item else None

    def save_to_db(self):
        collection.insert_one({
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "imageUrl": self.imageUrl,
            "isFavorite": self.isFavorite
        })

    def delete_from_db(self):
        pass
