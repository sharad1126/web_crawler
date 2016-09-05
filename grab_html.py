from urllib2 import urlopen
from link_finder import LinkFinder
from general import *

class grab_html:

	project_name = ''
	base_url = ''
	domain_name = ''
	queue_file = ''
	crawled_file = ''
	queue = set()
	crawled = set()

	def __init__(self, project_name, base_url, domain_name):
		grab_html.project_name = project_name
		grab_html.base_url = base_url
		grab_html.domain_name = domain_name
		grab_html.queue_file = grab_html.project_name + '/queue.txt'
		grab_html.crawled_file = grab_html.project_name + '/crawled.txt'
		self.boot()
		self.crawl_page('first grab', grab_html.base_url)

	@staticmethod
	def boot():
		create_project_dir(grab_html.project_name)
		create_data_files(grab_html.project_name, grab_html.base_url)
		grab_html.queue = file_to_set(grab_html.queue_file)
		grab_html.crawled =  file_to_set(grab_html.crawled_file)

		






