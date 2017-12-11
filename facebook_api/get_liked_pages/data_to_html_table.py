#generate html table from data
import io
import json

def get_data_from_file(file_name = None):
    data = str()
    with io.open(file_name,'r') as f:
        for line in f:
            data += line
    return data

def to_html_table(list_pages):
    if(len(list_pages)!=0):
        header = ['Stt']
        header += list_pages[0].keys()
        html = '<table align="center" border="2" style="BORDER-COLLAPSE: collapse" bordercolor="#CCCCCC" cellpadding="2" cellspacing="0" width="100%"><tr><th>' + '</th><th>'.join(header) + '</th></tr>'
        for i in range(0,len(list_pages)):
            data = list_pages[i]
            html += '<tr>'
            html +='<td align="center">' + str(i+1) + '</td>'
            for value in data.values():
                if value == data['name']:
                    html += '<td align="center">' + r'<a href="https://facebook.com/' + data['id'] +'">'+ str(value) +'</a>' + '</td>'
                elif 'category' in data and value == data['category']:
                    html += '<td align="center">' + ', '.join(value) + '</td>'
                else:
                    html += '<td align="center">' + str(value) + '</td>'
            html += '</tr>'
        html += '</table>'
        #file_name = 'out_put' + '.html'
        file_name = 'my_new_list_pages_with_time_category' + '.html'
        with io.open(file_name,'w',encoding="utf-8") as f:
            f.write(html)
        print('Saved ' + file_name)
    else:
        print('empty')
                
def main():
   # list_pages = json.loads(get_data_from_file('list_pages.txt'))
    list_pages = json.loads(get_data_from_file(r'C:\Users\Laptop\Desktop\py\facebook_api\result\my_new_list_pages_with_time_all.txt'))
    to_html_table(list_pages = list_pages)

if __name__ == '__main__':
    main()
