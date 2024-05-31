import json
import funcs as f
import argparse
import sys
import os

# 檢查-o 輸出檔案是否存在
def check_output_file_exist(file):
    if os.path.exists(file):
        # 如果檔案存在，拋出錯誤
        print(f"Error: output file '{file}' already exists.")
        sys.exit(1)









# 判斷輸入的檔案是否是合法json檔，並檢查是否存在
def check_input_file(file):

    try:
        with open(file, 'r') as input_file:
           
            try:
                json_data = json.load(input_file)
                print(f"Input file '{file}' is a valid JSON file.")
                
                return json_data

            except json.JSONDecodeError:
                print(f"Error: Input file '{file}' is not a valid JSON file.")
                sys.exit(1)

    except FileNotFoundError:
        print(f"Error: Input file '{file}' does not exist.")
        sys.exit(1)





# 輸出兩種json
def output_json_file(file_name):
    global domains_ip_history_json

    output_file = f'{file_name}'
    output_formatted_file = f'formatted_{file_name}'

    try:
        # 輸出壓縮json
        with open(output_file, 'w') as file:
            file.write(json.dumps(domains_ip_history_json))

        # 輸出排版json
        with open(output_formatted_file, 'w') as file:
            file.write(json.dumps(domains_ip_history_json, indent=4))

    except IOError as e:
        print(f"Error writing to file: {e}")
        sys.exit(1)














if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process a text file')
    parser.add_argument('-i', '--input', type=str, required=True, help='Input file path')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output file path')

    args = parser.parse_args()

    #檢查輸出檔案     
    check_output_file_exist(args.output)

    #檢查輸入檔案，載入json
    domains_ip_history_json =  check_input_file(args.input)






    # 讀取列表中的每個元素，每個元素都是一個字典{}
    for domain_item in domains_ip_history_json['domains']:

        domain = domain_item['domain']
        ip_history = domain_item['ip_history']



        for ip, ip_data in ip_history.items():

            # 送 ip 到 virus total 反解
            result = f.ip_reverse_sender(ip)

            # 抽取所有 反解 的domain + 日期 裝到字典
            reverse_data_dict = f.extract_reverse_domains(result)
            
            # 創建 ip_reverse_data 字典
            add_new_dict = {}
            add_new_dict['ip_reverse_data'] = {}

            # 每個ip底下 加入 ip_reverse_data 字典
            domain_item['ip_history'][ip].update(add_new_dict)

            # 每個ip底下 加入 ip_reverse_data 字典裡面 加入 所有 反解 的domain + 日期
            domain_item['ip_history'][ip]['ip_reverse_data'].update(reverse_data_dict)



            # waiting random time not to fast
            f.wait_random_time()
                
    print(domains_ip_history_json)

    output_json_file(args.output) 






























