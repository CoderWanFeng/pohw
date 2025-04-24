from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkocr.v1.region.ocr_region import OcrRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkocr.v1 import *
from loguru import logger

from pohw.lib.Config import pohwConfig


class OCR(pohwConfig):

    def __init__(self):
        self.CLOUD_SDK_AK = None
        self.CLOUD_SDK_SK = None
        self.CREDENTIAL = None
        self.CLIENT = None

    def get_credential(self, ak, sk):
        """
            初始化认证信息
        :param ak:华为云账号Access Key。
        :param sk:华为云账号Secret Access Key 。
        :return:返回初始化信息
        """
        return BasicCredentials(ak, sk)

    def set_config(self, ak, sk):
        """
            初始化配置
        :param sk:
        :param ak:
        :return:
        """
        if ak is not None and sk is not None:
            self.CLOUD_SDK_AK = ak
            self.CLOUD_SDK_SK = sk
        else:
            raise BaseException('ak和sk参数有误！')
        self.CREDENTIAL = self.get_credential(ak, sk)
        if self.CREDENTIAL is None:
            raise BaseException('初始化认证信息有误！')
        self.CLIENT = OcrClient.new_builder(). \
            with_credentials(self.CREDENTIAL). \
            with_region(OcrRegion.CN_NORTH_4).build()
        if self.CLIENT is None:
            raise BaseException('初始话client有误！')

    def HouseholdRegister(self, file_base64=None, file_url=None):
        """
        发送户口本请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeHouseholdRegisterRequest()
            if file_base64 is not None:
                request.body = HouseholdRegisterRequestBody(
                    image=file_base64
                )
            else:
                request.body = HouseholdRegisterRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_household_register(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def SmartDocumentRecognizer(self, file_base64=None, file_url=None):
        """
        发送智能文档识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeSmartDocumentRecognizerRequest()
            if file_base64 is not None:
                request.body = SmartDocumentRecognizerRequestBody(
                    data=file_base64
                )
            else:
                request.body = SmartDocumentRecognizerRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_smart_document_recognizer(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def BankReceipt(self, file_base64=None, file_url=None):
        """
        发送智能文档识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeBankReceiptRequest()
            if file_base64 is not None:
                request.body = BankReceiptRequestBody(
                    data=file_base64
                )
            else:
                request.body = BankReceiptRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_bank_receipt(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def Seal(self, file_base64=None, file_url=None):
        """
        印章识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeSealRequest()
            if file_base64 is not None:
                request.body = SealRequestBody(
                    image=file_base64
                )
            else:
                request.body = SealRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_seal(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def IdCard(self, file_base64=None, file_url=None):
        """
        身份证识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeIdCardRequest()
            if file_base64 is not None:
                request.body = IdCardRequestBody(
                    data=file_base64
                )
            else:
                request.body = IdCardRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_id_card(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def VehicleLicense(self, file_base64=None, file_url=None):
        """
        行驶证识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeVehicleLicenseRequest()
            if file_base64 is not None:
                request.body = VehicleLicenseRequestBody(
                    image=file_base64
                )
            else:
                request.body = VehicleLicenseRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_vehicle_license(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def DriverLicense(self, file_base64=None, file_url=None):
        """
        驾驶证识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeDriverLicenseRequest()
            if file_base64 is not None:
                request.body = DriverLicenseRequestBody(
                    image=file_base64
                )
            else:
                request.body = DriverLicenseRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_driver_license(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def Passport(self, file_base64=None, file_url=None):
        """
        护照识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizePassportRequest()
            if file_base64 is not None:
                request.body = PassportRequestBody(
                    image=file_base64
                )
            else:
                request.body = PassportRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_passport(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def Bankcard(self, file_base64=None, file_url=None):
        """
        银行卡识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeBankcardRequest()
            if file_base64 is not None:
                request.body = BankcardRequestBody(
                    image=file_base64
                )
            else:
                request.body = BankcardRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_bankcard(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def BusinessLicense(self, file_base64=None, file_url=None):
        """
        营业执照识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeBusinessLicenseRequest()
            if file_base64 is not None:
                request.body = BusinessLicenseRequestBody(
                    image=file_base64
                )
            else:
                request.body = BusinessLicenseRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_business_license(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def TransportationLicense(self, file_base64=None, file_url=None):
        """
        道路运输证识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeTransportationLicenseRequest()
            if file_base64 is not None:
                request.body = TransportationLicenseRequestBody(
                    image=file_base64
                )
            else:
                request.body = TransportationLicenseRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_transportation_license(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def RealEstateCertificate(self, file_base64=None, file_url=None):
        """
        不动产证识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeRealEstateCertificateRequest()
            if file_base64 is not None:
                request.body = RealEstateCertificateRequestBody(
                    image=file_base64
                )
            else:
                request.body = RealEstateCertificateRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_real_estate_certificate(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def VehicleCertificate(self, file_base64=None, file_url=None):
        """
        车辆合格证识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeVehicleCertificateRequest()
            if file_base64 is not None:
                request.body = VehicleCertificateRequestBody(
                    image=file_base64
                )
            else:
                request.body = VehicleCertificateRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_vehicle_certificate(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def QualificationCertificate(self, file_base64=None, file_url=None):
        """
        道路运输从业资格证识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeQualificationCertificateRequest()
            if file_base64 is not None:
                request.body = QualificationCertificateRequestBody(
                    image=file_base64
                )
            else:
                request.body = QualificationCertificateRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_qualification_certificate(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def LicensePlate(self, file_base64=None, file_url=None):
        """
        车牌识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeLicensePlateRequest()
            if file_base64 is not None:
                request.body = LicensePlateRequestBody(
                    image=file_base64
                )
            else:
                request.body = LicensePlateRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_license_plate(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def BusinessCard(self, file_base64=None, file_url=None):
        """
        名片识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeBusinessCardRequest()
            if file_base64 is not None:
                request.body = BusinessCardRequestBody(
                    image=file_base64
                )
            else:
                request.body = BusinessCardRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_business_card(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def Vin(self, file_base64=None, file_url=None):
        """
        Vin识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeVinRequest()
            if file_base64 is not None:
                request.body = VinRequestBody(
                    image=file_base64
                )
            else:
                request.body = VinRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_vin(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def InvoiceVerification(self, file_base64=None, file_url=None):
        """
        增值税发票识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeVatInvoiceRequest()
            if file_base64 is not None:
                request.body = VatInvoiceRequestBody(
                    image=file_base64
                )
            else:
                request.body = VatInvoiceRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_vat_invoice(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def MvsInvoice(self, file_base64=None, file_url=None):
        """
        机动车销售发票识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeMvsInvoiceRequest()
            if file_base64 is not None:
                request.body = MvsInvoiceRequestBody(
                    image=file_base64
                )
            else:
                request.body = MvsInvoiceRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_mvs_invoice(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def TaxiInvoice(self, file_base64=None, file_url=None):
        """
        出租车发票识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeTaxiInvoiceRequest()
            if file_base64 is not None:
                request.body = TaxiInvoiceRequestBody(
                    image=file_base64
                )
            else:
                request.body = TaxiInvoiceRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_taxi_invoice(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def TrainTicket(self, file_base64=None, file_url=None):
        """
        火车票识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeTrainTicketRequest()
            if file_base64 is not None:
                request.body = TrainTicketRequestBody(
                    image=file_base64
                )
            else:
                request.body = TrainTicketRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_train_ticket(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def QuotaInvoice(self, file_base64=None, file_url=None):
        """
        定额发票识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeQuotaInvoiceRequest()
            if file_base64 is not None:
                request.body = QuotaInvoiceRequestBody(
                    image=file_base64
                )
            else:
                request.body = QuotaInvoiceRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_quota_invoice(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def TollInvoice(self, file_base64=None, file_url=None):
        """
        车辆通行费识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeTollInvoiceRequest()
            if file_base64 is not None:
                request.body = TollInvoiceRequestBody(
                    image=file_base64
                )
            else:
                request.body = TollInvoiceRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_toll_invoice(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def FlightItinerary(self, file_base64=None, file_url=None):
        """
        飞机行程单识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeFlightItineraryRequest()
            if file_base64 is not None:
                request.body = FlightItineraryRequestBody(
                    image=file_base64
                )
            else:
                request.body = FlightItineraryRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_flight_itinerary(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def WaybillElectronic(self, file_base64=None, file_url=None):
        """
        电子面单识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeWaybillElectronicRequest()
            if file_base64 is not None:
                request.body = WaybillElectronicRequestBody(
                    image=file_base64
                )
            else:
                request.body = WaybillElectronicRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_waybill_electronic(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def InsurancePolicy(self, file_base64=None, file_url=None):
        """
        保险单识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeInsurancePolicyRequest()
            if file_base64 is not None:
                request.body = InsurancePolicyRequestBody(
                    image=file_base64
                )
            else:
                request.body = InsurancePolicyRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_insurance_policy(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def FinancialStatement(self, file_base64=None, file_url=None):
        """
        财务报表识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeFinancialStatementRequest()
            if file_base64 is not None:
                request.body = FinancialStatementRequestBody(
                    image=file_base64
                )
            else:
                request.body = FinancialStatementRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_financial_statement(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def AcceptanceBill(self, file_base64=None, file_url=None):
        """
        承兑汇票识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeAcceptanceBillRequest()
            if file_base64 is not None:
                request.body = AcceptanceBillRequestBody(
                    image=file_base64
                )
            else:
                request.body = AcceptanceBillRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_acceptance_bill(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def ThailandIdcard(self, file_base64=None, file_url=None):
        """
        泰文身份证识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeThailandIdcardRequest()
            if file_base64 is not None:
                request.body = ThailandIdcardRequestBody(
                    image=file_base64
                )
            else:
                request.body = ThailandIdcardRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_thailand_idcard(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def ColombiaIdCard(self, file_base64=None, file_url=None):
        """
        哥伦比亚身份证识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeColombiaIdCardRequest()
            if file_base64 is not None:
                request.body = ColombiaIdCardRequestBody(
                    image=file_base64
                )
            else:
                request.body = ColombiaIdCardRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_colombia_id_card(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)

    def ThailandLicensePlate(self, file_base64=None, file_url=None):
        """
        泰文车牌识别请求
        :param file_base64: 文件base64编码
        :param file_url: 在线文件url
        :return:
        """
        try:
            request = RecognizeThailandLicensePlateRequest()
            if file_base64 is not None:
                request.body = ThailandLicensePlateRequestBody(
                    image=file_base64
                )
            else:
                request.body = ThailandLicensePlateRequestBody(
                    url=file_url
                )
            return self.CLIENT.recognize_thailand_license_plate(request)
        except exceptions.ClientRequestException as e:
            logger.error(f"request exception: {e}.")
            raise BaseException(e)