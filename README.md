# TPC AI 튜토리얼 프로젝트 (TPCDrum 정리본)

현재 작업물은 `project/tpcdrum/`에 모아두었습니다.

- `00_tutorial_plan_kr.ipynb`: 튜토리얼 세션 설계
- `01_data_contract_kr.ipynb`: 필요한 데이터/소스 체크리스트
- `10_event_baseline.ipynb`: `tpcd_ai_event.csv` baseline
- `99_external_repo_sync_template.ipynb`: 외부 repo 파일 반영 템플릿

## 실행
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r project/starter/requirements.txt
jupyter notebook
```

## 컨벤션
- 숫자용 truth slope: `MCTrack vertex + GetCoordinateGeantToPad()`
- display용 truth trajectory: `MCStepTPCDrum`
- 용어: `CSV reco` 대신 **Fitting method**
