from html.parser import HTMLParser
from urllib import parse


# Iterate through a HTML file and find all the <a href> links, and we only care about the start tags.
class LinkFinder(HTMLParser):

    # Override method
    # Initializer: Pass in base_url, homepage_url when create
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # Override method
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attributes, value) in attrs: # href = attribute, url = value
                if attributes == 'href':
                    # in case of relative url, we stitch the partial url with our base url to form the full url
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    # Links getter
    def page_links(self):
        return self.links

    # Override method
    def error(self, message):
        pass


finder = LinkFinder()  # indentation is important here
finder.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')
