# DB API

엔지니어가 편리하게 데이터를 업로드하고 관리할 수 있는 인터페이스와
클라이언트가 데이터를 처리할 수 있는 REST API 제공.

제작자: 김한울(hanwool95@snu.ac.kr)

Django, Rest framework, MySQL


<br>

## Controller
#### DB 관리 인터페이스

HOST/controller

upload: 파일을 업로드하여 서버 static folder에 등록.<br>
insert file: 업로드한 static file를 지정하여 DB(manager/models)에 insert.<br>
event 제작: 현재 업로드한 모델을 기준으로 Event Table 작성.



## Manager
DB 관리 REST API<br><br>
<b>HOST/manager/<db_name: str></b><br>
target db 전체 정보 GET POST

<br><br>

<b>HOST/manager/<db_name: str>/<case_number: int></b><br>
target db의 특정 Case에 대해서 GET POST DELETE

<br><br>

<b>HOST/manager/<db_name: str>/id/<id_number: int></b><br>
target db의 특정 Index에 대해서 GET PATCH DELETE



