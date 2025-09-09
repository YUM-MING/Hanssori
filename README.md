# Hanssori
[개인] AI 기반 사용자 맞춤 국악 추천 웹서비스

## 📅 개발 기간
> 2025.03.27 ~ 2025.05.29

## 📖 프로젝트 소개
>  **Hanssori**는 전통 국악을 현대적으로 즐길 수 있도록 설계된 AI 기반 국악 추천 웹서비스입니다.<br>
> 단순한 음악 감상 사이트가 아니라, **사용자의 감정·취향·상황을 반영한 맞춤형 추천**과 **개인화 플레이리스트 생성** 기능을 제공합니다. 실제 국악 관련 SNS 및 아카이브 데이터를 연동하여, 실사용 가능한 음악 플랫폼처럼 구현했습니다.

<img width="872" height="1063" alt="image" src="https://github.com/user-attachments/assets/70df928a-8130-4ede-a668-af69f19dd3d5" />

<br>

## 🎮 프로젝트 내용
🔹 1. 메인 페이지 & 아카이브 인기곡

국악 아카이브에서 최근 많이 듣는 국악 9곡을 크롤링<br>

각 곡 이미지를 클릭하면 바로 재생 가능<br>

---
🔹 2. 검색 기반 추천

KoBERT 감정 분석 모델을 파인튜닝하여 7개 감정 분류<br>

감정 + 템포 + 시김새 + 장르 + 악기 정보를 벡터화 → 콘텐츠 기반 필터링 모델로 추천<br>

추천 결과에서 바로 듣기 및 다운로드 가능<br>

---
🔹 3. 최근 들은 노래 (로컬 스토리지 저장)

추천 결과에서 선택한 곡은 자동으로 우측 사이드바 ‘최근 들은 노래’에 저장<br>

로컬스토리지 활용 → 새로고침 후에도 유지<br>

여러 번 검색하면 데이터가 누적되어 더 다양한 플레이리스트 생성 기반 제공<br>

---
🔹 4. 개인화 플레이리스트

플레이리스트 메뉴 선택 시, 최근 들은 노래 데이터를 기반으로 코사인 유사도 분석<br>

사용자의 취향과 유사한 곡을 자동으로 모아 개인 맞춤형 플레이리스트 제공<br>


## 🛠️ 기술 스택

| **영역**         | **기술**       |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **백엔드**   | ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) |
| **프론트 엔드**       | ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)  |
| **AI 모델**       | ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white) |
| **데이터베이스**    |	![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) |
| **협업 도구**    |	![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white) |

## 🌟 **활용 방안**

| **활용 분야**                | **세부 내용**                                                                                     | **기대 효과**                                                                                           |
|------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| **국악 대중**    | - 전통 국악을 현대적 UI/UX로 접할 수 있도록 지원         | - 젊은 세대의 국악 접근성 향상 |
| **개인화 음악 서비스**     | - 감정 분석 + 협업 필터링 기반 플레이리스트 제공       | - 맞춤형 경험 제공으로 지속적 이용 유도              |
| **문화 교육**     | - 악기·감정·장르별 학습 자료로 활용 가능       | - 전통음악의 교육적 가치 제고              |

## 👥 **팀원 소개**

| **이름**       | **역할**               | **담당 업무**                                             | **깃허브 주소** |
|----------------|------------------------|----------------------------------------------------------|----------------------------------------|
| **이유민**     | **개발 총괄<br>(개인 프로젝트)** | - Django 기반 백엔드 및 추천 알고리즘 구현.<br>- KoBERT 감정 분석 모델 파인튜닝 및 연동.<br>- 국악 아카이브 크롤링 및 데이터 전처리<br>- UI/UX 설계 및 전체 시스템 구현 |  https://github.com/YUM-MING |


