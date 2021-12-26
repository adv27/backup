from lxml import etree
import urllib
import io
import json

from urllib import request
from operator import itemgetter

def getListID(file_name):
    data = str()
    with io.open(file_name,'r') as ins:
        for line in ins:
            data += line
    return data.split(',')

def dataToHTMLTable(my_list, subjectName):
    try:
        if (len(my_list)!=0):
            #sort
            if subject_name != 'All':
                key_sort = subject_name
                if key_sort in ['Toán', 'Tin']:
                    key_sort = 'Toán 2'
                elif key_sort == 'Hóa':
                    key_sort = 'Hoá'
                my_list = sorted(my_list, key = lambda k: k[key_sort],reverse = True)
            #
            header = ['Stt']
            header += my_list[0].keys()
            html = '<table align="center" border="2" style="BORDER-COLLAPSE: collapse" bordercolor="#CCCCCC" cellpadding="2" cellspacing="0" width="100%"><tr><th>' + '</th><th>'.join(header) + '</th></tr>'
            for i in range(len(my_list)):
                data = my_list[i]
                html += '<tr>'
                html +='<td align="center">' + str(i+1) + '</td>'
                for value in data.values():
                    html += '<td align="center">' + str(value) + '</td>'
                html +='</tr>'
            html += '</table>'
            file_name = subjectName+ '_listResult' +'.html'
            with io.open(file_name, "w", encoding="utf-8") as f:
                f.write(html)
            print("Saved " +  file_name)
    except Exception:
        print(my_list)

def getData(_list,list_id,_from,_to):
    try:
       for i in range(_from,_to):
            stu_id = list_id[i]
            url = "http://hus.vnu.edu.vn/thpt2017/?q=" + stu_id + "&Submit=Xem+%C4%90i%E1%BB%83m"
            page = urllib.request.urlopen(url,timeout=20)
            content = page.read()
            table = etree.HTML(content).find('body/table')
            if table is not None:
                rows = iter(table)
                headers = [col.text for col in next(rows)]
                for row in rows:
                    values = [col.text for col in row]
                    data = dict(zip(headers, values));
                    if(data.get('Kết Luận')is not None):
                        data.pop(None,None)
##                        key = str(data.get('Kết Luận')).replace('Đỗ C. ','')
##                        _list[key].append(data)
##                        index = _list[key].index(data)
##                        student = (_list[key])[index]
##                        student['SBD'] = id
                        _list.append(data);
                        index = _list.index(data)
                        student = _list[index]
                        student['SBD'] = stu_id
    except Exception:
        print(i)
        getData(_list,list_id,i,_to)
        

def main():
    list_subjects = ['Toán','Tin', 'Lý', 'Hoá', 'Sinh']
##    list_all_passed = dict()
##    list_all_passed = {'Toán':list(),'Tin':list(), 'Lý':list(), 'Hóa':list(), 'Sinh':list()}
    list_all_passed = []
    list_id = getListID('listId.txt')
    print(list_id[320])
    print("Loaded, size = " +str(len(list_id)))
    getData(list_all_passed,list_id,100,len(list_id))
    print("Get data done")
    with io.open("All_listResult.txt", "w", encoding="utf-8") as f:
                f.write(json.dumps(list_all_passed))
    print("Saved ")
##    for _key in list_all_passed.keys():
##        dataToHTMLTable(list_all_passed[_key],_key)

if __name__ ==  "__main__":
    main()
