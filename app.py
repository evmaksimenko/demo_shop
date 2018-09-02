from flask import Flask, render_template, redirect, url_for
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


def chunks(seq, n):
    return (list(seq[i:i+n]) for i in range(0, len(seq), n))


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(8), index=True)
    name = db.Column(db.String(128), index=True)
    description = db.Column(db.String(1024))
    price = db.Column(db.Float)

    def __repr__(self):
        return '<Item {}>'.format(self.name)


@app.route('/')
def index():
    all_items = Item.query.all()
    items = list(chunks(all_items, 5))
    return render_template('index.html', items=items)


@app.route('/items/<string:item_id>')
def show_item_info(item_id):
    item = Item.query.filter_by(code=item_id).first_or_404()
    desc = (item.description).split('\n')
    return render_template('item.html', item=item, desc=desc, title=item.name[:20])


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
