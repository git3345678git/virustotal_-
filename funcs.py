import random
import time
import datetime
import requests
import execjs
from lxpy import copy_headers_dict
import pytz


# virus taotal 的js 會發出特殊值，我們逆向找到關鍵JS並取值
def get_xvt_anti_value():

    js = '''
    function get_anti(){
        const e = Date.now() / 1e3;
        return btoa(`${(()=>{
            const e = 1e10 * (1 + Math.random() % 5e4);
            return e < 50 ? "-1" : e.toFixed(0)
        }
        )()}-ZG9udCBiZSBldmls-${e}`)
    }
    '''

    xvt_anti = execjs.compile(js).call('get_anti')
    
    return xvt_anti







# 預設兩種模式，ip_history 和 ip_reverse 有不同的頭部
def header_generator(**kwargs):

    headers = copy_headers_dict('''
        authority: www.virustotal.com
        method: GET
        scheme: https
        accept: application/json
        accept-encoding: gzip, deflate, br
        accept-ianguage: en-US,en;q=0.9,es;q=0.8
        accept-language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
        cache-control: no-cache
        content-type: application/json
        cookie: __gsas=ID=7fbf1d55c470b3c5:T=1711350030:RT=1711350030:S=ALNI_MYjyadj3LNZkRctPBuuZZixC_aRkg; _ga_E8LNX6HSCN=GS1.2.1713341135.2.0.1713341135.60.0.0; _gid=GA1.2.2134845754.1715321476; new-privacy-policy-accepted=1; _ga=GA1.2.454274907.1711350028; _gat=1; _ga_BLNDV9X2JR=GS1.1.1715415293.47.1.1715416503.0.0.0
        pragma: no-cache
        referer: https://www.virustotal.com/
        sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"
        sec-ch-ua-mobile: ?0
        sec-ch-ua-platform: "Windows"
        sec-fetch-dest: empty
        sec-fetch-mode: cors
        sec-fetch-site: same-origin
        user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
        x-app-version: v1x262x2
        x-tool: vt-ui-main
    ''')


    # 頭部添加 Virustotal 的 特殊值
    xvt_anti = get_xvt_anti_value()
    headers.update({'X-Vt-Anti-Abuse-Header':xvt_anti})
    
    
    custom_header_path = '' 


    if kwargs["option"] == "ip_history":
        custom_header_path = f'/ui/domains/{kwargs["domain"]}/resolutions'
        headers.update({'path':custom_header_path})

    elif kwargs["option"] == "ip_reverse":
        custom_header_path = f'/ui/ip_addresses/{kwargs["ip"]}/resolutions'
        headers.update({'path':custom_header_path})

    else:
        return 'please set header option'

    return headers






# domain_ip_history 的封包
def domain_ip_history_sender(domain, limit=30):
    url = f"https://www.virustotal.com/ui/domains/{domain}/resolutions?limit={limit}"

    # header options setting
    # ip_history or ip_reverse
    headers = header_generator(option = "ip_history", domain = domain)

    # send request
    response = requests.get(url=url,  headers=headers)
    result = response.json()
    return result["data"]  

# ip_reverse 的封包
def ip_reverse_sender(ip, limit=30):

    url = f"https://www.virustotal.com/ui/ip_addresses/{ip}/resolutions?limit={limit}"

    # header options setting
    # ip_history or ip_reverse
    headers = header_generator(option = "ip_reverse", ip = ip)

    # send request
    response = requests.get(url=url,  headers=headers)
    result = response.json()
    return result["data"]  


#  抽取 歷史ip + date 到字典
def extract_domain_ip_history(items):

    ip_history_data = {}   
    
    # each ip get all domains 
    for item in items:

        # get hostname 
        ip = item["attributes"]["ip_address"]

        # get time
        datetime_object = datetime.datetime.fromtimestamp(item["attributes"]["date"], tz=pytz.timezone('Etc/GMT+0'))
        formatted_time = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
        
        # load to dict
        # {'8.8.8.8':{}}
        ip_history_data[ip] = {}
           
        # {'8.8.8.8':{    'resolve_date': '2024-05-15'       }
        ip_history_data[ip]['resolve_date']=formatted_time
    
    return ip_history_data


#  抽取 ip reverse + date 到字典
def extract_reverse_domains(items):

    reverse_data = {}   
    
    # each ip get all domains 
    for item in items:

        # get hostname 
        host_name = item["attributes"]["host_name"]

        # get time
        datetime_object = datetime.datetime.fromtimestamp(item["attributes"]["date"], tz=pytz.timezone('Etc/GMT+0'))
        formatted_time = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
        
        # load to dict
        reverse_data[host_name] = formatted_time   

    return reverse_data


# 等2-7秒
def wait_random_time(num1=2, num2=7):
    crawl_interval = random.uniform(num1, num2)
    print("等待", crawl_interval, "秒後發送下一次請求")
    time.sleep(crawl_interval)