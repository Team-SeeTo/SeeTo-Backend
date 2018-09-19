from tests import BasicTestCase


class TestProfile(BasicTestCase):
    def test_profile(self):
        response = self.request(type="query",
                                call='profile(token :"{0}")'.format(self.access_token),
                                body='''
                                ... on ProfileField{
                                email
                                username
                                rank
                                point
                                registerOn
                                }
                                ''')

        self.assertEqual(type(response['profile']['email']), str)
        self.assertEqual(type(response['profile']['username']), str)
        self.assertEqual(type(response['profile']['rank']), int)
        self.assertEqual(type(response['profile']['point']), int)

