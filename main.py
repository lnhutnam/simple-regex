# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le
# © 2020

# import section
import re
import argparse
from src import constant

'''
Hàm đọc file
Tham số:
    - file_name: Đường dẫn đến file/ tên file cần đọc
'''


def read_file(file_name):
    with open(file_name, 'r', encoding="utf-8") as file:
        string = file.read()
    file.close()
    return string


'''
Hàm ghi file
Tham số:
    - file_name: Đường dẫn đến file/ tên file để ghi
'''


def write_file(file_name, my_list):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(len(my_list)):
            str = "Start= {}, Length= {}, Content={} \n".format(
                my_list[i][0], my_list[i][1], my_list[i][2])
            file.write(str)
    file.close()


'''
Hàm exec
Trích xuất email, địa chỉ website, số điện thoại từ str
Tham số
    - str: chuỗi đầu vào
'''


def exec(str):
    email_regex = re.compile(constant.email_regex_pattern)
    phone_regex = re.compile(constant.phone_regex_pattern)
    website_regex = re.compile(constant.website_regex_pattern)

    email_result = [(m.start(0), len(m.group()), m.group())
                    for m in re.finditer(email_regex, str)]
    phone_result = [(m.start(0), len(m.group()), m.group())
                    for m in re.finditer(phone_regex, str)]
    website_result = [(m.start(0), len(m.group()), m.group())
                      for m in re.finditer(website_regex, str)]

    return email_result + phone_result + website_result


'''
Hàm main
Hàm chính của chương trình
Tham số đầu vào
    args: các argument cần thiết
        - input: đường dẫn/ tên file đầu vào
        - output: đường dẫn/ tên file đầu đầu ra
'''


def main(args):
    input_path = args.input
    output_path = args.output
    data = read_file(input_path)
    write_file(output_path, exec(data))


if __name__ == "__main__":
    '''
    Commandline: python main.py input.txt output.txt
    '''
    parser = argparse.ArgumentParser(
        description="""Regular expression exercise: 
        Viết chương trình bằng ngôn ngữ Python, sử dụng regular expression, để trích xuất danh sách các email, địa chỉ website, số điện thoại từ văn bản."""
    )

    parser.add_argument(
        "input", type=None, help="The input text file's name with .txt extension - file văn bản, định dạng .txt")
    parser.add_argument(
        "output", type=None, help="The output file's name - list các tuple có dạng (vị trí bắt đầu, độ dài, email/website/số điện thoại)")
    args = parser.parse_args()

    main(args)
