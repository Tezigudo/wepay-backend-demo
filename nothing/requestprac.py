# import requests
# # from scb_payment import request

# POST_REQUEST_URL = 'https://api-sandbox.partners.scb/partners/sandbox/v3/deeplink/transactions '

# API_KEY = 'l72f68aa3f522e46bda808f2db17ea69d2'
# API_SECRET = 'ca4e84d04fac40daa23ab60ed7397976'
# MERCHANT = '910749439870568'
# TERMINAL = '7946735318761'

# header = {
#     "Content-type": "application/json",
#     "Authorization": "Bearer 7578ff20-9142-4e0a-85d2-ca5624a9e126",
#     "ResourceOwnerId": API_KEY,
#     "RequestUId": "c41334ec-478a-11ed-b878-0242ac120002",
#     "Channel": "scbeasy"
# }

# # payload = {
# #     "paymentAmount": 100,
# #     "transactionType": "PAYMENT",
# #     "transactionSubType": "BPA",
# #     "ref1": "12345678",
# #     "ref2": "87654321",
# #     "ref3": "SCB",
# #     "accountTo": MERCHANT
# # }
# body = {
#     "transactionType": "PURCHASE",
#     "transactionSubType": [
#         "BP"
#     ],
#     "billPayment": {
#         "paymentAmount": 100.00,
#         "accountTo": "910749439870568",
#         "ref1": "12345678",
#         "ref2": "87654321",
#         "ref3": "SCB1234"
#     }
# }
# while True:
#     resp = requests.post(POST_REQUEST_URL, headers=header, data=body)
#     print(resp.content)

# # another_resp = requests.get(POST_REQUEST_URL, headers=header, data=body)
# # print(another_resp.status_code)
# # print(request.basic_request('POST', REQUEST_URL, header, payload))
# # print('\n\n\n\n\n\n\n\n\n')

# # s = request.basic_request('GET', REQUEST_URL, header, payload)

# # print(s)
# # # access token 228ecf52-41ce-4a51-aa60-77e2c94ceedc

# i4CtdVrqLhvdSBkPNUcMS2vk8k4pcND6:T1cHA7Vq31omDa1N


# i4CtdVrqLhvdSBkPNUcMS2vk8k4pcND6:T1cHA7Vq31omDa1N

# import requests

# URL = 'https://openapi-sandbox.kasikornbank.com/v1/qrpayment/request'
# header = {
#     "Authorization": "Bearer e8wXan10dAjKhW5wk8etjrt5hl0F",
#     "Content-Type": "application/json",
#     "x-test-mode": "true",
#     "env-id": "QR002"
# }

# # body = {
# #     "Partner transaction unique identify": "PARTNERTEST0001",
# #     "partnerId": "PTR1051673",
# #     "partnerSecret": "d4bded59200547bc85903574a293831b",
# #     "merchantId": "KB102057149704",
# #     "Request Time": "2022-10-09T10:22:18+0000",
# #     "QR Type": "3",
# #     "Amount": "100",
# #     "Currency Code": "THB",
# #     "Reference 1":	"INV001",
# #     "Reference 2": "HELLOWORLD",
# #     "Reference 3": "INV001",
# #     "Reference 4": "INV001"

# # }

# body = {
#     "partnerTxnUid": "PARTNERTEST0001",
#     "partnerId": "PTR1051673",
#     "partnerSecret": "d4bded59200547bc85903574a293831b",
#     "merchantId": "KB102057149704",
#     "requestDt": "2022-10-09T11:02:02+00:00",
#     "qrType": "3",
#     "txnAmount": "100",
#     "txnCurrencyCode": "THB",
#     "reference1": "INV001",
#     "reference2": "HELLOWORLD",
#     "reference3": "INV001",
#     "reference4": "INV001"
# }
# {
#     "partnerId": "PTR1051673",
#     "partnerSecret": "d4bded59200547bc85903574a293831b",
#     "merchantId": "KB102057149704",
#     "partnerTxnUid": "PARTNERTEST0002",
#     "OrigPartnerTxnUid": "PARTNERTEST0001",
#     "requestDt": "2022-10-09T11:22:49+00:00"
# }

# resp = requests.post(URL, data=body, headers=header)
# print(resp.status_code)
# print()
# print(resp.content)

# # {
# #     "Authorization": "Bearer i4CtdVrqLhvdSBkPNUcMS2vk8k4pcND6:T1cHA7Vq31omDa1N",
# #     "Content-Type": "application/json",
# #     "x-test-mode": "true",
# # }


# def get_access_token():
#     resp = requests.post("https://openapi-sandbox.kasikornbank.com/v2/oauth/token", headers={"Authorization": "Basic aTRDdGRWcnFMaHZkU0JrUE5VY01TMnZrOGs0cGNORDY6VDFjSEE3VnEzMW9tRGExTg==",
#                                                                                              "Content-Type": "application/x-www-form-urlencoded",
#                                                                                              "env-id": "OAUTH2",
#                                                                                              "x-test-mode": "true"}, data={
#         "grant_type": "client_credentials"
#     })
#     data = str(resp.content)

#     return data

# print(get_access_token())
# # {
#   "partnerId": "PTR1051673",
#   "partnerSecret": "d4bded59200547bc85903574a293831b",
#   "merchantId": "KB102057149704",
#     "partnerTxnUid": "PARTNERTEST0002",
# "OrigPartnerTxnUid": "PARTNERTEST0001",
# #     "requestDt": "2022-10-09T11:22:49+00:00"
# # }

# "Authorization": "Bearer DCF6PuiBdHNYlMv0GwcCeikc3nAU",
# # {

# {
#   "merchantId": "KB102057149704",
#   "partnerId": "PTR1051673",
#   "partnerSecret": "d4bded59200547bc85903574a293831b",
#   "origPartnerTxnUid": "PARTNERTEST0007",
#   "partnerTxnUid": "PARTNERTEST0004",
#   "requestDt": "2022-10-09T11:47:30+00:00"
# }
