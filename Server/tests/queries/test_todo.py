from tests import BasicTestCase


class TestToDo(BasicTestCase):
    def test_todo(self):
        response = self.request(type="query",
                                call='todo(token: "{0}", orderBy: "type", searchString: "ti")'.format(self.access_token),
                                body='''
                                title
                                type
                                createdAt
                                milestones{
                                    name
                                    isCompleted
                                }
                                expiration
                                isCompleted
                                ''')

        self.assertEqual(type(response['todo'][0]['type']), str)
        self.assertEqual(type(response['todo'][0]['title']), str)
        self.assertEqual(type(response['todo'][0]['milestones']), list)
        self.assertEqual(type(response['todo'][0]['isCompleted']), bool)

