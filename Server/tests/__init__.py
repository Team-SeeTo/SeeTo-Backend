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
        fake_user_2 = User(email="test2@seeto.services",
                           username="test2",
                           password="admin1234",
                           point=99
                           ).save()

        fake_user_1 = User(email="test@seeto.services",
                           username="test1",
                           password="admin1234",
                           point=100
                           ).save()

        fake_idea = Idea(title="title",
                         body="body",
                         author=fake_user_1,
                         category="test",
                         upvoter=[fake_user_1],
                         comments=[Comment(author=fake_user_2, body="comment test")])

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

        fake_user_1.update(quick_memo=[fake_memo],
                           todo=[fake_todo],
                           ideas=[fake_idea],
                           my_items=[fake_item])

        self.idea_id = fake_idea.id
        self.todo_id = fake_todo.id
        self.milestone_id = fake_todo.milestones[0].id
        self.quickmemo_id = fake_memo.id

    def _get_tokens(self):
        response = self.request(type="mutation",
                                call='auth(email:"test@seeto.services", password:"admin1234")',
                                body='''
                                     result{
                                     ... on AuthField{
                                     refreshToken
                                     accessToken
                                     message
                                     }
                                     }
                                     ''')

        response = response['auth']
        self.access_token = response['result']['accessToken']
        self.refresh_token = response['result']['refreshToken']

    def setUp(self):
        self._create_fake_data()
        self._get_tokens()

    def tearDown(self):
        User.objects.delete()
        Idea.objects.delete()
        QuickMemo.objects.delete()
        ToDo.objects.delete()
        StoreItem.objects.delete()
        UserLog.objects.delete()
