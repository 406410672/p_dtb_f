
# p_dtb_f

![fram-png](frame.png)

**框架内通信协议：** TCP。传输json格式的字符串，用UTF-8编码。
<br>**Master的IP、Port：** 通过BaseModule.Configloader的master_host与master_port变量获得
<br>**首次爬取URL:** https://www.taobao.com/markets/tbhome/market-list

**python目录结构**
> - Authorizes:登陆相关、验证码识别相关
> - DB:数据库处理相关
> - Master：
> - Crawler：
> - BaseModule：
> - Socket：

------

# Master Crawler交互协议
> * 字段默认都是必须传的
> * 注册后，每次request都要带上client_id
> * 利用结束符'\0'标记着传输完毕

### 1.注册，首次启动需要注册，并获取clientId
##### 请求格式:
```python
{
    'request_type' : 'register',
    'client_name'：'',
    'request_time'：    #时间戳的形式
}
```
##### 返回格式:
```python
{
    'client_id' : '',
    'server_status'：''
}
```

### 2.HEARTBEAT心跳检测（每30秒上传一次）
##### 请求格式:
```python
{
    'request_type' : 'heartbeat',
    'client_id'：'',
    'request_time'：    #时间戳的形式
}
```
##### 返回格式:
```python
{
    'server_status'：''
}
```
##### 有报错则返回
```python
{
    'error' : [错误类型]
    'server_status' :
}
```
**错误类型:**
> * err_not_found：服务器端未发现该client(需要重新注册)



### **3.获取任务**
##### 请求格式:
```python
{
    'request_type' : 'application_tasks',
    'client_id'：'',
    'request_time'：    #时间戳的形式
    'task_name' : ''  #可选填，可指定爬取的任务
}
```
##### 返回格式:
```python
{
    'task_items' ： [获取到的任务格式],  #在下面  如果没有任务，则数组大小为0
    'task_nums' : 100, #返回的任务个数   如果没有任务，则为0
}
```
###### 获取到的任务格式：
```python
{
    "type": "GET",
    "task_name": "淘宝商品信息获取",
    "domain" : "www.taobao.com",
    "headers" : "",
    "parse_rule" : [{
      "type" : "xpath",
      "priority" : 100 ,
      "pattern" : "./li/div[@class=\"category-items\"]/a[@class=\"category-name\"]"
      "content" : {"category_name":"./text()","category_url":"./@href"}
    } ,{
      "type" : "json",
      "priority" : 200 ,
      "parttern" : "items.price"
    } ,{
      "type" : "regular",
      "priority" : 300 ,
      "parttern" : "g_page_config = ({.*})"
    },{
      "type" : "module",
      "module_name" : "taobao_category_parse",
      "priority" : 1
    }
    ],
    "storage_rule":{
      "type" : "task"
      "mongodb":"taobao.category_info"
    }
}

```
----

# 任务队列模块
##### 任务存储数据结构
```python
{
    "type": "GET",
    "task_name": "淘宝商品分类获取",
    "domain" : "www.taobao.com",
    "headers" : "",
    "parse_rule" : [{
      "type" : "xpath",
      "priority" : 100 ,
      "pattern" : "./li/div[@class=\"category-items\"]/a[@class=\"category-name\"]"
      "content" : {"category_name":"./text()","category_url":"./@href"}
    } ,{
      "type" : "json",
      "priority" : 200 ,
      "parttern" : "items.price"
    } ,{
      "type" : "regular",
      "priority" : 300 ,
      "parttern" : "g_page_config = ({.*})"
    },{
      "type" : "module",
      "module_name" : "taobao_category_parse",
      "priority" : 1
    }
    ],
    "storage_rule":{
      "type" : "task",
      "item" : {
            "task_name" : "淘宝商品二级分类获取",
            "mongodb":"taobao.category_info"
      }
    }
}
```

