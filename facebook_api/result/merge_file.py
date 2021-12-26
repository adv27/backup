import io
import json

def main():
	data = []
	for i in range(15):
		file_name = 'my_new_list_pages_with_time_'+str(i+1)+ '.txt'
		file_data = str()
		with io.open(file_name,'r',encoding = 'utf-8') as f:
			for line in f:
				file_data += line
		file_data = json.loads(file_data)
		data.extend(file_data)
	file_name = 'my_new_list_pages_with_time_all.txt'
	with io.open(file_name,'w',encoding = 'utf-8') as f:
		f.write(json.dumps(data))

if __name__ == '__main__':
	main()
