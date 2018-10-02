from tests import BasicTestCase


class TestToDo(BasicTestCase):
    def test_todo(self):
        response = self.request(type="query",
                                call='todo(token: "{0}", orderBy: "type", searchString: "ti")'.format(self.access_token),
                                body='''
                                ... on ToDoField{
                                id
                                title
                                type
                                createdAt
                                milestones{
                                    id
                                    name
                                    isCompleted
                                }
                                expiration
                                isCompleted
                                }
                                ''')

        self.assertEqual(type(response['todo'][0]['type']), str)
        self.assertEqual(type(response['todo'][0]['title']), str)
        self.assertEqual(type(response['todo'][0]['id']), str)

        self.assertEqual(type(response['todo'][0]['milestones']), list)
        self.assertEqual(type(response['todo'][0]['milestones'][0]['id']), str)
        self.assertEqual(type(response['todo'][0]['isCompleted']), bool)

