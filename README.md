<!--Heading-->
# 탄소 중립을 위한 채식 식단 제공 서비스 "Carbon Diet"와 채식주의 경향에 따른 식품 자동분류 자연어처리 모델 구현
#### 2021 데이터청년캠퍼스 동국대학교 B반 떡잎방범대(1조) 프로젝트
<!--Text Attributes-->
![0004](https://user-images.githubusercontent.com/59340103/164633906-edffa788-70e0-4dea-8767-984716b77edf.jpg)

"Carbon Diet"는 탄소 중립을 위해 채식을 시작하는 이들에게 다양한 채식 식단 정보를 제공하고 사용자의 탄소기여도를 확인할 수 있도록 기획된 안드로이드 하이브리드앱입니다. 사용자는 자신이 도전하고자 하는 채식 수준과 채식빈도를 설정하고 앱으로부터 해당 설정에 맞춰 일주일 단위로 채식 메뉴들을 제공받습니다. 그리고 해당 서비스의 기반을 위해 채식주의 경향에 따른 식품 자동분류 모델 구현하였습니다.
<br><br><br>
해당 프로젝트는 파일 목록 메인에 있는 **'carbon_diet_app.apk'** 파일을 통해 안드로이드 휴대폰에 설치하여 결과물을 바로 확인하실 수 있습니다.
(2022년 4월 22일 기준으로 AWS의 사용기한이 만료되어 서비스의 사용이 어렵습니다😂)


<br><br>
<!--Bullet list-->
[파일 목록 구조]
<br>
**carbon_diet** : django project 디폴트 앱 <br>
**carbon_diet/DB_table** : 데이터베이스에 쓰인 기초 데이터들에 대한 csv 파일. 테이블 별로 파일 구분. <br>
**carbon_diet/module** : 
* 레시피에 대한 채식수준 자동 분류 모델(VeganRecipeClassification_DeepLearning.ipynb) 
* 데이터베이스 활용 로직(dbmodule.py) 
* 레시피에 대한 탄소배출량 계산 로직(pymodule.py) 
* 레시피 웹크롤링 로직(recipe_crawling.ipynb) 
* 자동 식단 추천 로직(revised_reciperecommend.py)
<br><br>
<!--Text Attributes-->
**carbon_diet_service** : django project 구현 앱<br>
**carbon_diet_service/templates** : html 페이지
<br><br>
**static** : css, images, javascript 정적파일
<br><br><br>
<!--Heading-->
## 시스템 구성도
<!--Text attributes-->
- **Server** : AWS EC2
- **Framework** : Django
- **Database** : MySQL
- **Web Server** : Apache
- **App IDE** : Android studio
<br><br>
![2021-08-29 (14)](https://user-images.githubusercontent.com/59340103/131227740-6d69f2ed-15ce-4b74-bce5-dd237a3c094b.png)


<br><br><br>
<!--Heading-->
## 핵심기능
![0005](https://user-images.githubusercontent.com/59340103/164637188-3a3c1832-a879-4467-9389-a938fda399b8.jpg)
![0006](https://user-images.githubusercontent.com/59340103/164637314-620ca713-2bee-44b8-a241-d6d5024301ff.jpg)
![0007](https://user-images.githubusercontent.com/59340103/164637425-a92f6fbb-45ef-4e14-ae5f-96136d719804.jpg)



<br><br><br>
<!--Heading-->
## 프로젝트 배경 및 해결방안
<!--Text attributes-->
![0001](https://user-images.githubusercontent.com/59340103/164643770-3c59ad5d-3505-468b-acc5-70a30a26470e.jpg)
![0002](https://user-images.githubusercontent.com/59340103/164643795-dc9b9658-b888-47e4-8fc0-0a2fe3f1351e.jpg)
![0003](https://user-images.githubusercontent.com/59340103/164643814-beea0153-764b-40e4-b413-63be6b13a984.jpg)

- **Web Crawling** : Python
- **Deep Learning** : BERT, PyTorch (계속적으로 추가되는 레시피 데이터에 대해 채식수준을 자동으로 분류할 수 있도록 모델 구현)
- **Frontend** : HTML5, CSS, JavaScript


<!--Text attributes-->
<br><br><br>
[채식주의 종류]
<!--Table-->
|채식주의 종류 | 설명 |
|--|--|
|비건| 채소까지 허용. 완전한 채식주의자로서 동물을 희생시키는 꿀, 모피, 뿔도 거부.|
|락토| 채소, 유제품까지 허용. |
|락토 오보| 채소, 유제품, 달걀까지 허용. 가장 많은 수의 채식주의자들이 이 단계에 속함.|
|페스코| 채소, 유제품, 달걀, 해산물까지 허용.|
|폴로| 채소, 유제품, 달걀, 해산물, 가금류(닭, 오리 등)까지 허용. |
|플렉시테리언| 기본적으로 비건이지만 경우에 따라 육류 섭취를 허용하는 유연한 채식주의자.|

<!--Text attributes-->
<br><br><br>
![2021-08-29 (13)](https://user-images.githubusercontent.com/59340103/131227743-d07a2fa3-70ee-472d-88cd-8e3dd4f0d8ea.png)


