<div align = center>

# 올라갈지도
GPS 기반의 오름 방문 기록 사이트 

https://github.com/wvssm/Jeju_Oreum_Stamp_Project/assets/52875244/c794feac-e98f-498d-8b05-782f4351563d

</div>

# 프로젝트 소개
> **제주도의 흩어진 오름을 모두 방문하고 싶지 않나요?**
>
> **오름에 오른 추억을 색다르게 남기고 싶지 않나요?**
> 
> **현재 내가 방문한 오름이 궁금하지 않나요?**
> 

<br />

GPS 기능을 통해, 현재 내 주변의 오름을 파악해보세요!

내 주변의 오름을 하나씩 방문하고 스탬프를 찍어보세요. 스탬프를 찍다보면 중독될지도?

방문한 오름과 날짜를 한 눈에 확인해보세요.

### **방문 기록을 편하게❗️ 나의 추억을 영원하게❗️ 올라갈지도🌋가 도와드릴게요.**
<br><br>

# 프로젝트 기능
### ✍️GPS 기반의 오름 방문 기록
- GPS 기능을 통해 오름에 도착하면 스탬프를 찍을 수 있습니다.
- 스탬프를 찍으면, 해당 오름의 정보를 웹페이지에 나타내고, 오름 이름과 방문 날짜가 기록됩니다.
- 방문한 오름을 지도를 통해 시각적으로 확인할 수 있습니다.
<br><br>

# 기술 스택
### 개발 환경
<img src="https://img.shields.io/badge/visualstudiocode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white">

### 사용 언어 및 기술
<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
<!--<img src="https://img.shields.io/badge/postgresql-4169E1?style=for-the-badge&logo=postgresql&logoColor=white">-->
<br>

# 버전 정보
- 올라갈지도 1.0 - update: 2024.03.01
- 올라갈지도 1.1 - update: 2024.03.11 
  - 로그인, 회원가입, 스탬프 저장 기능 추가
<br><br>

# 참가 및 역할 분담
|[강수민](https://github.com/wvssm)|[정혜영](https://github.com/jungdoing)|[심혜민](https://github.com/hyemdol)|[이은진](https://github.com/JinJinJinJIn2)|
|:---:|:---:|:---:|:---:|
|<img src="https://github.com/wvssm/Jeju_Oreum_Stamp_Project/blob/main/static/images/profile-img-kang.jpg?raw=true"  width="200" height="200"/>|<img src="https://github.com/wvssm/Jeju_Oreum_Stamp_Project/blob/main/static/images/profile-img-jung.jpg?raw=true"  width="200" height="200"/>|<img src="https://github.com/wvssm/Jeju_Oreum_Stamp_Project/blob/main/static/images/profile-img-sim.jpg?raw=true"  width="200" height="200"/>|<img src="https://github.com/wvssm/Jeju_Oreum_Stamp_Project/blob/main/static/images/profile-img-lee.jpg?raw=true"  width="200" height="200"/>|
|Backend|기획, Frontend|Frontend|기획, PPT|
|비를 뚫고온 구세주☔|오름 정복중인 오름 러버😍|재주많은 덕후🤓|분위기메이커(저세상 텐션)🥳|


# 트러블 슈팅
### 문제
- 카카오맵 api를 사용하던 도중, 권한 거부 오류가 발생하였다.
### 해결
- 도메인 등록 시 포트번호를 8000번으로 등록해야하는데 8080으로 등록하여 발생한 문제였다. (포트 번호 잘못 입력)
- 포트 번호를 8000으로 변경하여 등록하니 해결되었다.
  
### 문제
- Django에서 css, js, image 파일의 경로를 인식하지 못했다.
### 해결
  - 별도의 static 파일을 생성하여, 해당 파일들을 모아둬야 했다.
  - static 폴더를 분리하는 이유
    - 정적과 동적 처리를 따로 할 수 있는 웹서버에서 정적 파일을 찾을 때 하나의 경로를 거치는 것이 신속한 응답에 유리하기 때문에, 정적 파일(css,js,images,fonts)들을 모아놓는 것이다.

### 문제
- html의 button이 제대로 작동하지 않았다.
### 해결
  - script 부분의 앞부분에서 오류가 발생하여 뒤에 등록한 버튼의 이벤트가 제대로 작동하지 않은 것이었다.
<br><br>

# 느낀점 및 개선하고 싶은 점
### 좋았던 점
- Django의 ORM을 이용하여 로그인, 회원가입, 스탬프 저장 기능을 구현해 보아서 좋았다.
  
- 카카오 지도 API의 마커나 인포 윈도우를 커스텀해 볼 수 있어서 좋았다.
  
- 제주의 멋진 오름들을 알게되어서 좋았다.🌋
  
### 아쉬웠던 점
- 오름 정보를 제대로 제공하는 api가 없어서 많은 오름을 표시하지 못한 것이 아쉬웠다. 
  - 향후 서귀포시에서 제공하는 json 데이터를 이용하여, 더 많은 오름을 표시하는 방향으로 업데이트 하고 싶다.

- 독창적인 서비스를 제공하지 못한 것이 아쉽다.  
  - "JStamp"라고 제주도의 카페, 관광지, 유적지 등 테마별로 특정 장소를 방문하면 스탬프를 제공하고, 해당 스탬프로 상품을 교환할 수 있게 하는 어플이 존재한다.
  
  - 위의 어플과 차별성을 두기 위해, 방문자의 기록, 사진 공유 등 추억과 관광정보를 공유하는 게시판 기능을 생성하거나, 해당 오름에서 쓰레기 회수를 하는 것을 인증하면 포인트를 제공하는 등 **올라갈지도**만의 특별한 서비스를 고민하고 있다.


### 개선하고 싶은 점
- 정보의 질을 올리고 싶다. 
  - 현재 오름의 주소, 간단한 소개, 오름 홈페이지의 url을 제공하고 있다. 기본적인 정보뿐만 아니라 주차장, 화장실의 유무 등 유용한 정보를 제공하고 싶다.
  
- 공유 기능을 추가하고 싶다.
  - 자신이 모은 스탬프가 담긴 지도를 공유함으로써 타인의 흥미를 불러올 수 있다고 생각한다.
<br><br>

# 프로젝트의 발전 방향
- 단순 스탬프를 찍어 방문을 기록하는 것이 아닌, 스탬프를 찍으면 제주도 현지 카페의 커피 교환권을 제공하는 등 주변 상권을 올릴 수 있는 방안을 제안할 수 있다.
  
- 추억 남기기, 쓰레기 줍기 챌린지 등 단순 방문을 넘어 오름을 보호할 수 있는 컨텐츠를 제공하는 웹페이지로 발전할 수 있다. 
  
- 오름 관광 정보 및 커뮤니티의 기반이 될 수 있다.
<br><br>
