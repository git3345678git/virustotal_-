


## 製作目的

有鑑於最近研究域名尋找真實ip時，很多情況下目標會加上cdn導致我們找不到對方的真實ip，這時可以利用歷史ip來定位看看，但ip手動反解出域名在判斷實在太費工，所以我製作了一個基於virustotal 資料庫的小爬蟲



### 歷史ip反解後的篩選

**ip反解後可以查看對應的域名的幾種情況**

1. ip屬與cdn 或是host shareing會解析出非常多的垃圾網站，這通常沒有價值
2. ip反解後如果是很少的域名代表這ip可能長期被某人租用，這就有參考價值，但不一定是同個站長了
3. ip反解後找到子站點，或是旁站，這很有可能還是同個站長


### 歷史網站

假設你看到了某個相似的域名或是感覺有可能是同個站長的旁站，但他已是N年前的域名早已過期，你可以藉助wayback machine 來調查，

**兩個前提**
1. wayback machine 有紀錄
2. 對方以前有開放80 443端口才有機會被收錄



### 子站，旁站在擴大攻擊面


假設你找到了子站旁站，或是你利用wayback 確認是同個業務，你可以再把這些域名蒐集起來在重複上面的動作。

甚至你可以蒐集完在利用subfinder 找出子域名，在一併重複上面動作



### 假設你定位出有可能的IP，不走cdn線路

1.你直接輸入ip 加上端口可以直接訪問(這通常是比較弱的站點)
2.對方要求一定要加上域名，你可以自行修改host檔使用本地dns解析。




###  maltego 畫出架構圖


我通常會使用maltego來可視化蒐集，但maltego免費版他媽的限制一次最多12筆輸出，你好不容易使用了virustotal 的key並使用他的插件回頭給你12筆輸出，真是太傷心了。

所以還是得靠自己，當然還沒研究maltego的自定義插件，之後搞不好可以去人工


### 小結

從一開始製作是為了純粹從歷史ip蒐集繞過cdn 演變成子站旁站蒐集，雖說不一定能夠繞過cdn，但
能夠跨大攻擊面作為情報蒐集也不錯拉。







## 使用方法


#### 準備 domains.txt
```
dmoe.in
dmoe.org
dmoe.us
```

#### get_domains_ip_history.py 獲取歷史ip
```
 python get_domains_ip_history.py -i domains.txt -o domains_ip_history.json
```


#### domains_ip_history.json
 
```
{
    "domains": [
        {
            "domain": "dmoe.in",
            "ip_history": {
                "172.67.223.28": {
                    "resolve_date": "2022-10-17 08:24:14"
                },
                "104.21.54.34": {
                    "resolve_date": "2022-10-17 08:24:14"
                },
                "65.108.74.52": {
                    "resolve_date": "2022-02-28 06:23:25"
                },
                "78.46.230.46": {
                    "resolve_date": "2021-05-28 03:58:24"
                },
                "95.216.104.156": {
                    "resolve_date": "2020-11-09 08:13:24"
                },
                "104.238.221.221": {
                    "resolve_date": "2020-10-04 07:46:35"
                }
            }
        },
        {
            "domain": "dmoe.org",
            "ip_history": {
                "67.198.205.152": {
                    "resolve_date": "2021-03-22 07:54:10"
                },
                "104.18.52.189": {
                    "resolve_date": "2020-04-21 03:35:03"
                },
                "104.18.53.189": {
                    "resolve_date": "2020-04-21 03:35:03"
                },
                "104.238.221.221": {
                    "resolve_date": "2020-04-20 05:23:28"
                },
                "44.227.65.245": {
                    "resolve_date": "2020-01-30 19:02:51"
                },
                "35.160.246.24": {
                    "resolve_date": "2019-11-29 18:59:09"
                },
                "72.52.4.119": {
                    "resolve_date": "2016-08-07 00:00:00"
                },
                "220.181.136.43": {
                    "resolve_date": "2015-12-31 00:00:00"
                }
            }
        },
        {
            "domain": "dmoe.us",
            "ip_history": {
                "198.27.67.8": {
                    "resolve_date": "2022-09-14 09:25:22"
                },
                "67.198.205.152": {
                    "resolve_date": "2019-11-29 18:00:55"
                }
            }
        }
    ]
}
```

#### ip_reverse.py 讀取 domains_ip_history.json 輸出 domains_ip_reverse.json
```
python ip_reverse.py -i domains_ip_history.json -o domains_ip_reverse.json
```


