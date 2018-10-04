from tests import BasicTestCase
import datetime


class TestIdeas(BasicTestCase):
    def test_ideas(self):
        response = self.request(type="query",
                                call='ideas(token: "{0}")'.format(self.access_token),
                                body='''
                                ... on IdeasField{
                                        id
                                        author
                                        title
                                        body
                                        createdAt
                                        upvoter
                                        voteChecked
                                        comments{
                                           commentCount
                                           comments{
                                              author
                                              body
                                           }
                                        }
                                    }
                                ''')

        self.assertEqual(type(response['ideas'][0]['author']), str)
        self.assertEqual(type(response['ideas'][0]['title']), str)
        self.assertEqual(type(response['ideas'][0]['body']), str)
        self.assertEqual(type(response['ideas'][0]['upvoter']), int)
        self.assertEqual(response['ideas'][0]['upvoter'], True)
        self.assertEqual(type(response['ideas'][0]['comments']['commentCount']), int)
        self.assertEqual(type(response['ideas'][0]['comments']['comments']), list)

        idea_id = response['ideas'][0]['id']

        response = self.request(type="query",
                                call='ideas(token: "{0}", view: "{1}")'.format(self.access_token, idea_id),
                                body='''
                                ... on IdeasField{
                                        id
                                        author
                                        title
                                        body
                                        createdAt
                                        upvoter
                                        voteChecked
                                        comments{
                                           commentCount
                                           comments{
                                              author
                                              body
                                           }
                                        }
                                    }
                                ''')
        print("VIEW", response)
        self.assertEqual(type(response['ideas'][0]['author']), str)
        self.assertEqual(type(response['ideas'][0]['title']), str)
        self.assertEqual(type(response['ideas'][0]['body']), str)
        self.assertEqual(type(response['ideas'][0]['upvoter']), int)
        self.assertEqual(response['ideas'][0]['upvoter'], True)
        self.assertEqual(type(response['ideas'][0]['comments']['commentCount']), int)
        self.assertEqual(type(response['ideas'][0]['comments']['comments']), list)