import unittest

from party import app
from model import db, example_data, connect_to_db


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Test to see homepage"""

        result = self.client.get("/")
        self.assertIn("board games, rainbows, and ice cream sundaes", result.data)

    def test_no_rsvp_yet(self):
        """Test to see the RSVP form, but NOT the party details"""

        result = self.client.get("/")

        raise Exception("what is result?")

        self.assertIn("RSVP", result.data)
        self.assertNotIn("Party Details", result.data)

    def test_rsvp(self):
        """Once we RSVP, we should see the party details, but not the RSVP form"""

        result = self.client.post("/rsvp",
                                  data={'name': "Jane", 'email': "jane@jane.com"},
                                  follow_redirects=True)
        self.assertIn("Party Details", result.data)
        self.assertNotIn("RSVP", result.data)


class PartyTestsDatabase(unittest.TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        connect_to_db(app, "postgresql:///testdb")

        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    def test_games(self):
        """Test that the games page displays the game from example_data()"""

        result =  self.client.get("/games")
        self.assertIn("trains", result.data)


if __name__ == "__main__":
    unittest.main()
