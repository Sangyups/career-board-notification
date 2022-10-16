# Career Board Notification

## 개요

고려대학교 컴퓨터학과 진로정보게시판에서 채용 공고를 가져와서 새로 업데이트 된 공고를 알려줍니다.

## 기능

- 매일 13시(한국 시간)마다 진로게시판에서 새로 업데이트 된 내용을 찾아 알림을 줍니다.
- 현재 가능한 알림 수단
  - 슬랙
  - 디스코드
  - github issue(지원예정)

현재 main 브랜치에 push될 때마다 oracle cloud 무료 인스턴스에 자동 배포되고 해당 인스턴스에서 crontab을 통해 실행 중입니다.<br>

> _oracle cloud의 free tier는 서버가 불안정할 때가 많고 oracle 대시보드 자체도 불편한 점이 많아 추후 github action의 cron job을 통해 배포할 예정입니다._
