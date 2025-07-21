import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


        # test the title is on the home page
        html = response.get_data(as_text=True)
        assert "<title>Home – Alan Mong</title>" in html

        # test the nav bar is present
        assert "<nav class=\"navbar navbar-expand-md navbar-dark bg-black\">" in html

        # test that bootstrap is present
        assert "<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js\"></script>" in html
    
    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        self.assertEqual(response.status_code, 200)

        # check the api is sending responses with json and get info in json
        assert response.is_json
        json = response.get_json()

        # intial tests of the JSON
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        # test both post and get requests against the api
        # post test
        response = self.client.post("/api/timeline_post", data={
            'name':'John Doe',
            'email':"john@example.com",
            'content':"Hello World"
        })
        assert response.is_json
        json = response.get_json()
        assert json['content'] == 'Hello World' and json['email'] == 'john@example.com' and json['name'] == 'John Doe'

        # get test
        response = self.client.get()
        self.assertEqual(response.status_code, 200)

        # testing the html code, such as bootstrap is present.
        html = self.client.get("/timeline").get_data(as_text=True)
        assert "<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js\"></script>" in html
        assert "<title>Timeline – Alan Mong</title>" in html

    
    def test_malformed_timeline_post(self):
        # missing name
        response = self.client.post("/api/timeline_post", data={
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid name", response.get_data(as_text=True))

        # empty content
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": ""
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid content", response.get_data(as_text=True))

        # bad email
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "not-an-email",
            "content": "Hello world, I'm John!"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid email", response.get_data(as_text=True)) 
        
        
