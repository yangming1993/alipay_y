# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse,redirect
from alipay.pay import AliPay
from django.views.decorators.csrf import csrf_exempt
import copy
ali = AliPay(
	appid="2016081900287704",
	app_notify_url="http://n18426f663.iask.in:10856/ali/notice/",
	app_private_key_path=r"C:\Users\ym\Desktop\secret_key_tools_RSA_win\RSA密钥\应用私钥2048.txt",
	alipay_public_key_path=r"C:\Users\ym\Desktop\secret_key_tools_RSA_win\RSA密钥\支付宝公钥.txt",  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
	debug=True,  # 默认False, 正式环境为False
	return_url="http://n18426f663.iask.in:10856/ali/return_url/")
url = ali.direct_pay(
	subject="测试订单",
	out_trade_no="201702223999", #随机订单，不能重复
	total_amount=9966
)

# Create your views here.
def index(request):

	re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
	return redirect(re_url)

@csrf_exempt
def notice(request):
	ret = request.POST
	if ali.verify(ret):
		#验证成功，则说明支付成功
		pass

	return HttpResponse('notice_url')

def return_url(request):
	# print(request.META['QUERY_STRING'])
	return HttpResponse('return_url')