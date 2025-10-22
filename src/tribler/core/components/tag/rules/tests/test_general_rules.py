import pytest

from tribler.core.components.tag.rules.tag_rules import (
    delimiter_re,
    extension_re,
    extract_only_valid_tags,
    extract_tags,
    parentheses_re,
    square_brackets_re,
    tags_in_parentheses,
    tags_in_square_brackets,
)

DELIMITERS = [
    ('word1 word2 word3', ['word1', 'word2', 'word3']),
    ('word1,word2,word3', ['word1', 'word2', 'word3']),
    ('word1/word2/word3', ['word1', 'word2', 'word3']),
    ('word1|word2|word3', ['word1', 'word2', 'word3']),
    ('word1 /.,word2', ['word1', 'word2']),
]

SQUARE_BRACKETS = [
    ('[word1] [word2 word3]', ['word1', 'word2 word3']),
    ('[word1 [word2] word3]', ['word2']),
]

PARENTHESES = [
    ('(word1) (word2 word3)', ['word1', 'word2 word3']),
    ('(word1 (word2) word3)', ['word2']),
]

EXTENSIONS = [
    ('some.ext', ['ext']),
    ('some.ext4', ['ext4']),
    ('some', []),
    ('some. ext', []),
    ('some.ext ', []),
]


@pytest.mark.parametrize('text, words', DELIMITERS)
def test_delimiter(text, words):
    assert delimiter_re.findall(text) == words


@pytest.mark.parametrize('text, words', SQUARE_BRACKETS)
def test_square_brackets(text, words):
    assert square_brackets_re.findall(text) == words


@pytest.mark.parametrize('text, words', PARENTHESES)
def test_parentheses(text, words):
    assert parentheses_re.findall(text) == words


@pytest.mark.parametrize('text, words', EXTENSIONS)
def test_extension(text, words):
    # test regex
    assert extension_re.findall(text) == words


def test_tags_in_square_brackets():
    # test that tags_in_square_brackets rule works correctly with extract_tags function
    text = 'text [tag1, tag2] text1 [tag3|tag4] text2, (tag5, tag6)'
    expected_tags = {'tag1', 'tag2', 'tag3', 'tag4'}

    actual_tags = set(extract_tags(text, rules=[tags_in_square_brackets]))
    assert actual_tags == expected_tags


def test_tags_in_parentheses():
    # test that tags_in_parentheses rule works correctly with extract_tags function
    text = 'text (tag1, tag2) text1 (tag3|tag4) text2, [tag5, tag6]'
    expected_tags = {'tag1', 'tag2', 'tag3', 'tag4'}

    actual_tags = set(extract_tags(text, rules=[tags_in_parentheses]))
    assert actual_tags == expected_tags


def test_default_rules():
    # test that default_rules works correctly with extract_tags function
    text = 'text (tag1, tag2) text1 (tag3|tag4) text2, [tag5, tag6].ext'
    expected_tags = {'tag1', 'tag2', 'tag3', 'tag4', 'tag5', 'tag6', 'ext'}

    actual_tags = set(extract_tags(text))
    assert actual_tags == expected_tags


def test_extract_only_valid_tags():
    # test that extract_only_valid_tags extracts only valid tags
    assert set(extract_only_valid_tags('[valid-tag, in va li d]')) == {'valid-tag'}
