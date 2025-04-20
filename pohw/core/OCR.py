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
        self.CLIENT = OcrClient.new_builder(OcrClient).\
            with_credentials(self.CREDENTIAL).\
            with_region(OcrRegion.CN_NORTH_4).build()
        if self.CLIENT is None:
            raise BaseException('初始话client有误！')

    def HouseholdRegister(self, file_base64=None, file_url=None):
        """
            获取户口本的信息
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

