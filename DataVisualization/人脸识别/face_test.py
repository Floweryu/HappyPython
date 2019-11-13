# -*- coding:utf-8 -*-
# _author_='Zhang JunFeng'
import base64
import json
import requests


def img(img1, img2):
    with open(img1, "rb") as f:
        pic1 = base64.b64encode(f.read())
    with open(img2, "rb") as f:
        pic2 = base64.b64encode(f.read())
    return json.dumps([
        {"image": str(pic1, "utf-8"), "image_type": "BASE64",
         "face_type": "LIVE", "quality_control": "LOW"},
        {"image": str(pic2, "utf-8"), "image_type": "BASE64",
         "face_type": "IDCARD", "quality_control": "LOW"},
    ])


def pinjie_api():
    get_token = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=" \
                "lVfov6E1oaWZR9f4qIhd9Hjy&client_secret=Gubrc6RnMTdA3Eb8WumHIGrz4vHgCTdy"
    pinjie_url = "https://aip.baidubce.com/rest/2.0/face/v3/match?access_token="
    response = requests.get(get_token)
    url = pinjie_url + eval(response.text)['access_token']
    return url


def request_result(img1, img2):
    params = img(img1, img2)
    api = pinjie_api()

    response = requests.post(api, params)
    score = eval(response.text)['result']['score']
    if score > 80:
        print("图片相识度 ：" + str(score) + "，是同一个人")
    else:
        print("图片相识度 ：" + str(score) + "，不是同一个人")


request_result("e.png", "f.png")
