from gglsbl import SafeBrowsingList
from config import GoogleConfig
from flask import request
from urllib.parse import urlparse, urljoin


class Security:
    def __init__(self):
        self.sbl = SafeBrowsingList(GoogleConfig.SAFEBROWSINGAPIKEY)
        self.sbl.update_hash_prefix_cache()
        pass

    def validate_referer(self, url):
        threat_list = self.sbl.lookup_url(url)
        if threat_list is None:
            return None
        return threat_list

    def get_referer(self):
        referer = request.referrer
        if not referer:
            return None
        return referer

    @staticmethod
    def is_safe_url(url):
        ref_url = urlparse(request.host_url)
        test_url = urlparse(urljoin(request.host_url, url))
        return test_url.scheme in ('http', 'https') and \
               ref_url.netloc == test_url.netloc


norman_security = Security()