from tests import BasicTestCase


class TestMirror(BasicTestCase):
    def test_mirror(self):
        response = self.request(type="query",
                                call='mirror(token :"{0}")'.format(self.access_token),
                                body='''
                                month{
                                    todo
                                    ideas
                                    totalPoint
                                }
                                week{
                                    todo
                                    ideas
                                    totalPoint
                                }
                                year{
                                    todo
                                    ideas
                                    totalPoint
                                }
                                ''')

        for period in ['month', 'week', 'year']:
            self.assertEqual(type(response['mirror'][period]['totalPoint']), int)
            self.assertEqual(type(response['mirror'][period]['todo']), int)
            self.assertEqual(type(response['mirror'][period]['ideas']), int)



