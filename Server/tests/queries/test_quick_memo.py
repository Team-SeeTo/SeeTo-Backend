from tests import BasicTestCase


class TestToDo(BasicTestCase):
    def test_todo(self):
        response = self.request(type="query",
                                call='quickMemo(token: "{0}")'.format(self.access_token),
                                body='''
                                ... on QuickMemoField{
                                title
                                body
                                }
                                ''')

        self.assertEqual(type(response['quickMemo'][0]['body']), str)
        self.assertEqual(type(response['quickMemo'][0]['title']), str)
