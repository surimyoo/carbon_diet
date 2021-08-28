<!--Heading-->
# 탄소 중립을 위한 채식 식단 제공 서비스 "Carbon Diet"
#### 2021 데이터청년캠퍼스 B반 떡잎방범대(1조) 프로젝트
<!--Text Attributes-->
"Carbon Diet"는 탄소 중립을 위해 채식을 시작하는 이들에게 다양한 채식 식단 정보를 제공하고 사용자의 탄소기여도를 확인할 수 있도록 기획된 안드로이드 하이브리드앱입니다. 사용자는 자신이 도전하고자 하는 채식 수준과 채식빈도를 설정하고 앱으로부터 해당 설정에 맞춰 일주일 단위로 채식 메뉴들을 제공받습니다.
<br><br>
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
<!--Table-->
|main funtion|description|
|:--:|:--:|
|사용자 질의| <img src="https://user-images.githubusercontent.com/59340103/131228507-c1a205fc-4e69-4383-8d12-b511b676c1f1.gif" width="250"><br><br>채식수준을 어느 식품군까지 허용할 것인지, 일주일에 몇 번 하루 몇 끼 채식을 실천할 것인지 설정<br><br>|
|주간 식단 제공|<img src="https://user-images.githubusercontent.com/59340103/131228510-2eef151e-81fc-4db3-a958-e2e6809ba63b.gif" width="250"><br><br>사용자 설정에 따른 주간 식단 제공. 실제로 실천한 식사인지 체크할 수 있음<br><br>|
|탄소배출 통계 시각화|<img src="https://user-images.githubusercontent.com/59340103/131228515-b1777367-24cd-4e94-9107-252acf0e3a4a.gif" width="250"><br><br>실제로 실천했다고 체크된 식사들에 대한 탄소배출량 데이터로 다양한 통계 자료 제공<br><br>|


<br><br><br>
<!--Heading-->
## 적용 기법 및 기술
<!--Text attributes-->
- **Web Crawling** : Python
- **Deep Learning** : BERT, PyTorch (계속적으로 추가되는 레시피 데이터에 대해 채식수준을 자동으로 분류할 수 있도록 모델 구현)
- **Frontend** : HTML5, CSS, JavaScript
<br><br>
![2021-08-29 (13)](https://user-images.githubusercontent.com/59340103/131227743-d07a2fa3-70ee-472d-88cd-8e3dd4f0d8ea.png)


<br><br><br>
<!--Heading-->
## 사용 데이터 목록
<!--Text attributes-->
![2021-08-29 (16)](https://user-images.githubusercontent.com/59340103/131227815-6c71fa96-05ad-409c-a85d-52731497e2d4.png)

