from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
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
  type = db.Column(db.String(10))
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
moodboosters_schema = MoodboosterSchema(many=True)

# with app.app_context():
#     db.create_all()

@app.route('/moodbooster', methods=['GET'])
def get_mbs():
    all_mbs = Moodboosters.query.all()
    result = moodboosters_schema.dump(all_mbs)
    return jsonify(result)

@app.route('/moodbooster/<id>', methods=['GET'])
def get_mb(id):
  mb = Moodboosters.query.get(id)
  return moodbooster_schema.jsonify(mb)

# Run Server
if __name__ == '__main__':
  app.run(debug=True)
