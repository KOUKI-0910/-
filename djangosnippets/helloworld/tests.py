from django.test import TestCase
from django.urls import resolve

from helloworld.views import top, snippet_new, snippet_edit, snippet_detail

class CreateSnippetTest(TestCase):
    def test_should_resolve_snippet_new(self):
        found = resolve('/helloworld/new/')
        self.assertEqual(snippet_new, found.func)


class SnippetDetailTest(TestCase):
    def test_should_resolve_snippet_detail(self):
        found = resolve('/helloworld/1/')
        self.assertEqual(snippet_detail, found.func)


class EditSnippetTest(TestCase):
    def test_should_resolve_snippet_edit(self):
        found = resolve('/helloworld/1/edit/')
        self.assertEqual(snippet_edit, found.func)