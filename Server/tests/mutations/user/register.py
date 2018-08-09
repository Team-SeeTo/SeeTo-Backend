from tests import BasicTestCase


class TestRegister(BasicTestCase):
    def setUp(self):
        pass

    def test_register(self):
        response = self.request(method=self.tester.post,
                                query='''mutation{
                                            register(email:"test@seeto.services", username: "lewis", password:"admin1234"){
                                                message
                                            }
                                        }''')

        self.assertEqual(response['register']['message'], 'Successfully registered')