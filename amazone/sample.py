import urllib
import io
from urllib import request

def get_list(file_name):
	_list = []
	with io.open(file_name,'r', encoding="utf-8") as f:
		for line in f:
			_list.append(line.replace('\n',''))
	return _list

def save_content_to_file(file_name, content):
	with io.open(file_name,'w', encoding="utf-8") as f:
		f.write(content)

def get_page_content(url):
	if url is not None:
		page = urllib.request.urlopen(url)
		content = page.read().decode('utf-8')
		title = content.split('<title>')[1].split('</title>')[0]
		return content, title

def main():
	file_name = r'C:\Users\vdanh\Desktop\py\amazone\list.txt'
	_list = get_list(file_name)
	for count, url in enumerate(_list, start=1):
		content, title = get_page_content(url)
		file_name = r'C:\Users\vdanh\Desktop\py\amazone'
		file_name += '\\'+ str(count) + '.html'
		save_content_to_file(file_name,content)


if __name__ == '__main__':
	main()
