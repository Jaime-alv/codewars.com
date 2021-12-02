# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
# For example:
# domain_name("http://github.com/carbonfive/raygun") == "github"
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

types = ['//', 'www.''.com']
test0 = "http://github.com/carbonfive/raygun"
test1 = "http://www.zombie-bites.com"
test2 = "https://www.cnet.com"
test3 = "http://google.co.jp"
test4 = "www.xakep.ru"
test5 = "https://youtube.com"


def domain_name(url):
    import re
    domain_regex = re.compile(r'(http(s)?://)?(www\.)?(.*?)(\.)')
    url_name = domain_regex.search(url)
    return url_name.group(4)

def domain_name_c(url):
    import re
    return re.compile(r'(http(s)?://)?(www\.)?(.*?)(\.)').search(url).group(4)


print(domain_name_c(test5))
