# -*- coding: utf-8 -*-

import os
import pytest


@pytest.fixture()
def change_test_dir(request):
    os.chdir(request.fspath.dirname)
    yield
    os.chdir(request.config.invocation_dir)


@pytest.fixture()
def text(change_test_dir):
    with open('./Kolobok.md', mode='r') as output_file:
        return output_file.read()


def test_has_header(text):
    assert '# Сказка про Колобка' in text

def test_has_subheader_kolobok_appeared(text):
    assert '## 1. Как Колобок появился' in text

def test_has_subheader_kolobok_runaway(text):
    assert '## 2. Как Колобок убежал' in text

def test_has_subheader_kolobok_faced_animals(text):
    assert '## 3. Встреча со зверями' in text

def test_has_subheader_kolobok_faced_hare(text):
    assert '### 3.1 Заяц' in text

def test_has_subheader_kolobok_faced_wolf(text):
    assert '### 3.2 Серый волк' in text

def test_has_subheader_kolobok_faced_bear(text):
    assert '### 3.4 Медведь' in text

def test_has_subheader_kolobok_faced_fox(text):
    assert '## 4. Финал. Встреча с Лисой' in text
