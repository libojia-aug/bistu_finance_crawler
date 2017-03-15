# encoding: utf-8

from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):

    def _get_new_urls(self, soup):
        new_full_urls = set()
        blog_nodes = soup.find_all('a', href=re.compile(r'/blog.sina.com.cn/s/blog_\S+\.htm\S+'))
        stock_nodes = soup.find_all('a', href=re.compile(r'finance.sina.com.cn/stock/\S+\.shtml'))
        roll_nodes = soup.find_all('a', href=re.compile(r'finance.sina.com.cn/roll/\S+\.shtml'))
        for a_node in blog_nodes:
            new_url = a_node['href']
            # new_full_url = urlparse.urljoin(url, new_url)
            new_full_urls.add(new_url)
        for a_node in stock_nodes:
            new_url = a_node['href']
            # new_full_url = urlparse.urljoin(url, new_url)
            new_full_urls.add(new_url)
        for a_node in roll_nodes:
            new_url = a_node['href']
            # new_full_url = urlparse.urljoin(url, new_url)
            new_full_urls.add(new_url)
        return new_full_urls

    # def _get_new_data(self, url, soup):
    def _get_new_data(self, url, soup):
        new_data = {}
        if(re.search(r'/blog.sina.com.cn/s/blog_\S+\.htm\S+', url)):
        # if(re.search(r'finance.sina.com.cn/stock/\S+\.shtml', url)):
            # print soup.find('h1')
            if(soup.find('h1') == None): 
               new_data['url'] = url
               new_data['title'] = 'redirection'
               new_data['summary'] = 'redirection'
            else:
                #url
                new_data['url'] = url
                #title
                title_node = soup.find('h1')
                title = title_node.get_text()
                new_data['title'] = title
                #summary
                summary_node = soup.find('div', class_='articalContent')
                summary = summary_node.get_text()
                summary = re.sub(r'\s+', '\n', summary)
                new_data['summary'] = summary
        elif(re.search(r'finance.sina.com.cn/stock/\S+\.shtml', url)):
            if(re.search(r'/usstock/', url)):
               new_data['url'] = url
               new_data['title'] = 'not text'
               new_data['summary'] = 'not text'
            elif(soup.find('h1') == None): 
               new_data['url'] = url
               new_data['title'] = 'redirection'
               new_data['summary'] = 'redirection'  
            else:
                #url
                new_data['url'] = url
                #title
                title_node = soup.find('h1')
                title = title_node.get_text()
                new_data['title'] = title
                #summary
                summary_node = soup.find('div', id='artibody')
                summary = summary_node.get_text()
                summary = re.sub(r'\s+', '\n', summary)
                new_data['summary'] = summary
        elif(re.search(r'finance.sina.com.cn/roll/\S+\.shtml', url)):
            if(re.search(r'/usstock/', url)):
               new_data['url'] = url
               new_data['title'] = 'not text'
               new_data['summary'] = 'not text'
            elif(soup.find('h1') == None): 
               new_data['url'] = url
               new_data['title'] = 'redirection'
               new_data['summary'] = 'redirection'  
            else:
                #url
                new_data['url'] = url
                #title
                title_node = soup.find('h1')
                title = title_node.get_text()
                new_data['title'] = title
                #summary
                summary_node = soup.find('div', id='artibody')
                summary = summary_node.get_text()
                summary = re.sub(r'\s+', '\n', summary)
                new_data['summary'] = summary
        return new_data

    def parseRoot(self, content):
        # if url is None or content is None:
        if content is None:
            return
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(soup)
        # new_data = self._get_new_data(url, soup)
        # return new_urls, new_data
        return new_urls

    def parseLeaves(self, url, content):
        if url is None or content is None:
            return
        soup = BeautifulSoup(content, 'lxml', from_encoding='utf-8')
        # new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        # return new_urls, new_data
        return new_data