from tests import BasicTestCase


class TestTimeLine(BasicTestCase):
    def test_timeline(self):
        response = self.request(type="query",
                                call='timeline(token: "{0}")'.format(self.access_token),
                                body='''
                     ... on TimeLineField{
                     date
                     todo{
                        totalPoint
                     }
                     ideas{
                        totalPoint
                     }
                     totalPoint
                     }
                     ''')

        self.assertEqual(type(response['timeline']['totalPoint']), int)
        self.assertEqual(type(response['timeline']['todo']['totalPoint']), int)
        self.assertEqual(type(response['timeline']['ideas']['totalPoint']), int)

    def test_specific_timeline(self):
        response = self.request(type="query",
                                call='timeline(token: "{0}", date:"2018-10-08")'.format(self.access_token),
                                body='''
                     ... on TimeLineField{
                     date
                     todo{
                        totalPoint
                     }
                     ideas{
                        totalPoint
                     }
                     totalPoint
                     }
                     ''')

        self.assertEqual(type(response['timeline']['totalPoint']), int)
        self.assertEqual(type(response['timeline']['todo']['totalPoint']), int)
        self.assertEqual(type(response['timeline']['ideas']['totalPoint']), int)
