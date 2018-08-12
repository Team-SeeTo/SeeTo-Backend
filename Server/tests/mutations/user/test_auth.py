from tests import BasicTestCase


class TestAuth(BasicTestCase):

    def test_auth(self):
        response = self.request(type="mutation",
                                call='auth(email:"test@seeto.services", password:"admin1234")',
                                body='''
                                     refreshToken
                                     accessToken
                                     message
                                     ''')

        self.assertEqual(response['auth']['message'], 'Login Success')

    def test_refresh(self):
        response = self.request(type="mutation",
                                call='refresh(token: "{}")'.format(self.refresh_token),
                                body='''
                                     accessToken
                                     message
                                     ''')

        self.assertEqual(response['refresh']['message'], 'Refresh success')

