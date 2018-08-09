from tests import BasicTestCase


class TestAuth(BasicTestCase):

    def test_auth(self):
        response = self.request(method=self.tester.post,
                                query='''mutation{
                                            auth(email:"test@seeto.services", password:"admin1234"){
                                                refreshToken
                                                accessToken
                                                message
                                            }
                                        }''')

        self.assertEqual(response['auth']['message'], 'Login Success')

    def test_refresh(self):
        query = '''mutation{
                      refresh(token: "_"){
                          accessToken
                          message
                      }
                   }'''
        query = query.replace('_', self.refresh_token)

        response = self.request(method=self.tester.post,
                                query=query)

        self.assertEqual(response['refresh']['message'], 'Refresh success')

