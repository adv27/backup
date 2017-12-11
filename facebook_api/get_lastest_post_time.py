import requests
import json
import io
import _thread
from bs4 import BeautifulSoup

def get_data_from_file(file_name = None):
    data = str()
    with io.open(file_name,'r',encoding = 'utf-8') as f:
        for line in f:
            data += line
    return data

def save_data_to_file(file_name = None, data = None):
    with io.open(file_name,'w',encoding = 'utf-8') as f:
        f.write(data)

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

def get_time_data(liked_pages, user_token, numbers = 1):
    count = 0
    for _list in split_list(liked_pages,numbers):
        count += 1
        _thread.start_new_thread(get_latest_post_data,(_list,user_token,None,count))

#this function return the json result of the request to url:
def my_request(url):
    json_data = requests.get(url).text
    return json.loads(json_data)

def get_latest_post_data(list_pages, user_token, start_id = None,count = 0):
    try:
        request_get_post = r'/posts?limit=1'
        request_get_category = r'/?fields=category_list,category'
        for page in list_pages:
            page_id = page['id']
            if start_id is not None and start_id == page_id:
                start_id = None
            elif start_id is None:
                #geting time of latest post
                url = r'https://graph.facebook.com/' + page_id + request_get_post + '&access_token='+ user_token
                json_obj = my_request(url)
                latest_created_time = ''
                if 'data' in json_obj:
                    if len(json_obj['data']) != 0:
                        data = json_obj['data'][0]
                        latest_created_time = data['created_time']               
                page['latest_post'] = latest_created_time
                #geting category
                url = r'https://graph.facebook.com/' + page_id + request_get_category + '&access_token='+ user_token
                json_obj = my_request(url)
                category = []
                if 'category_list' in json_obj:
                    for item in json_obj['category_list']:
                        category.append(item['name'])
                elif 'category' in json_obj:
                    category.append(json_obj['category'])
                page['category'] = category
        location = r'C:\Users\Laptop\Desktop\py\facebook_api\result\my_new_list_pages_with_time_'+ str(count) + '.txt'
        save_data_to_file(location,data = json.dumps(list_pages))
        print('saved ',location)
    except Exception as ex:
        print(str(ex))
        get_latest_post_data(list_pages,user_token,page_id,count)

def main():
    liked_pages = get_data_from_file(r'C:\Users\Laptop\Desktop\py\facebook_api\get_liked_pages\list_pages.txt')
    liked_pages = json.loads(liked_pages)
    user_token = 'EAACEdEose0cBAF08pvIg88BDaV97cGZAyniCyTXh5kL1B7hX9LOWVzUBC1wW8KTkZBY1M3wV6GKROWFQoI8TbFVEBgiIKGRod6UV2ZBhZBq3qFvZAZAqLnM9nZC45WZAPLb47P55xinNarOVLF3eGQnKDdCzPCJ9nOnQHUA8pxUdE0H771IpDWYZCkCy2C4BNEhIZD'
    get_time_data(liked_pages,user_token,15)


if __name__ == '__main__':
    main()
