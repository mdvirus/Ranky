from re import findall
from requests import get


def toph(link):
	if link == "":
		return "0"
	else:
		return findall(r'<div class=value>(.*?)</div>', get(link).text)[1]
