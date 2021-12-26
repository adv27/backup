from lxml import etree
import urllib
import io
from urllib import request
def dataToHTMLTable(my_list):
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
    with io.open('listResult.html', "w", encoding="utf-8") as f:
        f.write(html)

def getData(_list,_from, _to):
    try:
        for i in range(_from,_to):
            id = str(i).zfill(5)
            url = "http://hus.vnu.edu.vn/thpt2017/?q=" + id + "&Submit=Xem+%C4%90i%E1%BB%83m"
            page = urllib.request.urlopen(url,timeout=20)
            content = page.read()
            table = etree.HTML(content).find('body/table')
            if table is not None:
                rows = iter(table)
                headers = [col.text for col in next(rows)]
                for row in rows:
                    values = [col.text for col in row]
                    data = dict(zip(headers, values));
                    if(data.get('Kết Luận')== 'Đỗ C. Hóa'):
                        data.pop(None,None)
                        _list.append(data)
    except Exception:
        getData(_list,i-1,_to)
        

def main():
    my_list= []
    getData(my_list,0,3000)
    my_list = sorted(my_list,key = lambda k: k['Hoá'])
    dataToHTMLTable(my_list)
    

if __name__ ==  "__main__":
    main()