#### domains_ip_reverse.json
```
{
    "domains": [
        {
            "domain": "dmoe.in",
            "ip_history": {
                "172.67.223.28": {
                    "resolve_date": "2022-10-17 08:24:14",
                    "ip_reverse_data": {
                        "garansino1.cfd": "2024-05-30 17:39:49",
                        "shahram.shahram1510.workers.dev": "2024-05-29 16:04:42",
                        "montero-sport-2017-owners-manual-pdf.vepajufaji.cfd": "2024-05-29 12:34:13",
                        "www.victorinoxknivesus.com": "2024-05-29 11:42:15",
                        "thoiemxin189.win": "2024-05-28 16:07:33",
                        "mahdi.ughhhhhh.monster": "2024-05-28 04:32:15",
                        "long-pine-6bd7.mehrdad-dmc1370701901.workers.dev": "2024-05-28 02:43:54",
                        "super-wave-df70.mehrdad-dmc1370701901.workers.dev": "2024-05-27 23:27:22",
                        "newfreenodes.shahram1510.workers.dev": "2024-05-27 18:42:27",
                        "macanqq.lat": "2024-05-27 16:15:26",
                        "webmail.tetden.com": "2024-05-26 19:51:39",
                        "cpcontacts.tetden.com": "2024-05-26 19:51:39",
                        "mail.tetden.com": "2024-05-26 19:51:39",
                        "cpcalendars.tetden.com": "2024-05-26 19:51:38",
                        "webdisk.tetden.com": "2024-05-26 19:51:37",
                        "cpanel.tetden.com": "2024-05-26 19:51:30",
                        "www.tetden.com": "2024-05-26 18:42:42",
                        "www.pylingual.io": "2024-05-26 12:43:11",
                        "www.thebridge.ma": "2024-05-26 11:16:14",
                        "kpy.uk": "2024-05-26 00:18:36",
                        "samir.shahram1510.workers.dev": "2024-05-25 22:11:47",
                        "sam.shahram1510.workers.dev": "2024-05-25 20:56:12",
                        "www.turkurollerderby.com": "2024-05-25 08:37:20",
                        "get-elderly-day-care-centers.today": "2024-05-24 23:54:19",
                        "towulogo.vepajufaji.cfd": "2024-05-24 20:37:44",
                        "el-regreso-ala-caba-a-pdf-gratis.vepajufaji.cfd": "2024-05-24 20:29:39",
                        "annyluxury.com": "2024-05-24 16:15:32",
                        "differentcups.com": "2024-05-24 16:11:19",
                        "0524.lt.gitski.work": "2024-05-24 05:14:20",
                        "dl-evernight.candyhouse.eu.org": "2024-05-24 02:57:18"
                    }
                },
                "104.21.54.34": {
                    "resolve_date": "2022-10-17 08:24:14",
                    "ip_reverse_data": {
                        "garansino1.cfd": "2024-05-30 17:39:49",
                        "shahram.shahram1510.workers.dev": "2024-05-29 16:04:42",
                        "montero-sport-2017-owners-manual-pdf.vepajufaji.cfd": "2024-05-29 12:38:40",
                        "www.victorinoxknivesus.com": "2024-05-29 11:42:56",
                        "thoiemxin189.win": "2024-05-28 16:07:33",
                        "mahdi.ughhhhhh.monster": "2024-05-28 04:32:15",
                        "long-pine-6bd7.mehrdad-dmc1370701901.workers.dev": "2024-05-28 02:43:54",
                        "super-wave-df70.mehrdad-dmc1370701901.workers.dev": "2024-05-27 23:27:22",
                        "newfreenodes.shahram1510.workers.dev": "2024-05-27 18:42:27",
                        "macanqq.lat": "2024-05-27 16:15:26",
                        "webmail.tetden.com": "2024-05-26 19:51:39",
                        "cpcontacts.tetden.com": "2024-05-26 19:51:39",
                        "mail.tetden.com": "2024-05-26 19:51:39",
                        "cpcalendars.tetden.com": "2024-05-26 19:51:38",
                        "webdisk.tetden.com": "2024-05-26 19:51:37",
                        "cpanel.tetden.com": "2024-05-26 19:51:30",
                        "www.tetden.com": "2024-05-26 18:42:42",
                        "www.pylingual.io": "2024-05-26 12:43:16",
                        "www.thebridge.ma": "2024-05-26 11:16:14",
                        "kpy.uk": "2024-05-26 00:18:36",
                        "samir.shahram1510.workers.dev": "2024-05-25 22:11:47",
                        "sam.shahram1510.workers.dev": "2024-05-25 20:56:12",
                        "turkurollerderby.com": "2024-05-25 08:37:23",
                        "www.turkurollerderby.com": "2024-05-25 08:37:20",
                        "get-elderly-day-care-centers.today": "2024-05-24 23:54:19",
                        "towulogo.vepajufaji.cfd": "2024-05-24 20:37:44",
                        "el-regreso-ala-caba-a-pdf-gratis.vepajufaji.cfd": "2024-05-24 20:34:27",
                        "annyluxury.com": "2024-05-24 16:15:32",
                        "differentcups.com": "2024-05-24 16:11:19",
                        "0524.lt.gitski.work": "2024-05-24 05:14:20"
                    }
                },
                "65.108.74.52": {
                    "resolve_date": "2022-02-28 06:23:25",
                    "ip_reverse_data": {
                        "lgmbspz.vfkslayowiew.hath.network": "2023-05-14 15:04:29",
                        "gyvywlj.vfkslayowiew.hath.network": "2023-05-14 02:02:24",
                        "vkxwokx.vfkslayowiew.hath.network": "2023-05-13 00:42:47",
                        "xltgjet.vfkslayowiew.hath.network": "2023-05-11 16:02:39",
                        "xtrsruk.vfkslayowiew.hath.network": "2023-05-09 20:09:01",
                        "yyepewv.vfkslayowiew.hath.network": "2023-05-08 10:04:03",
                        "mjgxmut.vfkslayowiew.hath.network": "2023-05-07 15:07:02",
                        "sllboup.vfkslayowiew.hath.network": "2023-05-06 10:13:26",
                        "xuuexfv.vfkslayowiew.hath.network": "2023-05-05 10:36:56",
                        "sptjlaw.vfkslayowiew.hath.network": "2023-05-04 13:40:47",
                        "pjbqtjy.vfkslayowiew.hath.network": "2023-05-01 11:14:31",
                        "jxcyhpm.vfkslayowiew.hath.network": "2023-04-30 18:49:08",
                        "cqwcvcw.vfkslayowiew.hath.network": "2023-04-30 06:29:14",
                        "glgkyzi.vfkslayowiew.hath.network": "2023-04-27 12:18:09",
                        "pgvzlbw.vfkslayowiew.hath.network": "2023-04-25 12:52:52",
                        "oxhabzm.vfkslayowiew.hath.network": "2023-04-24 15:55:06",
                        "epaahef.vfkslayowiew.hath.network": "2023-04-21 17:23:13",
                        "zpnlkzr.vfkslayowiew.hath.network": "2023-04-20 23:10:51",
                        "tacujjg.vfkslayowiew.hath.network": "2023-04-19 19:21:41",
                        "jljoevo.vfkslayowiew.hath.network": "2023-04-16 14:29:27",
                        "phwqprm.vfkslayowiew.hath.network": "2023-04-14 11:12:46",
                        "xosuskq.vfkslayowiew.hath.network": "2023-04-13 16:11:29",
                        "hmuqoxf.vfkslayowiew.hath.network": "2023-04-10 20:35:04",
                        "pivylmk.vfkslayowiew.hath.network": "2023-04-09 13:43:49",
                        "awnoxjf.vfkslayowiew.hath.network": "2023-04-08 23:19:54",
                        "qypimtn.vfkslayowiew.hath.network": "2023-04-07 12:57:16",
                        "kidajot.vfkslayowiew.hath.network": "2023-04-06 18:50:12",
                        "vlasoaa.vfkslayowiew.hath.network": "2023-04-05 20:02:15",
                        "zhciqcb.vfkslayowiew.hath.network": "2023-04-02 15:40:01",
                        "sedcwkn.vfkslayowiew.hath.network": "2023-03-31 17:53:16"
                    }
                },
                "78.46.230.46": {
                    "resolve_date": "2021-05-28 03:58:24",
                    "ip_reverse_data": {
                        "frawards.mpass.gr": "2022-07-18 07:44:11",
                        "frawards.fra-alliance.com": "2022-07-18 07:13:39",
                        "www.dmoe.in": "2021-05-28 03:58:27",
                        "dmoe.in": "2021-05-28 03:58:24",
                        "eroero.moe": "2020-12-04 00:04:15",
                        "lululu.moe": "2020-05-15 02:05:22",
                        "www.lululu.moe": "2020-05-15 02:05:20",
                        "z.thoma.cc": "2020-03-28 11:43:38",
                        "verticaltechedge.com": "2019-10-17 18:33:56"
                    }
                },
                "95.216.104.156": {
                    "resolve_date": "2020-11-09 08:13:24",
                    "ip_reverse_data": {
                        "dmoe.in": "2020-11-09 08:13:24",
                        "www.dmoe.in": "2020-11-09 08:13:18",
                        "pic.dmoe.in": "2020-11-09 07:46:28",
                        "mail.lyngby-boldklub.dk": "2020-04-14 15:47:44",
                        "lyngbyboldklub.dk": "2019-12-06 23:13:15",
                        "www.lyngbyboldklub.dk": "2019-12-06 23:13:15",
                        "www.lyngby-boldklub.dk": "2019-12-06 23:13:13",
                        "lyngby-boldklub.dk": "2019-12-06 23:13:13",
                        "ns2.itwebhotel.dk": "2019-11-30 17:58:43",
                        "jvalbak.dk": "2019-11-18 12:04:32",
                        "www.jvalbak.dk": "2019-11-18 12:04:27",
                        "ns3.itwebhotel.dk": "2018-09-03 20:07:04"
                    }
                },
                "104.238.221.221": {
                    "resolve_date": "2020-10-04 07:46:35",
                    "ip_reverse_data": {
                        "pic.dmoe.in": "2020-10-04 07:52:46",
                        "dmoe.in": "2020-10-04 07:46:35",
                        "www.dmoe.in": "2020-10-04 07:46:35",
                        "pic.dmoe.org": "2020-04-20 06:32:59",
                        "dmoe.org": "2020-04-20 05:23:28",
                        "www.dmoe.org": "2020-04-20 05:23:26",
                        "maczap.com": "2017-05-25 00:00:00",
                        "benevian.com": "2017-05-19 00:00:00"
                    }
                }
            }
        },
        {
            "domain": "dmoe.org",
            "ip_history": {
                "67.198.205.152": {
                    "resolve_date": "2021-03-22 07:54:10",
                    "ip_reverse_data": {
                        "408.isb.moe": "2022-09-14 05:09:51",
                        "ahx.bb10.vip": "2022-03-17 07:42:20",
                        "www.dmoe.moe": "2021-03-22 07:54:10",
                        "dmoe.org": "2021-03-22 07:54:10",
                        "dmoe.moe": "2021-03-22 07:54:09",
                        "www.dmoe.org": "2021-03-22 07:54:09",
                        "xcy.plus": "2020-11-21 03:03:24",
                        "www.dmoe.us": "2019-11-29 18:00:56",
                        "dmoe.us": "2019-11-29 18:00:55"
                    }
                },
                "104.18.52.189": {
                    "resolve_date": "2020-04-21 03:35:03",
                    "ip_reverse_data": {
                        "sakilive.com": "2024-05-10 00:12:37",
                        "arc-hhi.com": "2021-01-15 14:01:10",
                        "www.beachnewseveryday.com": "2021-01-14 22:55:40",
                        "server.simpleupload.net": "2021-01-14 21:54:20",
                        "www.jinbupal.com": "2021-01-14 13:25:33",
                        "alzatooverseas.com": "2021-01-14 12:11:27",
                        "mail.comune.simpleupload.net": "2021-01-14 08:49:00",
                        "tu.woyewan.cc": "2021-01-14 07:50:14",
                        "correo.simpleupload.net": "2021-01-14 07:36:58",
                        "mail9.simpleupload.net": "2021-01-14 05:22:24",
                        "mailgw.simpleupload.net": "2021-01-13 16:24:28",
                        "tonsavacon.ga": "2021-01-13 16:02:24",
                        "mdmamediatraining.com": "2021-01-13 15:55:34",
                        "shops-expos.news": "2021-01-13 13:53:03",
                        "a.mx.simpleupload.net": "2021-01-13 09:12:16",
                        "slemarcomulpa.tk": "2021-01-13 07:20:19",
                        "fromidalpelon.gq": "2021-01-12 19:17:11",
                        "welcome888.site": "2021-01-12 18:00:24",
                        "videosxxxbest.xyz": "2021-01-12 15:16:44",
                        "www.tv9800.com": "2021-01-12 14:40:40",
                        "barracuda.simpleupload.net": "2021-01-12 12:09:26",
                        "it.roasidcaro.tk": "2021-01-12 09:37:11",
                        "gateway.simpleupload.net": "2021-01-12 05:03:50",
                        "vmail.simpleupload.net": "2021-01-12 04:17:55",
                        "peperlefwsa.tk": "2021-01-12 01:00:36",
                        "belinkersonline.com.br": "2021-01-11 19:54:20",
                        "host.simpleupload.net": "2021-01-11 17:57:32",
                        "smtp.mail.simpleupload.net": "2021-01-11 15:44:33",
                        "server2.simpleupload.net": "2021-01-11 15:25:26",
                        "mail10.simpleupload.net": "2021-01-11 13:06:35"
                    }
                },
                "104.18.53.189": {
                    "resolve_date": "2020-04-21 03:35:03",
                    "ip_reverse_data": {
                        "arc-hhi.com": "2021-01-14 23:37:07",
                        "www.beachnewseveryday.com": "2021-01-14 22:55:40",
                        "server.simpleupload.net": "2021-01-14 21:54:20",
                        "www.jinbupal.com": "2021-01-14 13:25:33",
                        "alzatooverseas.com": "2021-01-14 12:11:27",
                        "mail.comune.simpleupload.net": "2021-01-14 08:48:59",
                        "tu.woyewan.cc": "2021-01-14 07:50:14",
                        "correo.simpleupload.net": "2021-01-14 07:36:57",
                        "mail9.simpleupload.net": "2021-01-14 05:22:24",
                        "mailgw.simpleupload.net": "2021-01-13 16:24:29",
                        "tonsavacon.ga": "2021-01-13 16:02:24",
                        "mdmamediatraining.com": "2021-01-13 15:55:34",
                        "shops-expos.news": "2021-01-13 13:53:03",
                        "a.mx.simpleupload.net": "2021-01-13 09:12:16",
                        "slemarcomulpa.tk": "2021-01-13 07:20:19",
                        "leoberhandthernprec.ga": "2021-01-13 06:11:48",
                        "fromidalpelon.gq": "2021-01-12 19:17:11",
                        "welcome888.site": "2021-01-12 18:00:24",
                        "www.tv9800.com": "2021-01-12 14:40:40",
                        "barracuda.simpleupload.net": "2021-01-12 12:09:26",
                        "it.roasidcaro.tk": "2021-01-12 09:37:11",
                        "ganganbb.com": "2021-01-12 09:00:35",
                        "gateway.simpleupload.net": "2021-01-12 05:03:50",
                        "vmail.simpleupload.net": "2021-01-12 04:17:55",
                        "peperlefwsa.tk": "2021-01-12 01:00:36",
                        "belinkersonline.com.br": "2021-01-11 19:54:20",
                        "host.simpleupload.net": "2021-01-11 17:57:32",
                        "smtp.mail.simpleupload.net": "2021-01-11 15:44:33",
                        "server2.simpleupload.net": "2021-01-11 15:25:26",
                        "mail10.simpleupload.net": "2021-01-11 13:06:35"
                    }
                },
                "104.238.221.221": {
                    "resolve_date": "2020-04-20 05:23:28",
                    "ip_reverse_data": {
                        "pic.dmoe.in": "2020-10-04 07:52:46",
                        "dmoe.in": "2020-10-04 07:46:35",
                        "www.dmoe.in": "2020-10-04 07:46:35",
                        "pic.dmoe.org": "2020-04-20 06:32:59",
                        "dmoe.org": "2020-04-20 05:23:28",
                        "www.dmoe.org": "2020-04-20 05:23:26",
                        "maczap.com": "2017-05-25 00:00:00",
                        "benevian.com": "2017-05-19 00:00:00"
                    }
                },
                "44.227.65.245": {
                    "resolve_date": "2020-01-30 19:02:51",
                    "ip_reverse_data": {
                        "dolphin.lighting": "2024-05-31 06:16:41",
                        "futurebloom.org": "2024-05-31 06:16:20",
                        "cc-shbfinance-com-vn.microcycas.com": "2024-05-31 06:12:55",
                        "www.tastetempel.com": "2024-05-31 05:55:52",
                        "harleton.co": "2024-05-31 05:54:21",
                        "maltern.cc": "2024-05-31 05:34:05",
                        "griffinhoward.com": "2024-05-31 05:33:52",
                        "dh503393ad.buzz": "2024-05-31 05:23:56",
                        "affiliatewithdrmac.com": "2024-05-31 04:53:16",
                        "cc-shbfinance-com-vn.cycadgarden.com": "2024-05-31 03:45:52",
                        "paramarines.space": "2024-05-31 03:17:57",
                        "internal.albusd.dev": "2024-05-31 03:13:08",
                        "consciouseffort.dev": "2024-05-31 03:12:29",
                        "tifflabs-software.org": "2024-05-31 03:06:34",
                        "henrymovieblog.com": "2024-05-31 01:48:15",
                        "ruschev.dev": "2024-05-31 01:25:13",
                        "luanderson.dev": "2024-05-31 01:21:01",
                        "gluchat.ai": "2024-05-31 00:32:13",
                        "tifflabs.cfd": "2024-05-30 23:16:54",
                        "cc.shbfinance.com-vn.cycadgarden.com": "2024-05-30 23:06:48",
                        "www.pensacolastartup.community": "2024-05-30 23:01:05",
                        "gwp.meetcv.com": "2024-05-30 22:52:45",
                        "nmlsconsumeraccess.org.trade": "2024-05-30 22:51:31",
                        "www.nmlsconsumeraccess.org.trade": "2024-05-30 22:51:28",
                        "www.gomountfoodie.com": "2024-05-30 22:32:42",
                        "gomountfoodie.com": "2024-05-30 22:32:40",
                        "callgreenyards.com": "2024-05-30 21:07:37",
                        "mouad.us": "2024-05-30 20:12:13",
                        "309200.xyz": "2024-05-30 20:06:37",
                        "sleepysucculent.co": "2024-05-30 20:04:25"
                    }
                },
                "35.160.246.24": {
                    "resolve_date": "2019-11-29 18:59:09",
                    "ip_reverse_data": {
                        "steven.style": "2023-06-24 02:34:19",
                        "goatbanner.com": "2022-09-09 03:53:17",
                        "aura.cx": "2021-06-08 15:12:38",
                        "mx10.sunshyne.tv": "2021-06-08 09:11:49",
                        "zimbra.sunshyne.tv": "2021-06-06 10:09:10",
                        "server1.sunshyne.tv": "2021-06-06 10:04:33",
                        "hermes.sunshyne.tv": "2021-04-07 11:13:55",
                        "mx0.sunshyne.tv": "2021-03-27 16:38:48",
                        "relay.sunshyne.tv": "2021-03-26 10:08:16",
                        "newmail.sunshyne.tv": "2021-03-25 18:31:13",
                        "poczta.sunshyne.tv": "2021-03-25 14:39:59",
                        "mailhost.sunshyne.tv": "2021-03-23 14:55:08",
                        "auth.sunshyne.tv": "2021-03-04 00:08:13",
                        "webmail.sunshyne.tv": "2021-03-01 03:55:12",
                        "ftp.sunshyne.tv": "2021-02-24 19:53:43",
                        "mailout.sunshyne.tv": "2021-02-24 09:28:44",
                        "imap.sunshyne.tv": "2021-02-23 05:53:07",
                        "imap2.sunshyne.tv": "2021-02-15 12:47:49",
                        "m.sunshyne.tv": "2021-02-09 18:22:27",
                        "moonbasela.com": "2021-02-07 14:17:27",
                        "authsmtp.sunshyne.tv": "2021-02-07 12:10:07",
                        "mail1.sunshyne.tv": "2021-02-06 14:11:06",
                        "www2.sunshyne.tv": "2021-02-05 10:16:25",
                        "www1.sunshyne.tv": "2021-02-05 04:30:00",
                        "postmaster.sunshyne.tv": "2021-02-04 16:03:31",
                        "secure.sunshyne.tv": "2021-02-01 12:43:24",
                        "mailserver.sunshyne.tv": "2021-01-29 13:02:36",
                        "imap1.sunshyne.tv": "2021-01-29 08:24:50",
                        "mail3.sunshyne.tv": "2021-01-27 09:54:45",
                        "mailsrv.sunshyne.tv": "2021-01-26 17:57:53"
                    }
                },
                "72.52.4.119": {
                    "resolve_date": "2016-08-07 00:00:00",
                    "ip_reverse_data": {
                        "www.topread.com": "2024-04-09 05:12:29",
                        "admin.timeoutberlin.com": "2024-04-09 03:53:35",
                        "shop.sdp.com": "2024-03-13 08:22:24",
                        "www.shop.sdp.com": "2024-03-13 08:21:21",
                        "2fwww.sdp.com": "2024-02-21 03:22:19",
                        "wp.radiofona.net": "2024-02-02 15:46:19",
                        "mymwatch.sdp.com": "2023-12-30 01:29:52",
                        "nd.sdp.com": "2023-09-29 00:26:23",
                        "com.nd.sdp.com": "2023-09-29 00:25:53",
                        "dpworld.southampton.com": "2023-09-10 22:26:09",
                        "app.dpworld.southampton.com": "2023-09-10 22:25:38",
                        "appgate.sdp.com": "2023-07-18 20:58:37",
                        "bin.appgate.sdp.com": "2023-07-18 20:57:45",
                        "www.scotairways.com": "2023-07-14 05:28:18",
                        "blog.cambo.org": "2023-07-04 04:50:51",
                        "bx.terracoin.org": "2023-06-16 00:14:22",
                        "pdns-34.sdp.com": "2023-05-05 10:13:07",
                        "pdns-12.sdp.com": "2023-05-05 10:13:06",
                        "pdns-36.sdp.com": "2023-05-05 10:13:06",
                        "pdns-35.sdp.com": "2023-05-05 10:13:05",
                        "pdns-37.sdp.com": "2023-04-24 12:39:27",
                        "my.sdp.com": "2023-02-14 23:11:53",
                        "workforce.sdp.com": "2023-02-07 06:31:40",
                        "www.lempiredeschattes.com": "2022-12-31 21:53:09",
                        "www.asexe.com": "2022-12-31 21:53:04",
                        "www.renholder.com": "2022-12-06 15:19:48",
                        "www.1sexe1.com": "2022-12-06 14:42:09",
                        "runlogin.sdp.com": "2022-11-18 07:03:30",
                        "www.runlogin.sdp.com": "2022-11-18 07:03:05",
                        "aaa.sdp.com": "2022-09-28 02:21:08"
                    }
                },
                "220.181.136.43": {
                    "resolve_date": "2015-12-31 00:00:00",
                    "ip_reverse_data": {
                        "hinaron.com": "2019-09-13 00:38:39",
                        "lokong.net": "2017-04-23 00:00:00",
                        "dailyblog-dailyblog.stor.sinaapp.com": "2017-04-13 00:00:00",
                        "gllue.sinaapp.com": "2017-04-13 00:00:00",
                        "njsxxjc.com": "2017-04-13 00:00:00",
                        "pythontip-img.stor.sinaapp.com": "2017-04-13 00:00:00",
                        "snapi.sinaapp.com": "2017-04-13 00:00:00",
                        "313201595.applinzi.com": "2017-04-12 00:00:00",
                        "bitell.sinaapp.com": "2017-04-12 00:00:00",
                        "iheka0212-iheka0212.stor.sinaapp.com": "2017-04-12 00:00:00",
                        "israel.sinaapp.com": "2017-04-12 00:00:00",
                        "milatula.cn": "2017-04-12 00:00:00",
                        "ourmysql.sinaapp.com": "2017-04-12 00:00:00",
                        "sunzibingfa.sinaapp.com": "2017-04-12 00:00:00",
                        "www.firstshotz.com": "2017-04-12 00:00:00",
                        "www.jssdk.sinaapp.com": "2017-04-12 00:00:00",
                        "www.pptvq.com": "2017-04-12 00:00:00",
                        "www.xiaoxiongyouhao.com": "2017-04-12 00:00:00",
                        "cs.yzfyy.net": "2017-04-11 00:00:00",
                        "forexbonus.sinaapp.com": "2017-04-11 00:00:00",
                        "hqlong.com": "2017-04-11 00:00:00",
                        "ibar.sinaapp.com": "2017-04-11 00:00:00",
                        "lyhzw.sinaapp.com": "2017-04-11 00:00:00",
                        "neihanmanhua.vipappsina.com": "2017-04-11 00:00:00",
                        "newtab-newtab.stor.sinaapp.com": "2017-04-11 00:00:00",
                        "qiyeqiang.vipsinaapp.com": "2017-04-11 00:00:00",
                        "ttqwe.applinzi.com": "2017-04-11 00:00:00",
                        "wereadchina.com": "2017-04-11 00:00:00",
                        "www.mengjx.com": "2017-04-11 00:00:00",
                        "www.namisj.com": "2017-04-11 00:00:00"
                    }
                }
            }
        },
        {
            "domain": "dmoe.us",
            "ip_history": {
                "198.27.67.8": {
                    "resolve_date": "2022-09-14 09:25:22",
                    "ip_reverse_data": {
                        "xahprtj.fbotnmroccwt.hath.network": "2023-11-16 20:59:33",
                        "mcbvlgv.fbotnmroccwt.hath.network": "2023-11-14 12:37:04",
                        "zpgkaxp.fbotnmroccwt.hath.network": "2023-11-12 04:43:31",
                        "xynajyi.fbotnmroccwt.hath.network": "2023-11-08 13:30:24",
                        "fuskegd.fbotnmroccwt.hath.network": "2023-11-08 01:17:42",
                        "qzcbwzi.fbotnmroccwt.hath.network": "2023-11-05 08:23:32",
                        "vetcvhv.fbotnmroccwt.hath.network": "2023-11-05 00:46:59",
                        "tnrxquo.fbotnmroccwt.hath.network": "2023-11-02 22:15:57",
                        "docnrbz.fbotnmroccwt.hath.network": "2023-10-31 08:15:22",
                        "eqnftan.fbotnmroccwt.hath.network": "2023-10-27 08:09:40",
                        "uirbymo.fbotnmroccwt.hath.network": "2023-10-25 03:58:54",
                        "aovqdel.fbotnmroccwt.hath.network": "2023-10-24 02:05:40",
                        "wpyezmr.fbotnmroccwt.hath.network": "2023-10-21 16:14:14",
                        "ndyowzn.fbotnmroccwt.hath.network": "2023-10-15 16:14:25",
                        "ijwmpks.fbotnmroccwt.hath.network": "2023-10-13 06:43:55",
                        "uhjamzv.fbotnmroccwt.hath.network": "2023-10-11 04:16:01",
                        "olwxlcr.fbotnmroccwt.hath.network": "2023-10-09 21:57:03",
                        "vixmwcn.fbotnmroccwt.hath.network": "2023-10-08 20:41:26",
                        "vvujoaq.fbotnmroccwt.hath.network": "2023-10-07 15:07:54",
                        "safpxlq.fbotnmroccwt.hath.network": "2023-10-06 10:58:15",
                        "rvzvips.fbotnmroccwt.hath.network": "2023-10-02 16:56:30",
                        "yldcliw.fbotnmroccwt.hath.network": "2023-09-30 21:58:38",
                        "thuevtl.fbotnmroccwt.hath.network": "2023-09-28 05:51:11",
                        "seraqom.fbotnmroccwt.hath.network": "2023-09-28 03:17:26",
                        "xcqjyox.fbotnmroccwt.hath.network": "2023-09-26 10:31:28",
                        "jwganks.fbotnmroccwt.hath.network": "2023-09-25 03:23:11",
                        "pmzzzkm.fbotnmroccwt.hath.network": "2023-09-20 11:05:19",
                        "uxiajqn.fbotnmroccwt.hath.network": "2023-09-18 10:02:02",
                        "iknlhrd.fbotnmroccwt.hath.network": "2023-09-11 05:25:09",
                        "ijjhswn.fbotnmroccwt.hath.network": "2023-09-09 09:33:34"
                    }
                },
                "67.198.205.152": {
                    "resolve_date": "2019-11-29 18:00:55",
                    "ip_reverse_data": {
                        "408.isb.moe": "2022-09-14 05:09:51",
                        "ahx.bb10.vip": "2022-03-17 07:42:20",
                        "www.dmoe.moe": "2021-03-22 07:54:10",
                        "dmoe.org": "2021-03-22 07:54:10",
                        "dmoe.moe": "2021-03-22 07:54:09",
                        "www.dmoe.org": "2021-03-22 07:54:09",
                        "xcy.plus": "2020-11-21 03:03:24",
                        "www.dmoe.us": "2019-11-29 18:00:56",
                        "dmoe.us": "2019-11-29 18:00:55"
                    }
                }
            }
        }
    ]
}
```


