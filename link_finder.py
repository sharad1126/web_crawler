from six.moves.html_parser import HTMLParser
from urlparse import urlparse

class linkFinder(HTMLParser):

	def __init__(self, base_url, page_url):
		super().__init__()
		self.base_url = base_url
		self.page_url = page_url
		seld.links = set()

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for (attribute, value) in attrs:
				if attribute == 'href':
					url = parse.urljoin(self.base_url, value)
					self.links.add(url)

	def page_links(self):
		return self.links

	def error(self, message):
		pass



	