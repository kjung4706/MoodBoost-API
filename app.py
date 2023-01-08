from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.sql.expression import func
import os

# init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'moodboost.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init db
db = SQLAlchemy(app)

# init ma
ma = Marshmallow(app)


# moodboosters class/model
class Moodboosters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String())
    message = db.Column(db.String())

    def __init__(self, id, type, message):
        self.id = id
        self.type = type
        self.message = message


# moodbooster schema
class MoodboosterSchema(ma.Schema):
    class Meta:
        fields = ('id', 'type', 'message')


# init schema
moodbooster_schema = MoodboosterSchema()


@app.errorhandler(Exception)
def handle_error(error):
    return jsonify({'error': 'Invalid parameters or URL NotFound'})


@app.route('/', methods=['GET'])
def get_mb():
    mb = Moodboosters.query.order_by(func.random()).first()
    return moodbooster_schema.jsonify(mb)


@app.route('/id=<id>', methods=['GET'])
def get_mb_id(id):
    mb = Moodboosters.query.get_or_404(id)
    return moodbooster_schema.jsonify(mb)


@app.route('/type=<type>', methods=['GET'])
def get_mb_type(type):
    if type not in ['joke', 'motivate']:
        abort(404)
    mb = Moodboosters.query.filter_by(type=type).order_by(func.random()).first()
    return moodbooster_schema.jsonify(mb)


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
