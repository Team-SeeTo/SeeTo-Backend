from tests import BasicTestCase
import datetime


class TestIdeas(BasicTestCase):
    def test_ideas(self):
        response = self.request(type="query",
                                call='ideas(token: "{0}")'.format(self.access_token),
                                body='''
                                ... on IdeasField{
                                        author
                                        title
                                        body
                                        createdAt
                                        upvoter
                                        comments{
                                           author
                                           body
                                        }
                                    }
                                ''')

        self.assertEqual(type(response['ideas'][0]['author']), str)
        self.assertEqual(type(response['ideas'][0]['title']), str)
        self.assertEqual(type(response['ideas'][0]['body']), str)
        self.assertEqual(type(response['ideas'][0]['upvoter']), list)
        self.assertEqual(type(response['ideas'][0]['comments']), list)
