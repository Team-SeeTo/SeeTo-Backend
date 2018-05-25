# 스키마 정의

# TODO
## TODO 받아오기
```
query{
    getTODO(token:<token>!, date:<Datetime>!, type:<ENUM>, sortby:<ENUM>){
        title
        milestones{
            index
            name
            complete
            day
        }
        expiration
        type
        message{
            success
            message
        }
    }
}
```
example response
```json
{
    "getTODO": [{
        "title":"title",
        "milestones":[
            {
                "index": 1,
                "name": "milestone",
                "complete": true,
                "day": 0
            },
            {
                "index": 2,
                "name": "milestone2",
                "complete": false,
                "day": 0
            }
        ],
        "expiration":"2018-05-25",
        "type":"standard",
        "message":{
            "success": true,
            "message": "query successfull"
        }
    },
    {
        "title":"title1",
        "milestones":[
            {
                "index": 1,
                "name": "milestone",
                "complete": true,
                "day":1
            },
            {
                "index": 2,
                "name": "milestone2",
                "complete": false,
                "day":2
            }
        ],
        "expiration":"2018-05-26",
        "type":"3-day",
        "message":{
            "success": true,
            "message": "query successfull"
        }
    }]
}
```
## TODO 마일스톤 체크하기
```
mutation {
    checkMilestone(token:<string>!, todo_id:<string>!, milestone_id:<int>!){
        reward
        message{
            success
            message
        }
    }
}
```
example response
```json
"checkMilestone":{
    "reward": 20,
    "message":{
        "success": true,
        "message": "mutate succesfull"
    }
}
```
## milestone 삭제 -> delete all로 TODO 삭제
```
mutation {
    deleteMilestone(token:<string>!, todo_id:<string>!, milestone_id:<int>!, delete_all:<bool>){
        reward
        message{
            success
            message
        }
    }
}
```
example response
```json
"deleteMilestone":{
    "reward": -100,
    "message":{
        "success": true,
        "message": "mutate succesfull"
    }
}
```
