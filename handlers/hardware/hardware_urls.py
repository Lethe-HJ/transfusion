# coding=utf-8
from handlers.hardware.hardware_handler import *

hardware_urls = [
# 硬件接口
#     (r'/St_test', Testhandler),
    (r'/dispensary/inputbdn', DespensaryInputBednumInterface),  # 配药输入病床号
    (r'/dispensary/scan_dr', ScanDrugQRCodeInterface),  # 配药扫描药品条形码
    # (r'/dispensary/confirm', DispensaryConfirmInterface),  # 配药扫描药品条形码
    (r'/transfuse/sendmsgandaskhook', MsgRecvAndAskHookInterface),  #
    # (r'/transfuse/scan_pt', TransfuseScanPtInterface),  #

    # (r'/dispensary/scan_dr', DespensaryScanDrcodeInterface),

]