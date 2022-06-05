# DB 관리 시스템

### 소견서 자동요약 프로젝트 DB 관리 및 API 처리 서버.

참여자: 김한울(hanwool95@snu.ac.kr)

Django, MySQL

## Module

#### 1. db_manager: sql문으로 MySQL을 조작하는 object<br>
#### 2. event_manager: DB를 분석하여 Event와 Important를 분류하여 새로운 Table 제작하는 objct<br>
#### 3. dbApi: "db_manager"와 "event_manager"를 서버에 적용(Django). 엔지니어가 DB관리할 수 있는 인터페이스, client에 DB 정보 전달하는 RestAPI.
<br>

## Execute example
##### a_make_orient_table.py: DB table 생성 (init)
##### b_Data_Lodader.py: csv파일을 table에 insert
##### c_Get_Data_by_case.py: 원하는 Case number의 통합 table 제작
##### d_output_event.py: 원하는 Case number의 통합 table 기준 event 분류
##### e_add_important.py: event 기준 important 판별
##### total_process.py: 모든 case number의 c~e 과정 진행.