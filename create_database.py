from appflexi import database, app
from appflexi.model import Photo, User

with app.app_context():
    database.create_all()