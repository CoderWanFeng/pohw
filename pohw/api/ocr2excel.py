from pofile import get_files, mkdir
from pathlib import Path
from poprogress import simple_progress
from pohw.api.ocr import *
from loguru import logger

import pandas as pd
import json


def HouseholdRegister2Excel(input_path=None, output_path=None, output_excel='HouseholdRegister2Excel.xlsx',
                            file_url=None, ak=None, sk=None):
    """
    户口本识别
    :param input_path: 户口本存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为HouseholdRegister2Excel.xlsx
    :param file_url: 户口本在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = HouseholdRegister(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            for result in results:
                contents = result.get('content')
                if contents is not None:
                    res_df.append(contents)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def BankReceipt2excel(input_path=None, output_path=None, output_excel='BankReceipt2excel.xlsx',
                      file_url=None, ak=None, sk=None):
    """
    户口本识别
    :param input_path: 银行回单存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为BankReceipt2excel.xlsx
    :param file_url: 银行回单在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = BankReceipt(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')

            bank_receipt_list = results.get('bank_receipt_list')
            if bank_receipt_list is None:
                logger.error("无识别到数据!")
            else:
                for list_item in bank_receipt_list:
                    kv_pair_list = list_item.get('kv_pair_list')
                    row_res = {}
                    for item in kv_pair_list:
                        row_res[item['key']] = item['value']
                    res_df.append(row_res)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def Seal2excel(input_path=None, output_path=None, output_excel='Seal2excel.xlsx',
               file_url=None, ak=None, sk=None):
    """
    印章识别
    :param input_path: 印章存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为Seal2excel.xlsx
    :param file_url: 印章在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = Seal(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')

            seal_list = results.get('seal_list')
            if seal_list is None or len(seal_list) == 0:
                logger.error("无识别到数据!")
            else:
                for seal in seal_list:
                    words_block_list = seal.get('words_block_list')
                    words_list = [obj.words for obj in words_block_list]
                    my_dict = {f"words{index}": value for index, value in enumerate(words_list)}
                    my_dict['type'] = seal.get('type')
                    res_df.append(my_dict)

    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def IdCard2Excel(input_path=None, output_path=None, output_excel='IdCard2Excel.xlsx',
                 file_url=None, ak=None, sk=None):
    """
    身份证识别
    :param input_path: 身份证存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为IdCard2Excel.xlsx
    :param file_url: 身份证在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = IdCard(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def VehicleLicense2Excel(input_path=None, output_path=None, output_excel='VehicleLicense2Excel.xlsx',
                         file_url=None, ak=None, sk=None):
    """
    行驶证识别
    :param input_path: 行驶证存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为VehicleLicense2Excel.xlsx
    :param file_url: 行驶证在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = VehicleLicense(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def DriverLicense2Excel(input_path=None, output_path=None, output_excel='DriverLicense2Excel.xlsx',
                        file_url=None, ak=None, sk=None):
    """
    驾驶证识别
    :param input_path: 驾驶证存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为DriverLicense2Excel.xlsx
    :param file_url: 驾驶证在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = DriverLicense(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def Passport2Excel(input_path=None, output_path=None, output_excel='Passport2Excel.xlsx',
                   file_url=None, ak=None, sk=None):
    """
    护照识别
    :param input_path: 护照存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为Passport2Excel.xlsx
    :param file_url: 护照在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = Passport(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def Bankcard2Excel(input_path=None, output_path=None, output_excel='Bankcard2Excel.xlsx',
                   file_url=None, ak=None, sk=None):
    """
    银行卡识别
    :param input_path: 银行卡存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为Bankcard2Excel.xlsx
    :param file_url: 银行卡在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = Bankcard(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def BusinessLicense2Excel(input_path=None, output_path=None, output_excel='BusinessLicense2Excel.xlsx',
                          file_url=None, ak=None, sk=None):
    """
    营业执照识别
    :param input_path: 营业执照存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为BusinessLicense2Excel.xlsx
    :param file_url: 营业执照在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = BusinessLicense(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def TransportationLicense2Excel(input_path=None, output_path=None, output_excel='TransportationLicense2Excel.xlsx',
                                file_url=None, ak=None, sk=None):
    """
    道路运输证识别
    :param input_path: 道路运输证存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为TransportationLicense2Excel.xlsx
    :param file_url: 道路运输证在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = TransportationLicense(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def RealEstateCertificate2Excel(input_path=None, output_path=None, output_excel='RealEstateCertificate2Excel.xlsx',
                                file_url=None, ak=None, sk=None):
    """
    不动产证识别
    :param input_path: 不动产证存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为RealEstateCertificate2Excel.xlsx
    :param file_url: 不动产证在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = RealEstateCertificate(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def VehicleCertificate2Excel(input_path=None, output_path=None, output_excel='VehicleCertificate2Excel.xlsx',
                             file_url=None, ak=None, sk=None):
    """
    车辆合格证识别
    :param input_path: 车辆合格证存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为VehicleCertificate2Excel.xlsx
    :param file_url: 车辆合格证在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = VehicleCertificate(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def QualificationCertificate2Excel(input_path=None, output_path=None,
                                   output_excel='QualificationCertificate2Excel.xlsx',
                                   file_url=None, ak=None, sk=None):
    """
    道路运输从业资格证识别
    :param input_path: 道路运输从业资格证存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为QualificationCertificate2Excel.xlsx
    :param file_url: 道路运输从业资格证在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = QualificationCertificate(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def LicensePlate2Excel(input_path=None, output_path=None,
                       output_excel='LicensePlate2Excel.xlsx',
                       file_url=None, ak=None, sk=None):
    """
    车牌识别
    :param input_path: 车牌存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为LicensePlate2Excel.xlsx
    :param file_url: 车牌在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = LicensePlate(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def BusinessCard2Excel(input_path=None, output_path=None,
                       output_excel='BusinessCard2Excel.xlsx',
                       file_url=None, ak=None, sk=None):
    """
    名片识别
    :param input_path: 名片存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为BusinessCard2Excel.xlsx
    :param file_url: 名片在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = BusinessCard(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def Vin2Excel(input_path=None, output_path=None, output_excel='Vin2Excel.xlsx',
              file_url=None, ak=None, sk=None):
    """
    Vin识别
    :param input_path:  Vin存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为Vin2Excel.xlsx
    :param file_url: Vin在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = Vin(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def InvoiceVerification2Excel(input_path=None, output_path=None, output_excel='InvoiceVerification2Excel.xlsx',
                              file_url=None, ak=None, sk=None):
    """
    增值税发票识别
    :param input_path:  增值税发票存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为InvoiceVerification2Excel.xlsx
    :param file_url: 增值税发票在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = InvoiceVerification(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def MvsInvoice2Excel(input_path=None, output_path=None, output_excel='MvsInvoice2Excel.xlsx',
                     file_url=None, ak=None, sk=None):
    """
    机动车销售发票识别
    :param input_path:  机动车销售发票存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为MvsInvoice2Excel.xlsx
    :param file_url: 机动车销售发票在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = MvsInvoice(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def TaxiInvoice2Excel(input_path=None, output_path=None, output_excel='TaxiInvoice2Excel.xlsx',
                      file_url=None, ak=None, sk=None):
    """
    出租车发票识别
    :param input_path:  出租车发票存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为TaxiInvoice2Excel.xlsx
    :param file_url: 出租车发票在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = TaxiInvoice(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def TrainTicket2Excel(input_path=None, output_path=None, output_excel='TrainTicket2Excel.xlsx',
                      file_url=None, ak=None, sk=None):
    """
    火车票识别
    :param input_path:  火车票存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为TrainTicket2Excel.xlsx
    :param file_url: 火车票在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = TrainTicket(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def QuotaInvoice2Excel(input_path=None, output_path=None, output_excel='QuotaInvoice2Excel.xlsx',
                       file_url=None, ak=None, sk=None):
    """
    定额发票识别
    :param input_path:  定额发票存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为QuotaInvoice2Excel.xlsx
    :param file_url: 定额发票在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = QuotaInvoice(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def TollInvoice2Excel(input_path=None, output_path=None, output_excel='TollInvoice2Excel.xlsx',
                      file_url=None, ak=None, sk=None):
    """
    车辆通行费发票识别
    :param input_path:  车辆通行费发票存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为TollInvoice2Excel.xlsx
    :param file_url: 车辆通行费发票在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = TollInvoice(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def FlightItinerary2Excel(input_path=None, output_path=None, output_excel='FlightItinerary2Excel.xlsx',
                          file_url=None, ak=None, sk=None):
    """
    飞机行程单识别
    :param input_path:  飞机行程单存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为FlightItinerary2Excel.xlsx
    :param file_url: 飞机行程单在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = FlightItinerary(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def WaybillElectronic2Excel(input_path=None, output_path=None, output_excel='WaybillElectronic2Excel.xlsx',
                            file_url=None, ak=None, sk=None):
    """
    电子面单识别
    :param input_path:  电子面单存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为WaybillElectronic2Excel.xlsx
    :param file_url: 电子面单在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = WaybillElectronic(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)


def InsurancePolicy2Excel(input_path=None, output_path=None, output_excel='InsurancePolicy2Excel.xlsx',
                          file_url=None, ak=None, sk=None):
    """
    保险单识别
    :param input_path:  保险单存放位置
    :param output_path: 输出文件目录
    :param output_excel: 输出文件名，默认为InsurancePolicy2Excel.xlsx
    :param file_url: 保险单在线文件地址
    :param ak: 华为云账号Access Key
    :param sk: 华为云账号Secret Access Key
    :return:
    """
    if input_path is None and file_url is None:
        raise BaseException(f'参数异常,请检查后重新运行!')
    file_paths = [file_url] if input_path is None else get_files(input_path)
    if file_paths is None or len(file_paths) == 0:
        raise BaseException(f'未识别到有效文件,请检查后重新运行.')
    output_path = output_path or './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []
    try:
        for item in simple_progress(file_paths):
            api_res = InsurancePolicy(file_path=str(item), file_url=file_url, sk=sk, ak=ak)
            api_res_json = json.loads(str(api_res))
            results = api_res_json.get('result')
            if results is None:
                raise BaseException('调用接口异常！')
            if 'confidence' in results:
                del results['confidence']
            res_df.append(results)
    except Exception as e:
        logger.error(e)
    biz_def = pd.DataFrame(res_df)
    # 将结果数据框保存到Excel文件
    biz_def.to_excel(str(abs_output_excel), index=None)