from app.main import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(8), index=True)
    name = db.Column(db.String(128), index=True)
    description = db.Column(db.String(1024))
    price = db.Column(db.Float)

    def __repr__(self):
        return '<Item {}>'.format(self.name)
