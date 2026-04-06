# TPC AI 튜토리얼 프로젝트 (Notebook 전용)

요청하신 대로, 이 브랜치는 **주피터 노트북 중심**으로 정리했습니다.

## 실행 순서
1. `project/tutorial_plan_kr.ipynb`  
   - 수업 흐름(물리 의미 + 코드 대응 + branch 대응)
2. `project/data_contract_kr.ipynb`  
   - 업로드/연동 체크리스트
3. `project/starter/tpcdrum_event_baseline.ipynb`  
   - `tpcd_ai_event.csv` 기반 event-level AI baseline 실습

## 빠른 시작
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r project/starter/requirements.txt
jupyter notebook
```

노트북에서 아래 컨벤션을 유지합니다.
- 숫자용 truth slope: `MCTrack vertex + GetCoordinateGeantToPad()`
- display용 truth trajectory: `MCStepTPCDrum`
- 용어: `CSV reco` 대신 **Fitting method**
