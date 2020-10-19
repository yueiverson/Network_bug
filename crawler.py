from bs4 import BeautifulSoup
import requests
import time
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
}#模仿一般瀏覽器
def request_weather(location):
    location_lists={'臺北市':'臺北市/臺北市2306179','新北市':'新北市/新北市-20070569','基隆市':'基隆市/基隆市-2306188','桃園市':'桃園市/桃園市-2298866','新竹市':'新竹市/新竹市-2306185',
    '苗栗市':'苗栗市/苗栗市-2301128','臺中市':'臺中市/臺中市-2306181','彰化市':'彰化市/彰化市-2306183','南投市':'南投市/南投市-2306204','雲林':'雲林/雲林-2347346','嘉義市':'嘉義市/嘉義市-2296315',
    '臺南市':'臺南市/臺南市-2306182','高雄市':'高雄市/高雄市-2306180','屏東市':'屏東市/屏東市-2306189','宜蘭市':'宜蘭市/宜蘭市-2306198','花蓮市':'花蓮市/花蓮市-2306187','臺東市':'臺東市/臺東市-2306190'}
    location=location_lists.get(location)
    url='https://tw.news.yahoo.com/weather/臺灣/'+ location
    website=requests.get(url,headers=HEADERS)
    html=website.content
    if website.status_code ==200:
        website_soup=BeautifulSoup(html,'html.parser')
        locations=website_soup.find_all("h1",class_="city Fz(2em)--sm Fz(3.7em)--lg Fz(3.3em) Fw(n) M(0) Trsdu(.3s) desktop_Lh(1) smartphone_Lh(1)")
        weathers=website_soup.find_all("span",class_="description Va(m) Px(2px) Fz(1.3em)--sm Fz(1.6em)",attrs={"data-reactid":"26"})
        temperatures=website_soup.find_all("span",class_="Va(t)",attrs={"data-reactid":"37"})
        for location in locations:
            for weather in weathers:
                for temperature in temperatures:
                    b={}
                    b['地點']=location.text
                    b['天氣']=weather.text
                    b['溫度']=temperature.text  
                    return b['地點'],b['天氣'],b['溫度']
    else:
        return '網頁載入失敗'
# location_lists=['臺北市/臺北市2306179','新北市/新北市-20070569','基隆市/基隆市-2306188','桃園市/桃園市-2298866','新竹市/新竹市-2306185',
# '苗栗市/苗栗市-2301128','臺中市/臺中市-2306181','彰化市/彰化市-2306183','南投市/南投市-2306204','雲林/雲林-2347346','嘉義市/嘉義市-2296315',
# '臺南市/臺南市-2306182','高雄市/高雄市-2306180','屏東市/屏東市-2306189','宜蘭市/宜蘭市-2306198','花蓮市/花蓮市-2306187','臺東市/臺東市-2306190']
# for location_list in location_lists:
#     url='https://tw.news.yahoo.com/weather/臺灣/'+ location_list
# a=request_website('嘉義市')
# print(a)
# print(request_website)
def request_ForeignExchange():
    website=requests.get('https://rate.bot.com.tw/xrt?Lang=zh-TW',headers=HEADERS)
    html=website.content
    a={}
    buys_list=[]
    sells_list=[]
    dollars_list=[]
    if website.status_code ==200: #請求連線成功
        website_soup=BeautifulSoup(html,'html.parser')
        dollars=website_soup.find_all("div",class_="visible-phone print_hide")
        buys=website_soup.find_all("td" ,class_="rate-content-cash text-right print_hide",attrs={"data-table":"本行現金買入"} )
        sells=website_soup.find_all("td" ,class_="rate-content-cash text-right print_hide",attrs={"data-table":"本行現金賣出"})
        for buy in buys:
            buys_list.append(buy.text)
        for sell in sells:
            sells_list.append(sell.text)
        merge_list=list(zip(buys_list,sells_list))
        # print(d)
        for dollar in dollars:
            dollar=dollar.text.strip() #刪除幣別前後空白字串
            dollars_list.append(dollar)          
        merge_dic=dict(zip(dollars_list,merge_list))
        # print(merge_dic)
        print(merge_dic["美金 (USD)"][0])
    else:
        print("網頁載入失敗")
# request_ForeignExchange()

