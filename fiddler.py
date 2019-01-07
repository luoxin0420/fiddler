__author__ = 'Administrator'
#-*- coding: UTF-8 -*-
import json
from xlwt import *
from xlrd import *
import datetime
import csv

format_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
json_file = 'E:/fiddler/TCL.har'
text_file = 'E:/fiddler/TCL.txt'
xlsx_file = 'E:/fiddler/data.xls'
csv_file = 'E:/fiddler/data.csv'


def get_number():
    with open(json_file, 'r') as f:
        json_data = ''.join(f.readlines()).decode("utf-8-sig").encode("utf-8")
        harDirct = json.loads(json_data)
        json_str = json .dumps(harDirct, sort_keys=True, indent=4, separators=(',', ':'))
        with open(text_file, 'w') as n:
            n.write(json_str + '\n')
        all_list1 = harDirct['log']['entries']
        request_list = []
        response_list = []
        total_list = []
        url_list = []
        for item in all_list1:
            request_bodySize = (item['request']['bodySize'])
            request_headerSize = (item['request']['headersSize'])
            request = request_bodySize + request_headerSize
            response_bodySize = (item["response"]['bodySize'])
            response_headerSize = (item["response"]['headersSize'])
            response = response_bodySize + response_headerSize
            url = (item['request']['url'])
            total = request + response
            url_list.append(url)
            request_list.append(request)
            response_list.append(response)
            total_list.append(total)
            # print(request, response, total)
        sum_request = 0
        for i in request_list:
            sum_request = sum_request + i
        # print(sum_request)
        sum_response = 0
        for i in response_list:
            sum_response = sum_response + i
        # print(sum_response)
        sum_total = 0
        for i in total_list:
            sum_total = sum_total + i
        # print(sum_total)
        return (request_list, response_list, total_list, sum_request, sum_response, sum_total, url_list)


def make_form(number):
    data_request = number[0]
    data_response = number[1]
    data_total = number[2]
    data_url = number[6]
    file = Workbook(encoding='utf-8')
    table = file.add_sheet('data', cell_overwrite_ok=True)
    table.write(0, 1, label="URL")
    table.write(0, 2, label="Request")
    table.write(0, 3, label="Response")
    table.write(0, 4, label="Total")
    table.write(len(data_total) + 1, 0, label="SUM")
    data_sum_request = number[3]
    data_sum_response = number[4]
    data_sum_total = number[5]
    i = 1
    j = 1
    for data1 in data_url:
            table.write(i, j, data1)
            i += 1
    for i in range(1, len(data_total)+1):
        j = 2
        table.write(i, j, data_request[i-1])
        j += 1
        table.write(i, j, data_response[i-1])
        j += 1
        table.write(i, j, data_total[i-1])

    table.write(len(data_total) + 1, 2, data_sum_request)
    table.write(len(data_total) + 1, 3, data_sum_response)
    table.write(len(data_total) + 1, 4, data_sum_total)
    file.save(xlsx_file)
    return (xlsx_file)
print(xlsx_file)


def same_url(xlsx_file, number):
    # xlsx_file = xlsx_file
    # xls_file = open_workbook(xlsx_file)
    # sheet = xls_file.sheet_by_index(0)
    # print(sheet.name, sheet.nrows, sheet.ncols)

    value1 = number[0]
    value2 = number[1]
    value3 = number[2]
    dict_key = number[6]
    mid = map(list, zip(dict_key, value1, value2, value3))
    # print(mid)
    new_dict = {}
    for i in mid:
        k = i[0]
        if k not in new_dict.keys():
            new_dict[k] = i[1:4]
        else:
            new_dict[k][0] += int(i[1])
            new_dict[k][1] += int(i[2])
            new_dict[k][2] += int(i[3])
    # print(new_dict)
    with open(csv_file, 'wb') as f:
        fieldnames = ['URL', 'Request', 'Response', 'Total']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        write = csv.writer(f)
        for k, v in new_dict.items():
            write.writerow([k] + v)


if __name__ == '__main__':
    number = get_number()
    # make_form(number)
    same_url(xlsx_file, number)

