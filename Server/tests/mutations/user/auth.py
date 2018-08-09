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

