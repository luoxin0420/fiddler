import requests

url = "https://openapi.alipay.com/gateway.do?timestamp=2013-01-01 08:08:08&method=alipay.trade.fastpay.refund.query&app_id=14645&sign_type=RSA2&sign=ERITJKEIJKJHKKKKKKKHJEREEEEEEEEEEE&version=1.0&charset=GBK&biz_content="
params = {
    "trade_no": "20150320010101001",
    "out_trade_no": "2014112611001004680073956707",
    "out_request_no": "2014112611001004680073956707",
    "org_pid": "2088101117952222"
}
r = requests.request("post", url, params=params)
print(r.text)
