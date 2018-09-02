from flask import render_template
from app.main import app
from app.models import Item


def chunks(seq, n):
    return (list(seq[i:i+n]) for i in range(0, len(seq), n))


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