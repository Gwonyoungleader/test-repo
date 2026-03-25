# 4주 프로젝트: TPC 기초 머신러닝/딥러닝 (학부 2학년용)

이 저장소는 **최소한의 물리 지식**으로 수행 가능한 4주짜리 팀 프로젝트 템플릿입니다.
주제는 TPC(Time Projection Chamber) 신호를 단순화한 합성 데이터 기반으로,
ML/DL 모델을 적용하고 물리적으로 해석하는 것입니다.

## 프로젝트 목표
- TPC 데이터의 기본 개념(히트, 노이즈, 트랙)을 이해한다.
- 분류/회귀 중 하나의 문제를 ML 및 DL로 풀어본다.
- 결과를 물리적으로 해석하고 실패 사례를 분석한다.

## 4주 운영 계획

### Week 1 — 물리 배경 + 데이터 생성
- 미니 강의: TPC 원리(드리프트, 히트, 노이즈) 20~30분
- 합성 데이터 생성 코드 실행
- 데이터 시각화 및 통계 요약

### Week 2 — 베이스라인 ML
- Train/Validation/Test 분리
- 베이스라인 모델 1개 이상 구현
  - 예: Logistic Regression, Random Forest, 선형회귀
- 지표 계산: Accuracy/F1 혹은 MAE/RMSE

### Week 3 — 간단 DL
- 간단한 MLP 또는 CNN 구현
- 과적합 점검(학습곡선)
- 하이퍼파라미터 최소 2개 비교

### Week 4 — 물리 해석 중심 보고
- 실패 사례 시각화 및 원인 분석
- 노이즈/누락히트/아웃라이어 변화 실험
- 최종 발표(슬라이드 + 코드 + 결과표)

## 권장 주제 2가지(택1)
1. **분류:** 직선 트랙 vs 굽은 트랙
2. **회귀:** 트랙 기울기/절편 추정

## 저장소 구조
- `project/assignment_guide_kr.md`: 학생 안내문
- `project/grading_rubric_kr.md`: 채점표
- `project/starter/`: 시작 코드

## 빠른 시작
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r project/starter/requirements.txt
python project/starter/generate_data.py --task classify
python project/starter/baseline_ml.py --task classify
```

