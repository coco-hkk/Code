"""json 格式解析

json.dumps() 对数据进行编码
json.loads() 对数据进行解码

作者：coco-hkk
日期：2022年9月9日
"""
import json

def dict_to_json():
    """由字典生成 json 格式文件"""
    data = {
        'id': 1,
        'name': "foo",
        'score': {"math": 80, "english": 82.5}
    }

    json_str = json.dumps(data)
    print("dict: " + repr(data))
    print("json: " + json_str)

def json_to_dict(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    return data

if __name__ == '__main__':
    dict_to_json()
    json_data = json_to_dict('test.json')
    print(json_data)