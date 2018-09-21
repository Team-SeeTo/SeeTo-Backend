from tests import BasicTestCase


class TestQuickMemo(BasicTestCase):

    def test_new_memo(self):
        response = self.request(type="mutation",
                                call='newQuickmemo(token: "{0}", title: "{1}", body: "{2}")'
                                .format(self.access_token, "idea title", "idea body"),
                                body='''
                                     result{
                                     ... on ResponseMessageField{
                                     isSuccess
                                     message
                                     }
                                     }
                                     ''')

        self.assertEqual(response['newQuickmemo']['result']['message'], 'Quick memo upload success')

    def test_edit_memo(self):
        response = self.request(type="mutation",
                                call='editQuickmemo(token: "{0}", id: "{1}", update: "{2}")'
                                .format(self.access_token, str(self.quickmemo_id), "updated body"),
                                body='''
                                     result{
                                     ... on ResponseMessageField{
                                     isSuccess
                                     message
                                     }
                                     }
                                     ''')

        self.assertEqual(response['editQuickmemo']['result']['message'], 'Memo update success')

    def test_delete_memo(self):
        response = self.request(type="mutation",
                                call='deleteQuickmemo(token: "{0}", id: "{1}")'
                                .format(self.access_token, str(self.quickmemo_id)),
                                body='''
                                      result{
                                      ... on ResponseMessageField{
                                      isSuccess
                                      message
                                      }
                                      }
                                      ''')

        self.assertEqual(response['deleteQuickmemo']['result']['message'], 'Memo delete success')
