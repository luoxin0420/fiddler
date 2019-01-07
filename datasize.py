#!/usr/bin/evn python
# -*- coding:utf-8 -*-


from pyExcelerator import*
from performance import Write_file


def get_data_size():
    with open('C:/Users/Administrator/Desktop', 'r') as f:
        protocol_dict = eval(f.read())      # 抓取的协议包转换为字典
        get_request_times = len(protocol_dict['log']['entries'])
        request_data = []
        response_data = []
        total_data = []
        get_url_list = []
        request_dict = {}
        response_dict = {}
        total_dict = {}
        for n in range(get_request_times):
            get_url = protocol_dict['log']['entries'][n]['request']['url']
            get_url_list.append(get_url)
        get_url_removal = list(set(get_url_list))
        get_url_removal.sort(key=get_url_list.index)
        for url in get_url_removal:
            for n in range(get_request_times):
                if protocol_dict['log']['entries'][n]['request']['url'] == url:
                    request_header = protocol_dict['log']['entries'][n]['request']['headersSize']     # 请求头大小
                    request_body = protocol_dict['log']['entries'][n]['request']['bodySize']          # 请求body大小
                    request_data.append(request_header)
                    request_data.append(request_body)
                    response_header = protocol_dict['log']['entries'][n]['response']['headersSize']     # 返回头大小
                    response_body = protocol_dict['log']['entries'][n]['response']['bodySize']  # 返回body大小
                    response_data.append(response_header)
                    response_data.append(response_body)
            request_size = sum(request_data)  # 请求大小
            request_dict[url] = request_size
            print('request',request_dict)
            response_size = sum(response_data)  # 返回大小
            response_dict[url] = response_size
            print('response',response_dict)
            total_size = request_size + response_size  # 总大小
            total_dict[url] = total_size
            print('total',total_dict)
            total_data.append(request_size)
            total_data.append(response_size)
            total_data.append(total_size)
        protocol_tup = (request_dict, response_dict, total_dict, total_data)
        return protocol_tup

def get_excel(protocol_tup):
    # 得到数据写入到表格
    write_file = Write_file()
    w = Workbook()  # 创建一个工作薄
    url_size = w.add_sheet('url_size')  # 创建url工作表
    total_size = w.add_sheet('total_size')    # 创建总值表
    fname = write_file.get_file_name('C:/Users/Administrator/Desktop/data_size', '.xls')
    url_size.write(0, 1, 'request_size(kb)')
    url_size.write(0, 2, 'response_size(kb)')
    url_size.write(0, 3, 'total_size(kb)')
    total_size.write(0, 0, 'request_size(kb)')
    total_size.write(1, 0, 'response_size(kb)')
    total_size.write(2, 0, 'total_size(kb)')
    for i in range(3):
        times = 0
        key_list = []
        # url_size.write(0, i+1, protocol_tup[i]+'(kb)')
        # total_size.write(i, 0, protocol_tup[i]+'(kb)')
        for key in protocol_tup[i]:
            if key not in key_list:
                times += 1
            url_size.write(times, 0, key)
            url_size.write(times,i+1, protocol_tup[i][key])

    total_size.write(0, 1, protocol_tup[3][0])
    total_size.write(1, 1, protocol_tup[3][1])
    total_size.write(2, 1, protocol_tup[3][2])
    w.save(fname)




if __name__ == '__main__':
    get_data = get_data_size()
    get_excel(get_data)