#### data_graber.py 簡單輸出


```
# 輸出所有歷史ip
python data_graber.py -i domains_ip_reverse.json 

# -ip 輸出某個ip的reverse
python data_graber.py -i domains_ip_reverse.json -ip 220.181.136.43

# -date 輸出某個ip的reverse + 日期
python data_graber.py -i domains_ip_reverse.json -ip 220.181.136.43 -date
```


#### 輸出
```
dmoe.in
172.67.223.28   - 2022-10-17 08:24:14
104.21.54.34    - 2022-10-17 08:24:14
65.108.74.52    - 2022-02-28 06:23:25
78.46.230.46    - 2021-05-28 03:58:24
95.216.104.156  - 2020-11-09 08:13:24
104.238.221.221 - 2020-10-04 07:46:35


dmoe.org
67.198.205.152  - 2021-03-22 07:54:10
104.18.52.189   - 2020-04-21 03:35:03
104.18.53.189   - 2020-04-21 03:35:03
104.238.221.221 - 2020-04-20 05:23:28
44.227.65.245   - 2020-01-30 19:02:51
35.160.246.24   - 2019-11-29 18:59:09
72.52.4.119     - 2016-08-07 00:00:00
220.181.136.43  - 2015-12-31 00:00:00


dmoe.us
198.27.67.8     - 2022-09-14 09:25:22
67.198.205.152  - 2019-11-29 18:00:55
```




