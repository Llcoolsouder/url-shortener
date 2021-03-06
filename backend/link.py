import hashlib
from json import JSONEncoder
from functools import partialmethod


class Link():
    def __init__(self, url, source_tag):
        self.url = Link._clean_url(url)
        self.source_tag = source_tag

    @classmethod
    def from_url(cls, url) -> 'Link':
        ''' Creates a Link object from a url'''
        source_tag = hashlib.md5(url.encode('utf-8')).hexdigest()[0:8]
        return cls(url, source_tag)

    def get_absolute_url(self) -> 'str':
        '''Returns an absolute url'''
        return f'http://{self.url}'

    @staticmethod
    def _clean_url(url) -> 'str':
        '''
        Parameters:
            url (str): any properly formed, url
        Returns:
            a clean url for entry into a database
        '''
        cleaned_url = url
        if url.startswith('http'):
            cleaned_url = ''.join(url.split('//')[1:])
        return cleaned_url


class LinkEncoder(JSONEncoder):
    def default(self, obj, api_prefix=''):
        if isinstance(obj, Link):
            return {
                'url': obj.url,
                'source_tag': f'{api_prefix}{obj.source_tag}',
            }
        else:
            return super().default(obj)

    @classmethod
    def make_link_encoder(cls, api_prefix):
        ''' 
        Returns:
            a new class that derives JSONEncoder and overrides the `default` 
            method to use that of LinkEncoder with a prefixed string in front
            of source_tag
        '''
        return type(
            f'LinkEncoder_{api_prefix}',
            (JSONEncoder, ),
            dict(default=partialmethod(cls.default, api_prefix=api_prefix)))
