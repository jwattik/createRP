# -*- coding: UTF-8 -*-

import uuid


# class Body(object):
#     def __init__(self, address=None, inn=None, name=None, phone=None):
#         self.address = address
#         self.inn = inn
#         self.id = str(uuid.uuid4())
#         self.name = name
#         self.phone = phone
#         self.settings = {
#             "isPostponeAllowed": False,
#             "isPriceEditAllowed": True,
#             "isContinueCheckClose": False,
#             "freeSaleBarcode": "219999999999",
#             "freeSaleVatTag": None,
#             "defaultVatTag": 1105,
#             "egaisWebUIURL": None,
#             "aboutModulPosUrl": "http://modulkassa.ru/help/mobilnaya-kassa-dlya-kass.php?bitrix_include_areas=Y"
#                                 "&clear_cache=Y",
#             "checkSettings": {
#                 "headerText": [
#                     ""
#                 ],
#                 "footerText": [
#                     ""
#                 ],
#                 "printCheckLink": False
#             },
#             "hardwareSettings": {
#                 "printerSettings": {
#                     "protocol": "dummy",
#                     "programmableFields": None,
#                     "accessCode": 0,
#                     "userCode": 30,
#                     "dataChannel": {
#                         "channel": "serial",
#                         "rate": 115200
#                     },
#                     "defaultTaxMode": None
#                 },
#                 "processing": {
#                     "protocol": "mock",
#                     "login": None,
#                     "password": None,
#                     "describe": None,
#                     "email": None,
#                     "phone": None
#                 },
#                 "scales": None
#             },
#             "egaisSettings": {
#                 "utmHost": "",
#                 "utmTimeout": 15,
#                 "kpp": None,
#                 "retailPointName": None,
#                 "shouldOpenTare": False,
#                 "handleSoftDrinks": False
#             },
#             "moveRemainsToNextShift": True,
#             "autoPayoutOnShiftClose": False,
#             "printOnShiftClose": [],
#             "positionRoundNumber": None,
#             "checkRoundNumber": None,
#             "catalogUpdateInterval": 5,
#             "statusUpdateInterval": None,
#             "returnWithoutSaleAllowed": True,
#             "ofdEnabled": False,
#             "ofdSettings": {
#                 "senderAddress": None
#             },
#             "fiscalServiceEnabled": False,
#             "weightBarcodeFormat": "^21([0-9]{5})([0-9]{5})",
#             "defaultTaxMode": "COMMON",
#             "orderSettings": {
#                 "barcodePrefix": None,
#                 "defaultDescription": None
#             },
#             "showBatteryReplacementNotification": False,
#             "stockBalanceEnabled": False,
#             "stopFnServiceOnErrors": False,
#             "tobaccoDatamatrixRequest": False,
#             "postponeAllowed": False,
#             "continueCheckClose": False,
#             "movePostponeToNextShift": False,
#             "freeSaleEnabled": True,
#             "priceEditAllowed": True
#         }

class Body(object):
    def __init__(self, posLinkToken=None):
        self.posLinkToken = posLinkToken