#### 搭配其他工具輸出方式
```
查找關鍵字 dmoe  的域名
cat formatted_domains_ip_reverse.json | grep "dmoe" | grep -v 'domain' | awk -F'"' '{print $2}' | sort | uniq


查找多個域名 dmoe | sunshyne
cat formatted_domains_ip_reverse.json | grep "dmoe\|sunshyne" | grep -v 'domain' | awk -F'"' '{print $2}' | sort | uniq


```


#### 輸出方便複製到 maltego 
```
authsmtp.sunshyne.tv
auth.sunshyne.tv
dmoe.in
dmoe.moe
dmoe.org
dmoe.us
ftp.sunshyne.tv
hermes.sunshyne.tv
imap1.sunshyne.tv
imap2.sunshyne.tv
imap.sunshyne.tv
mail1.sunshyne.tv
mail3.sunshyne.tv
mailhost.sunshyne.tv
mailout.sunshyne.tv
mailserver.sunshyne.tv
mailsrv.sunshyne.tv
m.sunshyne.tv
mx0.sunshyne.tv
mx10.sunshyne.tv
newmail.sunshyne.tv
pic.dmoe.in
pic.dmoe.org
poczta.sunshyne.tv
postmaster.sunshyne.tv
relay.sunshyne.tv
secure.sunshyne.tv
server1.sunshyne.tv
webmail.sunshyne.tv
www1.sunshyne.tv
www2.sunshyne.tv
www.dmoe.in
www.dmoe.moe
www.dmoe.org
www.dmoe.us
zimbra.sunshyne.tv
```