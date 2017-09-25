#!/usr/bin/env python
#encoding: utf-8
'''
@author:ym

@time:2017/9/20
'''

# encoding:utf-8

from base64 import b64encode
import json
from urllib.parse import urlencode
import OpenSSL
import requests
def sign(params):
	sort_param = sorted([(key, value) for key, value in params.items()],
						key=lambda x: x[0], )
	content = '&'.join(['='.join(x) for x in sort_param]).encode()
	with open('./content2.txt','wb') as fw:
		fw.write(content)
	priKey = '''-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDOIrpDG0HXdNWU
xRPMyZXoKrVoP/aIYG9fAeKwdBduCltfcfmZ869jNDdrPxcRwZJjIJ40xjFHtfjI
r5/NUdjODg6OSTa4t0khWtALmSWfFdJNUCiqBAeSFtfOYbZVw1XoTAseD+zbDmCy
Two0R9xT6eoCbrenF42JwWJW4sNAExVGF3Ibrgels4rhxYTA5Dp/UqzwLA7S70Dm
oHUOIiMFY1IdiXl7t8Yp6Q7M4sZK+LfowC4aWbQudrcpovwJp1WYy7FoHEUmCQWR
4razWxpuTwsZlxHoiTBqpASIRQ0oA7wB8YN078yfls2ad64i3G9IYTTcCIJ9waaT
Hd8g8qcDAgMBAAECggEBALcrHq3gu5nzhJIEqTpw6lb6FGaFZ9D5OB2JNGEtV2B9
rYHbajsF0ZRqYtBWqG4rvqN86XfloQaiyWWywWIV13wJ+58tqYVrwHz2ECYuOMLr
BguTLf8dQ4jp6WvHYdlFkMGxSLO23PYuCXiISX35WOvrz/fHYEQG5stA3txr9amp
cdvJcOiKv93I4+3wwnm4Q8oL4gYsWOni6gGq2MeRxo0CmgzOJwbE8WuS+QzgE/pP
E/WrHNJitXvnoay9ZHFuweLtrEd79Jddy6pwm3VbYu6tSiaqBt6r2fEzFV3lIejJ
6XOIQ4ofxmCelK85MdxsoYSAZu+4XKKUv3DaUl6ImrkCgYEA+HmE6J7pIOJCt0+M
wjidLeQqJoACykP2Nc1X+vkiKNHXzN83pObbgzwPn9IjZxMqqYyxbyLbX/wXYilZ
79NaFqcdAZtwB65Nt7tv97ZUcM+cj6P2BRCASnoqC4osJNplKBd95OFj5A/Cj6n5
sueKx69dMNfx7xBJaf+8jWi/uY0CgYEA1GDxu78opPrIZmpQ/Rxvu1hRn3SWGUdt
0ZVlQEKFsryfzaOaKIFppyjb+d3minElVk4rndqiy0x+KJP9cv7OVR1InZGUvAWv
XCrk0n02qllwAcmnMqMxH4Woi6oi4N2UcIoWrMTvGgBvzRzufwQhMHGtKG+m85lI
YcI4awO/ls8CgYEA0+gvJYSBJf5RD6zUSr+lrQGtwO/jcUTMsc3SfsQCEfYEqUCl
YAlSpHWQjajVcI60D61hlXqQxSdled3yScpiRnd3EWvS+3n35f4A262wDhXBW+9l
XaRZBStyuCy6wSNQqgR+5bgjTNj0ATnhLmaxwOMaAxHnzw6AzdnAoIj5GfECgYBB
Mo2jPFjm5NIWlrbMLSmj0sYj9G+LzSDKgVl287UFnOBWCc5uduQPW/zD5To77+Yt
a4v6Rr9JN+9W16+r2MtQ18+OB74oRnqCCez7LVNV0mUPN2+rnOucqLSIQ6+3Zm6G
ae3yFfbs/YtU5XfV6Fej/pHQ4w3WpIzS7gPR3nG3gwKBgQDjk3pO9GUYLqbp7sNG
oVFWWIzooOiFiG2hW+OPvTCDtcorz3yP1EnUW/uodAU0gdy6JUs4UuAU3limngVR
JV8+jeHVM6bxiOT5uqdpI3ts9PkKEIEMh9UIrL6dAuXFUOxlv8hNjOQIvk8s3sR6
wd3lS6O6hxsyvcXs988ZNe7owg==
-----END PRIVATE KEY-----
'''

	private_key = OpenSSL.crypto.load_privatekey(OpenSSL.crypto.FILETYPE_PEM, priKey)
	return b64encode(OpenSSL.crypto.sign(private_key, content, 'sha256'))

if '__main__' == __name__:
	params = {}
	# params['a'] = '123'
	params['app_id'] = '2016081900287704'
	params['method'] = 'alipay.trade.app.pay'
	# params['format'] = 'JSON' #f
	params['charset'] = 'UTF-8'
	params['sign_type'] = 'RSA2'
	params['timestamp'] = '2017-09-22 10:05:56'
	params['version'] = '1.0'
	params['biz_content'] = {}
	params['biz_content']['out_trade_no'] = '20150320010101001'
	params['biz_content']['product_code'] = 'FAST_INSTANT_TRADE_PAY'
	params['biz_content']['total_amount'] = '88.88'
	params['biz_content']['subject'] = 'python支付宝支付'
	# params['biz_content']['body'] = '这是一个body部分'
	# params['biz_content']['timeout_express'] = '10m'
	# params['biz_content']['goods_type'] = '0'
	params['biz_content'] = json.dumps(params['biz_content'],  separators=(',', ':'),ensure_ascii=False)
	params['sign'] = sign(params)
	with open('./sign.txt','wb') as f:
		f.write(params['sign'])
	# params['notify_url'] = 'https://api.xx.com/receive_notify.htm' #f
	# params['return_url'] = '' #f
	sort_param = sorted([(key, value) for key, value in params.items()],
						key=lambda x: x[0])
	file = open('./signThing1.txt', 'wb')
	file.write('https://openapi.alipaydev.com/gateway.do?'.encode() + urlencode(params).encode())
	file.close()
