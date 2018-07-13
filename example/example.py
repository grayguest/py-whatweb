#-*- coding:utf-8 -*-
'''
Created on 2018-07-13

@author: ranyixu
'''

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
