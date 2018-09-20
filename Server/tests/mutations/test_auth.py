from tests import BasicTestCase


class TestAuth(BasicTestCase):

    def test_auth(self):
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

        self.assertEqual(response['auth']['result']['message'], 'Login Success')

    def test_refresh(self):
        response = self.request(type="mutation",
                                call='refresh(refreshToken: "{}")'.format(self.refresh_token),
                                body='''
                                     result{
                                     ... on RefreshField{
                                     accessToken
                                     message
                                     }
                                     }
                                     ''')

        self.assertEqual(response['refresh']['result']['message'], 'Refresh success')

