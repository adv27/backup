#generate HTML table from data
from lxml import etree
import urllib
import io
import json
import itertools
from urllib import request
from operator import itemgetter

def get_file_data(file_name):
    data = str()
    with io.open(file_name,'r') as f:
        for line in f:
            data += line
    return data

def data_to_HTML_table(my_list, subject_name):
    try:
        if(len(my_list)!=0):
            #sort
            if subject_name != 'All' and subject_name != 'Multi':
                key_sort = subject_name
                if subject_name == 'Toán' or subject_name == 'Tin':
                    key_sort = 'Toán 2'
                elif subject_name == 'Hóa':
                    key_sort = 'Hoá'
                my_list = sorted(my_list, key = lambda k: float(k[key_sort]),reverse = True)
            else:
                if subject_name == 'All':
                    #my_list.pop('Multi',None)
                    #my_list = my_list.values()
                    my_list = list(itertools.chain.from_iterable(my_list))
                my_list.sort(key = lambda k: k['Họ Và Tên'].rsplit(None, 1)[-1])
            #
            header = ['Stt']
            header += my_list[0].keys()
            html = '<table align="center" border="2" style="BORDER-COLLAPSE: collapse" bordercolor="#CCCCCC" cellpadding="2" cellspacing="0" width="100%"><tr><th>' + '</th><th>'.join(header) + '</th></tr>'
            for i in range(0,len(my_list)):
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
    except Exception as e:
        print(str(e))


def main():
    list_all_passed = json.loads(get_file_data("all_listResult_passed_and_nonpassed.txt"))
    list_all_passed = sorted(list_all_passed,key = lambda k: k['Họ Và Tên'].rsplit(None, 1)[-1])
##    for key in list_all_passed.keys():
##        list_ = list_all_passed[key]
##        data_to_HTML_table(list_,key)
  #  data_to_HTML_table(list_all_passed,'All')
    header = ['Stt']
    header += list_all_passed[0].keys()
    html = '<table align="center" border="2" style="BORDER-COLLAPSE: collapse" bordercolor="#CCCCCC" cellpadding="2" cellspacing="0" width="100%"><tr><th>' + '</th><th>'.join(header) + '</th></tr>'
    for i in range(0,len(list_all_passed)):
        data = list_all_passed[i]
        html += '<tr>'
        html +='<td align="center">' + str(i+1) + '</td>'
        for value in data.values():
            html += '<td align="center">' + str(value) + '</td>'
        html +='</tr>'
    html += '</table>'
    file_name = "all"+ '_listResult' +'.html'
    with io.open(file_name, "w", encoding="utf-8") as f:
        f.write(html)
    print("Saved " +  file_name)
        

if __name__ == "__main__":
    main()
