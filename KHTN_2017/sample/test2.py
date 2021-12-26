from lxml import etree
import urllib
import io
import json
import itertools

def get_data(file_name):
    data = str()
    with io.open(file_name,'r') as ins:
        for line in ins:
            data += line
    return data

def dataToHTMLTable(my_list, subject_name):
    if len(my_list) == 0:
        return
##            #sort
##            if subject_name != 'All' and subject_name != 'Multi':
##                key_sort = subject_name
##                if subject_name == 'Toán' or subject_name == 'Tin':
##                    key_sort = 'Toán 2'
##                elif subject_name == 'Hóa':
##                    key_sort = 'Hoá'
##                my_list = sorted(my_list, key = lambda k: k[key_sort],reverse = True)
##            elif subject_name == 'All':
##                my_list = list(my_list.get(x) for x in my_list.keys())
##                #my_list = sorted(my_list, key = lambda k: k['Họ Và Tên'][::-1])
##                my_list.sort(key = lambda k: k['Họ Và Tên'][::-1])
##            #
    my_list.sort(key = lambda k: k['Họ Và Tên'].rsplit(None, 1)[-1])
    header = ['Stt']
    header += my_list[0].keys()
    html = '<table align="center" border="2" style="BORDER-COLLAPSE: collapse" bordercolor="#CCCCCC" cellpadding="2" cellspacing="0" width="100%"><tr><th>' + '</th><th>'.join(header) + '</th></tr>'
    for i in range(len(my_list)):
        print(my_list[i]['Họ Và Tên'].rsplit(None, 1)[-1])
        data = my_list[i]
        html += '<tr>'
        html +='<td align="center">' + str(i+1) + '</td>'
        for value in data.values():
            html += '<td align="center">' + str(value) + '</td>'
        html +='</tr>'
    html += '</table>'
    file_name = subject_name+ '_listResult' +'.html'
    with io.open(file_name, "w", encoding="utf-8") as f:
        f.write(html)
    print("Saved " +  file_name)

def main():
    list_all_passed = json.loads(get_data('All_listResult.txt'))
    print('Multi' in list_all_passed)
    list_all_passed.pop('Multi',None)
    print( 'Multi'in list_all_passed)
    #list_all_passed = list(list_all_passed.get(x) for x in list_all_passed.keys())
    my_list = list_all_passed.values()
    my_list = list(itertools.chain.from_iterable(my_list))
    print(len(my_list))
    dataToHTMLTable(my_list,'All')

if __name__ ==  "__main__":
    main()
