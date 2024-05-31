import json
import argparse
import sys
import os




# 判斷檔案輸出檔案是否存在
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
                print(f"Input file '{file}' is a valid JSON file.\n")
                
                return json_data

            except json.JSONDecodeError:
                print(f"Error: Input file '{file}' is not a valid JSON file.")
                sys.exit(1)

    except FileNotFoundError:
        print(f"Error: Input file '{file}' does not exist.")
        sys.exit(1)



# 輸出 所有域名的 歷史ip + 解析時間  
def simple_output_history_ip_date():
    for domain_item in json_data['domains']:

        domain = domain_item['domain']
        ip_history = domain_item['ip_history']
        
        print(domain)

        for ip, ip_data in ip_history.items():
            print(ip.ljust(15),'-', ip_data['resolve_date'])

        print('\n')




# 輸出某個ip反解的 所有域名 
def output_ip_reverse_simple(input_ip):
    for domain_item in json_data['domains']:

        domain = domain_item['domain']
        ip_history = domain_item['ip_history']
        

        for ip, ip_data in ip_history.items():


            ip_reverse_data = ip_data['ip_reverse_data']

            if ip == input_ip:


                print('domain:', domain)
                print('ip history:', ip)
                print('resolve_date', ip_data['resolve_date'])
                print('\n') 

                for reverse_domain in ip_reverse_data.keys():
                        print(reverse_domain)
                print('\n')



# 輸出某個ip反解的 所有域名 + 時間
def output_ip_reverse_detail(input_ip):
    for domain_item in json_data['domains']:

        domain = domain_item['domain']
        ip_history = domain_item['ip_history']
        

        for ip, ip_data in ip_history.items():


            ip_reverse_data = ip_data['ip_reverse_data']

            if ip == input_ip:

                #判斷某ip reverse_data資料中最長域名，用於排版
                max_domain_length = max(len(reverse_domain) for reverse_domain in ip_reverse_data.keys())

                print('domain:', domain)
                print('ip history:', ip)
                print('resolve_date', ip_data['resolve_date'])
                print('\n') 
                print('ip reverse result')

                for reverse_domain, date in ip_reverse_data.items():
                   #排版
                   print(reverse_domain.ljust(max_domain_length), '-', date)

                print('\n')






if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process a text file')
    parser.add_argument('-i', '--input', type=str, required=True, help='Input file path')
    parser.add_argument('-ip', '--ip', type=str, required=False, help='Input file path')
    parser.add_argument('-date', '--date', action='store_true', help='Enable date parameter')

    args = parser.parse_args()
    
    if args.input is not None:
        json_data =  check_input_file(args.input)
    
    

    if args.ip is not None:
        input_ip = args.ip

        if args.date :
            output_ip_reverse_detail(input_ip)
        else:
            output_ip_reverse_simple(input_ip)

    else:
        simple_output_history_ip_date()