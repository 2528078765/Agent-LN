# 1.加载到环境变量
from dotenv import load_dotenv
# 2.定义工具
from langchain.tools import tool
# 3.创建Agent
from langchain.agents import create_agent

import datetime

# 1.加载环境变量
load_dotenv()

# 2.定义工具
@tool
def getWeather(location:str) -> str:
    """获取天气信息
    Args:
        location: 城市名
    Returns:
        str: 天气信息
    """
    return f"{location}的天气晴朗，温度25度。"

import requests

@tool
def getTime() -> str:
    '''
    获取当前时间
    Returns:
        str: 当前时间
    '''
    return datetime.datetime.now()

@tool
def getNews(type:str='科技',page:str='5',page_size:str='5',is_filter:str='1') -> str:
    '''
    获取新闻信息
    Args:
        type: 新闻类型，默认为AI
        page: 页数，默认为5
        page_size: 获取几条新闻，默认为5
        is_filter: 是否过滤重复数据，默认1过滤，0不过滤
    Returns:
        str: 新闻信息
    '''

    # 基本参数配置
    apiUrl = 'http://v.juhe.cn/toutiao/index'  # 接口请求URL
    apiKey = '7d2e1ea630864c565d9c2fae77490714'  # 在个人中心->我的数据,接口名称上方查看

    # 接口请求入参配置
    requestParams = {
        'key': apiKey,
        'type': type,
        'page': page,
        'page_size': page_size,
        'is_filter': is_filter,
    }

    # 发起接口网络请求
    response = requests.get(apiUrl, params=requestParams)

    # 解析响应结果
    if response.status_code == 200:
        responseResult = response.json()
        # 网络请求成功。可依据业务逻辑和接口文档说明自行处理。
        print(responseResult)
    else:
        # 网络异常等因素，解析结果异常。可依据业务逻辑自行处理。
        print('请求异常')


# 3.创建Agent
agent = create_agent(
    "deepseek-chat",
    tools=[getWeather, getNews, getTime]
)

# 4.调用Agent
print("正在调用...")
response = agent.invoke({
    "messages":[
        {"role":"user","content":"告诉我葫芦岛的天气怎么样？"}
    ]
})

for message in response['messages']:
    print(message.model_dump_json(indent=4))
    print("————————————————————————————————————————————————")

'''
{
    "content": "告诉我葫芦岛的天气怎么样？",
    "additional_kwargs": {},
    "response_metadata": {},
    "type": "human",
    "name": null,
    "id": "41bc21e9-b6c4-44cd-9d10-ac46c9193f17"
}
————————————————————————————————————————————————
{
    "content": "我来帮您查询葫芦岛的天气情况。",
    "additional_kwargs": {
        "refusal": null
    },
    "response_metadata": {
        "token_usage": {
            "completion_tokens": 52,
            "prompt_tokens": 511,
            "total_tokens": 563,
            "completion_tokens_details": null,
            "prompt_tokens_details": {
                "audio_tokens": null,
                "cached_tokens": 448
            },
            "prompt_cache_hit_tokens": 448,
            "prompt_cache_miss_tokens": 63
        },
        "model_provider": "deepseek",
        "model_name": "deepseek-chat",
        "system_fingerprint": "fp_eaab8d114b_prod0820_fp8_kvcache_new_kvcache",   
        "id": "86f56f39-ddd4-4135-aa4c-5c8b502f43d6",
        "finish_reason": "tool_calls",
        "logprobs": null
    },
    "type": "ai",
    "name": null,
    "id": "lc_run--019d47e1-239e-7c73-b3f9-9272ccbc9367-0",
    "tool_calls": [
        {
            "name": "getWeather",
            "args": {
                "location": "葫芦岛"
            },
            "id": "call_00_RSmMXgn3VflaA2RowHOVmQKB",
            "type": "tool_call"
        }
    ],
    "invalid_tool_calls": [],
    "usage_metadata": {
        "input_tokens": 511,
        "output_tokens": 52,
        "total_tokens": 563,
        "input_token_details": {
            "cache_read": 448
        },
        "output_token_details": {}
    }
}
————————————————————————————————————————————————
{
    "content": "葫芦岛的天气晴朗，温度25度。",
    "additional_kwargs": {},
    "response_metadata": {},
    "type": "tool",
    "name": "getWeather",
    "id": "fc216c7c-6d57-43e6-b48a-3f9d21a1883e",
    "tool_call_id": "call_00_RSmMXgn3VflaA2RowHOVmQKB",
    "artifact": null,
    "status": "success"
}
————————————————————————————————————————————————
{
    "content": "根据查询结果，葫芦岛目前的天气情况是：\n- **天气状况**：晴朗\n- **温度**：25度\n\n这是一个相当不错的天气，温度适中，适合外出活动。如果您计划去葫芦岛旅游或者有户外活动安排，这样的天气条件应该会很舒适。",
    "additional_kwargs": {
        "refusal": null
    },
    "response_metadata": {
        "token_usage": {
            "completion_tokens": 58,
            "prompt_tokens": 588,
            "total_tokens": 646,
            "completion_tokens_details": null,
            "prompt_tokens_details": {
                "audio_tokens": null,
                "cached_tokens": 512
            },
            "prompt_cache_hit_tokens": 512,
            "prompt_cache_miss_tokens": 76
        },
        "model_provider": "deepseek",
        "model_name": "deepseek-chat",
        "system_fingerprint": "fp_eaab8d114b_prod0820_fp8_kvcache_new_kvcache",   
        "id": "d4d84a27-124e-42cd-a92d-c181820139ab",
        "finish_reason": "stop",
        "logprobs": null
    },
    "type": "ai",
    "name": null,
    "id": "lc_run--019d47e1-2f59-7463-a578-b1e6f1a9ddc3-0",
    "tool_calls": [],
    "invalid_tool_calls": [],
    "usage_metadata": {
        "input_tokens": 588,
        "output_tokens": 58,
        "total_tokens": 646,
        "input_token_details": {
            "cache_read": 512
        },
        "output_token_details": {}
    }
}
————————————————————————————————————————————————

'''