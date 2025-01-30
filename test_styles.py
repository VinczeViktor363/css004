import pytest

def test_html_lang():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        assert '<html lang="hu">' in content, "Az oldal nyelve nem magyar!"

def test_html_charset():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        assert '<meta charset="UTF-8">' in content, "A karakterkódolás nem UTF-8!"

def test_html_css_link():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        assert '<link rel="stylesheet" type="text/css" href="style.css">' in content, "A CSS fájl nincs linkelve!"

def test_footer_content():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'Készítette: Sallai András' in content, "A footer nem tartalmazza a nevemet!"
        assert 'Informatika' in content, "A footer nem tartalmazza az osztályomat!"
        assert '2025. január 30.' in content, "A footer nem tartalmazza a dátumot!"

def test_css_container_style():
    with open('style.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert '.container {' in content, "Nincs .container osztály a CSS-ben!"
        assert 'margin: 15%;' in content, "A .container osztály nem tartalmaz 15%-os margót!"

def test_headings_centered():
    with open('style.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'text-align: center;' in content, "A fejezetcímek nincsenek középre igazítva!"

def test_h2_right_aligned():
    with open('style.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'text-align: right;' in content, "A h2 elem nem jobbra van igazítva!"

def test_paragraph_justified():
    with open('style.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'text-align: justify;' in content, "A bekezdések nincsenek sorkizárva!"
