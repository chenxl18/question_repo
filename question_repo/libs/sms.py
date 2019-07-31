import urllib.request
import urllib
import json
import logging

logger = logging.getLogger('sms')


def send_sms(mobile, captcha):
    # flag用于标记发送短信是否成功
    flag = True
    # 这个是短信API地址
    url = 'https://open.ucpaas.com/ol/sms/sendsms'
    # 准备一下头,声明body的格式
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }
    # 还有我们准备用Post传的值，这里值用字典的形式
    values = {
        "sid": "d82695a5d130ab2621ad01556be34a6c",
        "token": "900d249a329a3543668c3667ba1995fa",
        "appid": "eeea6de93f154f56ba5ab948a0877d06",
        "templateid": "489089",
        "param": str(captcha),
        "mobile": mobile,
    }

    try:
        # 将字典格式化成bytes格式
        data = json.dumps(values).encode('utf-8')
        logger.info("即将发送短信: {}".format(data))
        # 创建一个request,放入我们的地址、数据、头
        request = urllib.request.Request(url, data, headers)
        html = urllib.request.urlopen(request).read().decode('utf-8')
        # html = '{"code":"000000","count":"1","create_date":"2018-07-23 13:34:06","mobile":"15811564298","msg":"OK","smsid":"852579cbb829c08c917f162b267efce6","uid":""}'
        code = json.loads(html)["code"]
        if code == "000000":
            logger.info("短信发送成功：{}".format(html))
            flag = True
        else:
            logger.info("短信发送失败：{}".format(html))
            flag = False
    except Exception as ex:
        logger.info("出错了,错误原因：{}".format(ex))
        flag = False
    return flag


if __name__ == "__main__":
    # 测试短信接口是否是管用
    send_sms("17873550094", "123456")