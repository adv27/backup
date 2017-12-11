#getting all student passed
from bs4 import BeautifulSoup
from urllib import request
import io
import urllib
import json

def getListID(file_name):
    data = str()
    with io.open(file_name,'r') as ins:
        for line in ins:
            data += line
    list_id = data.replace(' ','').split(',')
    return list_id

def getData(list_stu, list_ids, from_,to_):
    try:
        for i in range(from_,to_):
            stu_id = list_ids[i];
            url = "http://hus.vnu.edu.vn/thpt2017/?q=" + stu_id + "&Submit=Xem+%C4%90i%E1%BB%83m"
            print(str(i) + " " +url)
            page = urllib.request.urlopen(url,timeout=20)
            content = page.read()
            soup = BeautifulSoup(content,"lxml")
            table = soup.find("table", attrs = {"align": "center"})
            if table is not None:
                rows = iter(table)
                headers = [th.get_text() for th in table.find("tr").find_all("td")]
                values = [th.get_text() for th in (table.find_all("tr"))[1].find_all("td")]
                data = dict(zip(headers, values));
                list_stu.append(data)
                #print(data)
##                if(data.get('Kết Luận')is not ''):
##                    list_key = (str(data.get('Kết Luận')).replace('Đỗ','')).replace('C. ','').split(',')
##                    if(len(list_key)>1):
##                        list_stu['Multi'].append(data)
##                    for key in list_key:
##                        list_stu[key.replace(' ','')].append(data)
    except Exception as ex:
        print(str(ex))
        print(i)
        getData(list_stu,list_ids,i,to_)

def main():
    #list_all_passed = {'Toán':list(),'Tin':list(), 'Lý':list(), 'Hóa':list(), 'Sinh':list(), 'Multi':list()}
    list_all = list()
    ids = getListID("listId.txt")
    #getting data from server
    getData(list_all,ids,0,len(ids))
    #save data to file
    with io.open("all_listResult_passed_and_nonpassed.txt", "w", encoding="utf-8") as f:
        f.write(json.dumps(list_all))

if __name__ == "__main__":
    main()
