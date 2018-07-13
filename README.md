# python-whatweb
> [WhatWeb](https://github.com/urbanadventurer/WhatWeb)的python封装,现只支持python>=3.4.

## install
`python3 setup.py`

## usage
### 扫描结果
扫描结果为whatweb的json输出格式进行json.loads()的结果. 

### 使用示例
```python
import asyncio
import whatweb

async def main():
    scanner = whatweb.WhatWeb()
    result = await scanner.scan("https://csdn.net")
    print(result) 

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

```

### whatweb的执行程序搜索路径
默认的whatweb搜索路径为`whatweb, /usr/bin/whatweb, /usr/local/bin/whatweb, /opt/local/bin/whatweb)`, 可以自己指定,通过whatweb.WhatWeb的第一个参数, 例如:
`scanner = whatweb.WhatWeb(("mypath/whatweb", ))`
