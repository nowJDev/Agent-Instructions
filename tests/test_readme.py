# 한·영 README의 언어 전환·기존 주소·대표 이미지와 누락 반례를 검증한다.
from html.parser import HTMLParser
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET

from test_documentation import anchor_ids, link_errors
from test_owned_skill_packages import prose_only


ROOT = Path(__file__).resolve().parents[1]
LEGACY_ANCHORS = {
    '무엇에-쓰는-건가요', '시작하기',
    '이미-쓰고-있는-ai에게-규칙을-알려-주려면',
    'windows에서-실행할-ai-도구까지-준비하려면',
    'ai가-일하는-순서', '파일들은-어떤-역할을-하나요',
    '쓰는-ai가-다르면-어떻게-하나요', '낯선-말은-이렇게-읽으세요',
    '더-알고-싶을-때-찾는-문서',
}
HEROES = {'assets/readme/hero-light.svg', 'assets/readme/hero-dark.svg'}


class ReadmeHTMLLinks(HTMLParser):
    """Collect only the HTML links and picture resources used by our READMEs."""

    def __init__(self, text):
        super().__init__()
        self.links = []
        self.images = []
        self.feed(prose_only(text))

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])
        elif tag == 'img':
            self.images.append(attrs)
            if attrs.get('src'):
                self.links.append(attrs['src'])
        elif tag == 'source' and attrs.get('srcset'):
            self.links.extend(item.strip().split()[0]
                              for item in attrs['srcset'].split(',') if item.strip())


def html_link_errors(root, relative, text):
    links = ReadmeHTMLLinks(text).links
    return link_errors(root, relative, '\n'.join('[resource](<' + target + '>)' for target in links))


class ReadmeTests(unittest.TestCase):
    def test_language_navigation_and_legacy_anchors(self):
        for filename, other in (('README.md', 'README.en.md'), ('README.en.md', 'README.md')):
            with self.subTest(filename=filename):
                text = (ROOT / filename).read_text(encoding='utf-8')
                self.assertIn(other, ReadmeHTMLLinks(text).links)
                self.assertEqual(html_link_errors(ROOT, Path(filename), text), [])
        text = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertTrue(LEGACY_ANCHORS <= anchor_ids(text))
        setup = text.index('<a id="windows에서-실행할-ai-도구까지-준비하려면"></a>')
        self.assertLess(setup, text.index('<details>'))

    def test_picture_resources_and_accessible_fallback(self):
        for filename in ('README.md', 'README.en.md'):
            with self.subTest(filename=filename):
                text = (ROOT / filename).read_text(encoding='utf-8')
                html = ReadmeHTMLLinks(text)
                self.assertTrue(HEROES <= set(html.links))
                fallback = [img for img in html.images if img.get('src') in HEROES]
                self.assertEqual(len(fallback), 1)
                self.assertTrue(fallback[0].get('alt', '').strip())
                self.assertEqual(html_link_errors(ROOT, Path(filename), text), [])

    def test_missing_theme_fallback_and_language_link_are_reported(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'light.svg').write_text('<svg/>', encoding='utf-8')
            good = '<picture><source srcset="light.svg 1x"><img src="light.svg" alt="Flow"></picture>'
            self.assertEqual(html_link_errors(root, Path('README.md'), good), [])
            broken = good.replace('srcset="light.svg 1x"', 'srcset="dark.svg 1x, other.svg 2x"')
            broken = broken.replace('src="light.svg"', 'src="fallback.svg"')
            broken += '<a href="README.en.md">English</a>'
            self.assertEqual(html_link_errors(root, Path('README.md'), broken),
                             ['dark.svg', 'other.svg', 'fallback.svg', 'README.en.md'])
            examples = '`<img src="inline.svg">`\n```html\n<img src="example.svg">\n```'
            self.assertEqual(html_link_errors(root, Path('README.md'), examples), [])

    def test_hero_svgs_are_static_and_self_contained(self):
        for relative in sorted(HEROES):
            with self.subTest(relative=relative):
                svg = ET.parse(ROOT / relative).getroot()
                self.assertEqual(svg.tag, '{http://www.w3.org/2000/svg}svg')
                self.assertEqual(svg.get('viewBox'), '0 0 1200 300')
                for element in svg.iter():
                    self.assertNotIn(element.tag.rsplit('}', 1)[-1],
                                     {'script', 'image', 'foreignObject', 'animate', 'animateTransform'})
                    for name, value in element.attrib.items():
                        if name.rsplit('}', 1)[-1] == 'href':
                            self.assertTrue(value.startswith('#'), value)
                self.assertTrue(svg.find('{http://www.w3.org/2000/svg}title').text)
                self.assertTrue(svg.find('{http://www.w3.org/2000/svg}desc').text)


if __name__ == '__main__':
    unittest.main()
