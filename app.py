import streamlit as st

# =================================================================
# 1. 웹 프로그램 레이아웃 및 디자인 설정
# =================================================================
st.set_page_config(page_title="중동 정세 시뮬레이터", page_icon="🧠", layout="centered")

st.title("🧠 국제정치철학 기반 중동 정세 예측 시뮬레이터")
st.markdown("---")

# =================================================================
# 2. 사이드바 (왼쪽 입력창): 사용자에게 5대 질문 던지기
# =================================================================
st.sidebar.header("🛠️ 정세 변수 설정 (5대 질문)")

# Q1. 철학 선택 (라디오 버튼)
philosophy = st.sidebar.radio(
    "1. 분석에 사용할 철학적 뇌를 선택하세요.",
    ("이마누엘 칸트 (제도주의)", "한스 모겐소 (현실주의)", "알렉산더 웬트 (구성주의)")
)

# Q2~Q5. 토글 스위치 형태의 질문들
treaty_active = st.sidebar.checkbox("2. 이슬라마바드 평화 각서가 유효합니까?", value=True)
proxy_support = st.sidebar.checkbox("3. 이란이 '저항의 축'에 비대칭 무기를 지원합니까?", value=False)
accidental_shot = st.sidebar.checkbox("4. 호르무즈 해협에서 오인 사격이 발생했습니까?", value=True)
saudi_mediation = st.sidebar.checkbox("5. 사우디아라비아가 적극적 외교 중재에 나섰습니까?", value=False)

# =================================================================
# 3. 핵심 알고리즘 연산 파트
# =================================================================
conflict_score = 50
log = []

if "칸트" in philosophy:
    log.append("🕊️ **[칸트 알고리즘 작동]** 제도적 합의와 공화국 간의 평화 연맹 가능성을 계산합니다.")
    if treaty_active:
        conflict_score -= 30
        log.append("- 이슬라마바드 조약 활성화: 갈등 지수 대폭 감소 (-30)")
    if saudi_mediation:
        conflict_score -= 15
        log.append("- 사우디의 평화 연맹 가입 및 중재: 안보 거버넌스 강화 (-15)")
    if proxy_support or accidental_shot:
        conflict_score += 10
        log.append("- 비국가 행위자 및 도발 발생: 제도의 구속력 덕분에 미미한 상승 (+10)")

elif "모겐소" in philosophy:
    log.append("⚔️ **[모겐소 알고리즘 작동]** 조약은 무효하며 오직 수치화된 군사력 균형만 계산합니다.")
    conflict_score = 20 
    log.append("- 이스라엘의 전통적 국력 우위로 기본적 억지력 작동 중 (기본값 20)")
    if proxy_support:
        conflict_score += 40
        log.append("- 이란의 비대칭 전력 획득: 힘의 균형 파괴, 갈등도 대폭 상승 (+40)")
    if accidental_shot:
        conflict_score += 15
        log.append("- 군사적 충돌 스파크 발생: 국익 방어를 위한 긴장 고조 (+15)")
    if treaty_active or saudi_mediation:
        log.append("- *(무시됨)* 현실주의는 종이 위의 조약이나 외교적 중재를 변수로 인정하지 않습니다.")

elif "웬트" in philosophy:
    log.append("👁️ **[웬트 알고리즘 작동]** 행위자 간 누적된 원한(-90)과 정체성 갈등을 계산합니다.")
    if proxy_support:
        conflict_score += 25
        log.append("- '저항의 축' 무기 지원: 반서구 시아파 정체성 연대 결속 확정 (+25)")
    if accidental_shot:
        conflict_score += 40
        log.append("- 🚨 **오인 사격 발생:** 깊은 불신 매트릭스로 인해 이를 '실수'가 아닌 '기습 선제 타격'으로 오독! (+40)")
    if treaty_active:
        conflict_score -= 10 
        log.append("- 조약 체결: 형식적 제도 진입했으나, 내면의 주적 인식이 남아있어 효과 미미 (-10)")
    if saudi_mediation:
        conflict_score -= 15
        log.append("- 사우디 중재: 이슬람 내부 정체성 딜레마가 발동하여 양측의 적대감 일시 완화 (-15)")

# 스코어 보정 (0 ~ 100)
conflict_score = max(0, min(100, conflict_score))

# =================================================================
# 4. 메인 화면 (오른쪽 리포트 화면): 결과 시각화
# =================================================================
st.subheader("📊 시뮬레이션 가동 결과 분석 리포트")

# 연산 과정 로그 출력
for line in log:
    st.write(line)

st.markdown("---")

# 최종 갈등 지수 시각화 (프로그레스 바)
st.metric(label="🔥 최종 연산된 중동 갈등 지수", value=f"{conflict_score} %")
st.progress(conflict_score / 100)

st.markdown("---")

# 최종 예측 결과에 따른 UI 색상 카드 출력
if conflict_score >= 70:
    st.error("🔮 **최종 예측 결과: [🚨 중동 전면전 재발발 및 시스템 붕괴]**")
    st.caption("불신과 비대칭 전력이 폭발하여 조약이 파기되고 통제 불능의 보복 루프에 진입했습니다.")
elif 40 <= conflict_score < 70:
    st.warning("🔮 **최종 예측 결과: [⚠️ 국지적 대리전 지속 및 불안정한 정전]**")
    st.caption("전면전은 피했으나 비국가 행위자들의 도발과 긴장 상태가 지속되는 회색지대 상태입니다.")
else:
    st.success("🔮 **최종 예측 결과: [✅ 평화 정착 및 지역 안정화 지표 달성]**")
    st.caption("국제 제도의 구속력 또는 압도적 억지력이 작동하여 안정적인 평화 궤도에 진입했습니다.")
