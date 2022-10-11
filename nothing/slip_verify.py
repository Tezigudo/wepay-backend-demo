
from scb_payment import QRCodePayment

API_KEY = 'l72f68aa3f522e46bda808f2db17ea69d2'
API_SECRET = 'ca4e84d04fac40daa23ab60ed7397976'
MERCHANT = '910749439870568'
TERMINAL = '552124700718327'
BILLER = '910749439870568'

qr = QRCodePayment(API_KEY, API_SECRET, MERCHANT, TERMINAL, BILLER)

data = qr.gererate_qr_cs(amount=200, invoice="ABCDEI1233474B")['data']['qrRawData']

# from qrtools.qrtools import QR
print(data)



# my_qr = QR(filename='slip.JPG')

# my_qr.decode()

# print(my_qr.data)

# import cv2
# from pyzbar import pyzbar

# def read_barcodes(frame):
#     barcodes = pyzbar.decode(frame)
#     for barcode in barcodes:
#         x, y, w, h = barcode.rect
#         # 1
#         barcode_info = barcode.data.decode('utf-8')
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

#         # 2
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, barcode_info, (x + 6, y - 6),
#                     font, 2.0, (255, 255, 255), 1)
#         # 3
#         with open("barcode_result.txt", mode='w') as file:
#             file.write("Recognized Barcode:" + barcode_info)
#     return frame

# import cv2

# filename = 'slip.JPG'

# image = cv2.imread(filename)

# detector = cv2.QRCodeDetector()

# data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

# # if there is a QR code
# # print the data
# if vertices_array is not None:
#     print("QRCode data:")
#     print(data)
# else:
#     print("There was some error")


# from scb_payment import QRCodePayment

# API_KEY = 'l72f68aa3f522e46bda808f2db17ea69d2'
# API_SECRET = 'ca4e84d04fac40daa23ab60ed7397976'
# MERCHANT = '910749439870568'
# TERMINAL = '7946735318761'
# BILLER = '910749439870568'

# QRCodePayment()