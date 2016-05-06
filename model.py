from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///testdb"):
    #actual games db uri > "postgresql:///games" 
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Example data for the test database."""

    t2r = Game(game_id="1", name="Ticket To Ride", description="trains")
    pg = Game(game_id="2", name="Power Grid", description="power")
    al = Game(game_id="3", name="Amazing Labyrinth", description="maze")

    db.session.add_all([t2r, pg, al])
    db.session.commit()

if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print "Connected to DB."