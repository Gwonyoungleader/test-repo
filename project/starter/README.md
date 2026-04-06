# Starter (Notebook only)

- 실행 파일: `tpcdrum_event_baseline.ipynb`
- 입력 CSV: `tpcd_ai_event.csv`
- 타깃: `true_dxdy` 또는 `true_dzdy`

노트북 내부에서 다음을 수행합니다.
1. 데이터 로드
2. train/test split
3. RandomForestRegressor 학습
4. RMSE/MAE/R2 계산
5. feature importance + AI vs truth 시각화
