from app.models import *
import unittest
from datetime import datetime, timedelta
from config import dev
from app import create_app
import json

app = create_app(dev.DevConfig)


class BasicTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

        app.testing = True
        self.tester = app.test_client(self)

    def request(self, type, call, body):
        query = type + " {" + call + "{" + body + "}" + "}"

        response = self.tester.post('/graphql',
                                    data=json.dumps({"query": query}),
                                    content_type='application/json'
                                    )

        print(response.json)
        return dict(response.json)['data']

    def _create_fake_data(self):

        fake_user_1 = User(email="test@seeto.services",
                           username="test1",
                           password="admin1234",
                           rank=1,
                           point=100,
                           quick_memo=[fake_memo],
                           todo=[fake_todo],
                           ideas=[fake_idea],
                           my_items=[fake_item],
                           img_path="seeto.services/static/test1.jpg"
                           )

        fake_user_2 = User(email="test2@seeto.services",
                           username="test2",
                           password="admin1234",
                           rank=2,
                           point=99,
                           img_path="seeto.services/static/test2.jpg"
                           )

        fake_user_1.save()
        fake_user_2.save()

        fake_idea = Idea(title="title",
                         body="body",
                         author=fake_user_1)

        fake_memo = QuickMemo(title="title",
                              body="body")

        fake_item = StoreItem(name="name",
                              price=50)

        fake_todo = ToDo(title="title",
                         milestones=[
                             Milestone(name="milestone")
                         ],
                         expiration=datetime.now() + timedelta(days=5))

        fake_idea.save()
        fake_item.save()
        fake_memo.save()
        fake_todo.save()

    def _get_tokens(self):
        response = self.request(type="mutation",
                                call='auth(email:"test@seeto.services", password:"admin1234")',
                                body='''
                                     refreshToken
                                     accessToken
                                     message
                                     ''')

        response = response['auth']
        self.access_token = response['accessToken']
        self.refresh_token = response['refreshToken']

    def setUp(self):
        self._create_fake_data()
        self._get_tokens()

    def tearDown(self):
        User.objects.delete()
        Idea.objects.delete()
        QuickMemo.objects.delete()
        ToDo.objects.delete()
        StoreItem.objects.delete()
