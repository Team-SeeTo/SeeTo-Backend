from tests import BasicTestCase


class TestToDo(BasicTestCase):

    def test_new_todo(self):
        response = self.request(type="mutation",
                                call='newTodo(token: "{0}", title: "{1}", type: {2}, milestones: {3}, expiration: "{4}")'
                                .format(self.access_token, "title", "STANDARD", '["1", "2"]', "2019-01-01"),
                                body='''
                                     result{
                                     ... on ResponseMessageField{
                                     isSuccess
                                     message
                                     }
                                     }
                                     ''')

        self.assertEqual(response['newTodo']['result']['message'], 'Todo upload success')

    def test_edit_todo(self):
        response = self.request(type="mutation",
                                call='editTodo(token: "{0}", id: "{1}", newTitle: "{2}")'
                                .format(self.access_token, str(self.todo_id), "updated body"),
                                body='''
                                     result{
                                     ... on ResponseMessageField{
                                     isSuccess
                                     message
                                     }
                                     }
                                     ''')

        self.assertEqual(response['editTodo']['result']['message'], 'Todo update success')

    def test_delete_todo(self):
        response = self.request(type="mutation",
                                call='deleteTodo(token: "{0}", id: "{1}")'
                                .format(self.access_token, str(self.todo_id)),
                                body='''
                                      result{
                                      ... on ResponseMessageField{
                                      isSuccess
                                      message
                                      }
                                      }
                                      ''')

        self.assertEqual(response['deleteTodo']['result']['message'], 'Todo delete success')

    def test_complete_todo(self):
        response = self.request(type="mutation",
                                call='completeTodo(token: "{0}", id: "{1}")'
                                .format(self.access_token, str(self.todo_id)),
                                body='''
                                      result{
                                      ... on ResponseMessageField{
                                      isSuccess
                                      message
                                      }
                                      }
                                      ''')

        self.assertEqual(response['completeTodo']['result']['message'], 'Todo complete success')
