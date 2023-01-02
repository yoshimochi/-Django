from django.contrib.auth import get_user_model  # get_user_modelをインポート
from django.test import TestCase, Client, RequestFactory  # RequestFactoryをインポート

from snippets.models import Snippet
from snippets.views import top

UserModel = get_user_model()


class TopPageRenderSnippetsTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="top_secret_pass0001",
        )
        self.snippet = Snippet.objects.create(
            title="title1",
            code="print('hello')",
            description="description1",
            created_by=self.user,
        )

    def test_should_return_snippet_title(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.snippet.title)

    def test_should_return_username(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.user.username)