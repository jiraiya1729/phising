import re
from urllib.parse import urlparse, parse_qs
import urllib.request

def num_dots(url):
    """Count the number of dots in the entire URL."""
    return url.count('.')

def subdomain_level(parsed_url):
    """Determine the subdomain level (count of subdomains)."""
    if parsed_url.hostname:
        return len(parsed_url.hostname.split('.')) - 2  # assuming a base domain like example.com
    return 0

def path_level(parsed_url):
    """Count the number of '/' in the path."""
    return parsed_url.path.strip('/').count('/') + 1 if parsed_url.path.strip('/') else 0

def url_length(url):
    """Get the length of the URL."""
    return len(url)

def num_dash(url):
    """Count the number of dashes in the entire URL."""
    return url.count('-')

def num_dash_in_hostname(parsed_url):
    """Count dashes in the hostname."""
    if parsed_url.hostname:
        return parsed_url.hostname.count('-')
    return 0

def at_symbol(url):
    """Determine if '@' symbol is in the URL."""
    return int('@' in url)

def tilde_symbol(url):
    """Determine if '~' symbol is in the URL."""
    return int('~' in url)

def num_underscore(url):
    """Count the number of underscores in the entire URL."""
    return url.count('_')

def num_percent(url):
    """Count the number of percent symbols in the URL."""
    return url.count('%')

def num_query_components(parsed_url):
    """Count the number of query components."""
    return len(parse_qs(parsed_url.query))

def num_ampersand(url):
    """Count the number of ampersands in the URL."""
    return url.count('&')

def num_hash(url):
    """Count the number of hash symbols in the URL."""
    return url.count('#')

def num_numeric_chars(url):
    """Count the number of numeric characters in the URL."""
    return len(re.findall(r'[0-9]', url))

def no_https(url):
    """Check if HTTPS is not in the URL."""
    return int('https://' not in url)

def random_string(url):
    """Check for random string in the URL - simplified example using entropy measure."""
    return len(url) - len(re.sub(r'[a-zA-Z0-9]', '', url))  # Non-alphanumeric as 'random'

