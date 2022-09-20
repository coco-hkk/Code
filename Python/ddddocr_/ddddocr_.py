"""验证码识别，识别图片中的文字或数字

PIL 可在通过 pip install Pillow 安装

作者：coco-hkk
日期：2022年9月9日
"""
import os

from PIL import Image
from PIL import ImageEnhance
from PIL import ImageGrab
import ddddocr

def verify_code(img_file, location):
    """验证码识别

    Args:
        img_file: 图片位置
        location: 识别图片某个区域的坐标，左上角和右下角
    Return:
        返回识别内容 返回识别内容 返回识别内容 返回识别内容
    """
    img_path = os.path.dirname(img_file)

    img1 = Image.open(img_file)
    img1 = img1.convert("RGB")

    #使用 Image 的 crop 函数，从截图中再次截取我们需要的区域
    img2 = img1.crop(location)
    img2.save(img_path + "/verify1.jpg")

    img2 = Image.open(img_path + "/verify1.jpg")
    img3 = img2.convert('L')
    sharpness = ImageEnhance.Contrast(img3)  #对比度增强

    img4 = sharpness.enhance(3.0)      #3.0 为图像的饱和度
    img4.save(img_path + "/verify2.jpg")

    ocr = ddddocr.DdddOcr()
    with open(img_path + "/verify2.jpg", 'rb') as file:
        img_bytes = file.read()
        content = ocr.classification(img_bytes)

    return content

if __name__ == '__main__':
    jpg = './test.jpg'

    # 截全屏
    img = ImageGrab.grab()
    img.save(jpg)

    # 左上角坐标，右下角坐标
    # Chrome 浏览器可使用 Page Ruler 插件定位
    position = (0, 0, 200, 40)

    res = verify_code(jpg, position)
    print(res)
