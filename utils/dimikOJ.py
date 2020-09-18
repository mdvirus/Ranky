from re import findall
from requests import get


def dimik(link):
	if link == "":
		return "0"
	else:
		return findall(r'<p class="h4">(.*?) <small>টি সঠিক সমাধান</small></p>', get(link).text)[0]
