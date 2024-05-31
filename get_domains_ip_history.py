import argparse
import sys
import re
import os
import json
import funcs as f


# 檢查-o 輸出檔案是否存在
def check_output_file_exist(file):
    if os.path.exists(file):
        # 如果檔案存在，拋出錯誤
        print(f"Error: output file '{file}' already exists.")
        sys.exit(1)





# 檢查輸入的檔案，並添加每個domain 字典到列表中
def check_input_file(file):

    global json_data
    # 定義 domain 的正則表達式
    domain_regex = r'^[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$'

    try:
        with open(file, 'r') as input_file:
            for line in input_file:
                if line.strip():  # 如果這一行不是空行

                    domain = line.rstrip('\n')
                    # 判斷是否符合 domain 正則表達式
                    if re.match(domain_regex, domain):

                        # 創建字典 {'domain':'a.com'}
                        add_new_dict = {}
                        add_new_dict['domain'] = domain

                        # 列表中 添加 字典
                        # {'domains':[     {'domain':'a.com'}          ]}
                        json_data['domains'].append(add_new_dict)
                    else:
                        print(f"Invalid domain: {domain}")
                        sys.exit(1)
                else:
                    # 忽略空行
                    pass
            # check empty file
            if json_data['domains'] == []:
                sys.exit(f"{file} is empty please check out ")               


    except FileNotFoundError:
        print(f"Error: Input file '{file}' does not exist.")
        sys.exit(1)






# 輸出兩種json
def output_json_file(file_name):
    global json_data

    output_file = f'{file_name}'
    output_formatted_file = f'fomatted_{file_name}'

    try:
        # 輸出壓縮json
        with open(output_file, 'w') as file:
            file.write(json.dumps(json_data))

        # 輸出排版json
        with open(output_formatted_file, 'w') as file:
            file.write(json.dumps(json_data, indent=4))

    except IOError as e:
        print(f"Error writing to file: {e}")
        sys.exit(1)













if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process a text file')
    parser.add_argument('-i', '--input', type=str, required=True, help='Input file path')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output file path')

    args = parser.parse_args()

    # 創造json
    json_data = {}

    # 創建 {'domains':[]}
    json_data['domains']=[]


    #檢查輸出檔案
    check_output_file_exist(args.output)
    
    #檢查輸入檔案，並把json_data 中 加入
    # {'domains':[     {'domain':'a.com'}, {'domain':'b.com'}          ]}
    check_input_file(args.input)



    # 讀取列表中的每個元素，每個元素都是一個字典{}
    for domain_item in json_data['domains']:
        # print(domain_item['domain'])
        domain = domain_item['domain']

        # 加入 ip_history 字典
        add_new_dict = {}
        add_new_dict['ip_history'] = {}

        domain_item.update(add_new_dict)

        # domain 發包到 virus total
        result = f.domain_ip_history_sender(domain)

        # 抽取 domain 所有 ip歷史記錄 
        ip_history_dict = f.extract_domain_ip_history(result)

        # 在 ip_history 字典中裝所有 ip
        domain_item['ip_history'].update(ip_history_dict)

        # waiting random time not to fast
        f.wait_random_time()

    print( json.dumps(json_data, indent=4, ensure_ascii=False) )



output_json_file(args.output)





