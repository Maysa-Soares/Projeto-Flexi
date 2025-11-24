from appflexi import database, app
from appflexi.models import Photo, User

with app.app_context():
    database.create_all()