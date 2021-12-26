import io
import json

def get_file_data(file_name):
        data = str()
        with io.open(file_name, "r") as f:
                for line in f:
                        data += line
        return data

def main():
        data = get_file_data("all_listResult_passed_and_nonpassed.txt")
        data = json.loads(data)
        subject_name = {"Toán": 0, "Lý" : 0, "Hoá": 0 ,"Sinh": 0}
        count = 0
        for i in range(len(data)):
                student = data[i]
                if ("Họ Và Tên" in student and student["Họ Và Tên"] is not ""
                    and student["Họ Và Tên"] == "Nguyễn Thúy Anh"):
                        print(student)
##                if "Kết Luận" in student:
##                        if student["Kết Luận"] is not "":
##                                if "GT" in student:
##                                        if student["GT"] is not "":
##                                                count = count + 1
        print(count)

if __name__ == '__main__':
        main()