def ip_address(parsed_url):
    """Check if the URL contains an IP address."""
    if parsed_url.hostname:
        return int(re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', parsed_url.hostname) is not None)
    return 0

def domain_in_subdomains(parsed_url):
    """Count the number of domains in subdomains."""
    if parsed_url.hostname:
        domains = parsed_url.hostname.split('.')
        base_domain = domains[-2] + '.' + domains[-1]  # Assuming a base domain like example.com
        return sum(1 for domain in domains[:-2] if domain != base_domain)
    return 0

def domain_in_paths(parsed_url):
    """Check if the base domain is in paths."""
    if parsed_url.hostname:
        base_domain = parsed_url.hostname.split('.')[-2] + '.' + parsed_url.hostname.split('.')[-1]
        return int(base_domain in parsed_url.path)
    return 0

def https_in_hostname(parsed_url):
    """Check if 'https' is in the hostname."""
    if parsed_url.hostname:
        return int('https' in parsed_url.hostname)
    return 0

def hostname_length(parsed_url):
    """Get the length of the hostname."""
    if parsed_url.hostname:
        return len(parsed_url.hostname)
    return 0

def path_length(parsed_url):
    """Get the length of the path."""
    return len(parsed_url.path)

def query_length(parsed_url):
    """Get the length of the query string."""
    return len(parsed_url.query)

def double_slash_in_path(parsed_url):
    """Check if there are double slashes in the path."""
    return int('//' in parsed_url.path)

def num_sensitive_words(url):
    """Count the number of sensitive words in the URL."""
    sensitive_words = ["password", "secret", "admin", "login", "bank", "credit"]
    return sum(1 for word in sensitive_words if word in url.lower())

def embedded_brand_name(url):
    """Check if a brand name is embedded in the URL."""
    brand_names = ["google", "facebook", "twitter", "amazon", "apple"]
    return int(any(brand_name in url.lower() for brand_name in brand_names))

def pct_ext_hyperlinks(html_content):
    """Calculate the percentage of external hyperlinks in the HTML content."""
    if not html_content:
        return 0
    # Example implementation: Count all '<a>' tags with 'href' attribute and check if they link to external domains
    num_ext_hyperlinks = sum(1 for match in re.finditer(r'<a\s+href="(https?://[^"/]+)', html_content))
    num_all_hyperlinks = len(re.findall(r'<a\s+href=', html_content))
    return (num_ext_hyperlinks / num_all_hyperlinks) * 100 if num_all_hyperlinks > 0 else 0

def pct_ext_resource_urls(html_content):
    """Calculate the percentage of external resource URLs in the HTML content."""
    if not html_content:
        return 0
    # Example implementation: Count all URLs in <img>, <script>, and <link> tags that link to external domains
    num_ext_urls = sum(1 for match in re.finditer(r'<(img|script|link)\s+.*?src\s*=\s*"(https?://[^"]+)', html_content))
    num_all_urls = len(re.findall(r'<(img|script|link)\s+.*?\s*=\s*"', html_content))
    return (num_ext_urls / num_all_urls) * 100 if num_all_urls > 0 else 0

def ext_favicon(html_content):
    """Check if the HTML content contains an external favicon."""
    return int('<link rel="icon"' in html_content.lower() or '<link rel="shortcut icon"' in html_content.lower())

def insecure_forms(html_content):
    """Check if there are forms without HTTPS in the HTML content."""
    return int('<form action="http://' in html_content.lower())

def relative_form_action(html_content):
    """Check if there are forms with relative action URLs in the HTML content."""
    return int('<form action="/' in html_content.lower())

def ext_form_action(html_content):
    """Check if there are forms with external action URLs in the HTML content."""
    return int('<form action="http' in html_content.lower())

def abnormal_form_action(html_content):
    """Check if there are forms with uncommon action URLs in the HTML content."""
    return int('<form action="' not in html_content.lower() and '<form' in html_content.lower())

def pct_null_self_redirect_hyperlinks(html_content):
    """Calculate the percentage of null self-redirect hyperlinks in the HTML content."""
    if not html_content:
        return 0
    num_null_self_redirects = sum(1 for match in re.finditer(r'<a\s+href="(javascript:void\(0\)|#)"', html_content))
    num_all_hyperlinks = len(re.findall(r'<a\s+href=', html_content))
    return (num_null_self_redirects / num_all_hyperlinks) * 100 if num_all_hyperlinks > 0 else 0

def frequent_domain_name_mismatch(html_content):
    """Check if there are frequent domain name mismatches in the HTML content."""
    return int('href="http' in html_content.lower() and 'href="https' in html_content.lower())

def fake_link_in_status_bar(html_content):
    """Check if there are fake links in the status bar in the HTML content."""
    return int('onmouseover="window.status' in html_content.lower())

def right_click_disabled(html_content):
    """Check if right-click is disabled in the HTML content."""
    return int('oncontextmenu="return false"' in html_content.lower())

def pop_up_window(html_content):
    """Check if there are pop-up windows in the HTML content."""
    return int('window.open' in html_content.lower())

def submit_info_to_email(html_content):
    """Check if there is information submission to email in the HTML content."""
    return int('mailto:' in html_content.lower())

def iframe_or_frame(html_content):
    """Check if there are iframes or frames in the HTML content."""
    return int('<iframe' in html_content.lower() or '<frame' in html_content.lower())

def missing_title(html_content):
    """Check if the HTML content is missing a title."""
    return int('<title>' not in html_content.lower())
def images_only_in_form(html_content):
    """Check if there are images only in forms in the HTML content."""
    return int('<form' in html_content.lower() and '<img' in html_content.lower() and '<a' not in html_content.lower())

def subdomain_level_rt(parsed_url):
    """Calculate the relative subdomain level."""
    if parsed_url.hostname:
        return len(parsed_url.hostname.split('.')) - 2  # Assuming a base domain like example.com
    return 0

def url_length_rt(url):
    """Calculate the relative URL length."""
    return len(url)

def pct_ext_resource_urls_rt(html_content):
    """Calculate the percentage of external resource URLs relative to all URLs."""
    if not html_content:
        return 0
    num_ext_urls = sum(1 for match in re.finditer(r'src="(https?://[^"]+)', html_content))
    num_all_urls = len(re.findall(r'src="', html_content))
    return (num_ext_urls / num_all_urls) * 100 if num_all_urls > 0 else 0

def abnormal_ext_form_action_r(html_content):
    """Check for abnormal external form action URLs relative to all form action URLs."""
    if not html_content:
        return 0
    num_abnormal_ext_form_action = sum(1 for match in re.finditer(r'<form.*?action="https?://[^"]+">', html_content)) - sum(1 for match in re.finditer(r'<form.*?action="/[^"]+">', html_content))
    num_all_ext_form_action = sum(1 for match in re.finditer(r'<form.*?action="https?://[^"]+">', html_content))
    return (num_abnormal_ext_form_action / num_all_ext_form_action) * 100 if num_all_ext_form_action > 0 else 0

def ext_meta_script_link_rt(html_content):
    """Check for external meta, script, or link tags relative to all meta, script, and link tags."""
    if not html_content:
        return 0
    num_ext_meta_script_link = sum(1 for match in re.finditer(r'<(meta|script|link)\s+.*?src\s*=\s*"(https?://[^"]+)', html_content))
    num_all_meta_script_link = len(re.findall(r'<(meta|script|link)\s+.*?\s*=\s*"', html_content))
    return (num_ext_meta_script_link / num_all_meta_script_link) * 100 if num_all_meta_script_link > 0 else 0

def pct_ext_null_self_redirect_hyperlinks_rt(html_content):
    """Calculate the percentage of external null self-redirect hyperlinks relative to all hyperlinks."""
    if not html_content:
        return 0
    num_ext_null_self_redirects = sum(1 for match in re.finditer(r'<a\s+href="(javascript:void\(0\)|#)"', html_content))
    num_all_hyperlinks = len(re.findall(r'<a\s+href=', html_content))
    return (num_ext_null_self_redirects / num_all_hyperlinks) * 100 if num_all_hyperlinks > 0 else 0

def extract_features(url):
    parsed_url = urlparse(url)
    # with urllib.request.urlopen(url) as response:
    #     html_content = response.read().decode('utf-8')
    html_content = """
    <html>
    <head>
        <title>Sample Page</title>
    </head>
    <body>
       <h2> this is phising site give money<h2/>
    </body>
    </html>
    """

    return [
        num_dots(url),
        subdomain_level(parsed_url),
        path_level(parsed_url),
        url_length(url),
        num_dash(url),
        num_dash_in_hostname(parsed_url),
        at_symbol(url),
        tilde_symbol(url),
        num_underscore(url),
        num_percent(url),
        num_query_components(parsed_url),
        num_ampersand(url),
        num_hash(url),
        num_numeric_chars(url),
        no_https(url),
        random_string(url),
        ip_address(parsed_url),
        domain_in_subdomains(parsed_url),
        domain_in_paths(parsed_url),
        https_in_hostname(parsed_url),
        hostname_length(parsed_url),
        path_length(parsed_url),
        query_length(parsed_url),
        double_slash_in_path(parsed_url),
        num_sensitive_words(url),
        embedded_brand_name(url),
        pct_ext_hyperlinks(html_content),
        pct_ext_resource_urls(html_content),
        ext_favicon(html_content),
        insecure_forms(html_content),
        relative_form_action(html_content),
        ext_form_action(html_content),
        abnormal_form_action(html_content),
        pct_null_self_redirect_hyperlinks(html_content),
        frequent_domain_name_mismatch(html_content),
        fake_link_in_status_bar(html_content),
        right_click_disabled(html_content),
        pop_up_window(html_content),
        submit_info_to_email(html_content),
        iframe_or_frame(html_content),
        missing_title(html_content),
        images_only_in_form(html_content),
        subdomain_level_rt(parsed_url),
        url_length_rt(url),
        pct_ext_resource_urls_rt(html_content),
        abnormal_ext_form_action_r(html_content),
        ext_meta_script_link_rt(html_content),
        pct_ext_null_self_redirect_hyperlinks_rt(html_content),
    ]
