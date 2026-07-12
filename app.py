import streamlit as st

# =================================================================
# 1. 페이지 레이아웃 및 스타일 설정
# =================================================================
st.set_page_config(
    page_title="고도화된 중동 정세 시뮬레이터",
    page_icon="🔮",
    layout="centered"
)

st.title("🔮 8대 복합 변수 기반 중동 정세 예측 시뮬레이터")
st.markdown("---")

# =================================================================
# 2. 사이드바: 8대 질문 및 변수 제어 환경
# =================================================================
st.sidebar.header("🛠️ 고도화된 정세 변수 (8대 질문)")

# Q1. 철학적 뇌 선택
philosophy = st.sidebar.radio(
    "1. 분석 프레임워크 선택",
    ("이마누엘 칸트 (자유주의)", "한스 모겐소 (현실주의)", "알렉산더 웬트 (구성주의)")
)

st.sidebar.markdown("---")
st.sidebar.subheader("📋 실시간 외교·안보 변수")

# Q2 ~ Q8. 상황 변수 토글 스위치
treaty_active = st.sidebar.checkbox("2. 이슬라마바드 평화 각서가 유효합니까?", value=True)
proxy_support = st.sidebar.checkbox("3. 이란이 '저항의 축'에 비대칭 무기를 지원합니까?", value=False)
accidental_shot = st.sidebar.checkbox("4. 호르무즈 해협에서 오인 사격이 발생했습니까?", value=True)
saudi_mediation = st.sidebar.checkbox("5. 사우디가 적극적 외교 중재에 나섰습니까?", value=False)
cyber_attack = st.sidebar.checkbox("6. 이스라엘이 이란에 선제 사이버 테러를 감행했습니까?", value=False)
imec_active = st.sidebar.checkbox("7. IMEC(인도-중동-유럽 경제회랑) 신공급망이 작동 중입니까?", value=True)
nuclear_breakout = st.sidebar.checkbox("8. 이란이 우라늄 농축 90%(핵임계점)를 돌파했습니까?", value=False)

# =================================================================
# 3. 8대 복합 변수 철학별 알고리즘 연산
# =================================================================
conflict_score = 50
log = []

# --- [1] 칸트 모델: 제도 및 경제적 상호의존 중심 ---
if "칸트" in philosophy:
    log.append("🕊️ **[칸트 알고리즘]** 제도적 구속력과 상호의존성 매커니즘을 연산합니다.")
    if treaty_active:
        conflict_score -= 25
        log.append("🟢 조약의 규범적 구속력 작동 (-25)")
    if imec_active:
        conflict_score -= 20
        log.append("🟢 IMEC 공급망 가동: 경제적 상호의존성이 전쟁 비용을 증폭시켜 평화 유도 (-20)")
    if saudi_mediation:
        conflict_score -= 10
        log.append("🟢 다자주의 평화 연맹의 중재력 가동 (-10)")
    if proxy_support or accidental_shot:
        conflict_score += 15
        log.append("🟡 돌발 도발 및 대리전 긴장: 제도의 복원력으로 인해 상승폭 상쇄 (+15)")
    if cyber_attack or nuclear_breakout:
        conflict_score += 20
        log.append("🔴 체제 불신 및 핵 확산 징후: 제도적 통제 한계점 도달 (+20)")

# --- [2] 모겐소 모델: 물리적 전력 격차와 공격 현실주의 중심 ---
elif "모겐소" in philosophy:
    log.append("⚔️ **[모겐소 알고리즘]** 선언적 조약 및 경제 공급망은 무시하며, 오직 군사적 힘의 균형만 계산합니다.")
    conflict_score = 25  # 기본 이스라엘 우위 상황
    log.append("🟡 이스라엘의 물질적 군사력(90) 우위로 인한 기본적 억지력 상태 (기본 갈등도 25)")
    
    if nuclear_breakout:
        conflict_score += 45
        log.append("🚨 **[게임 체인저]** 이란의 핵 임계점 돌파: 세력 균형의 완전 파괴 및 실존적 위협 고조 (+45)")
    if proxy_support:
        conflict_score += 20
        log.append("🔴 이란의 비대칭 전력 및 비국가 행위자 활용으로 물질적 위협 증가 (+20)")
    if cyber_attack:
        conflict_score += 15
        log.append("🔴 선제 사이버 타격을 통한 힘의 투사: 안보 딜레마 자극 (+15)")
    if accidental_shot:
        conflict_score += 10
        log.append("🔴 국지적 물리 충돌 발생에 따른 안보 대응 (+10)")
    if treaty_active or imec_active or saudi_mediation:
        log.append("⚪ *(무시됨)* 현실주의 패러다임은 상호의존성, 조약, 외교 중재를 가중치로 인정하지 않습니다.")

# --- [3] 웬트 모델: 역사적 불신 매트릭스와 주관적 인지(오독) 중심 ---
elif "웬트" in philosophy:
    log.append("👁️ **[웬트 알고리즘]** 누적된 적대감(-90점) 구조 속에서 각 행위자가 사건을 어떻게 '해석'하는지 연산합니다.")
    
    if accidental_shot:
        conflict_score += 35
        log.append("🚨 **[상호 오독 루프]** 호르무즈 오인 사격 발생: 깊은 불신 탓에 이를 실수가 아닌 '선제 침공'으로 확증 편향 (+35)")
    if cyber_attack:
        conflict_score += 25
        log.append("🚨 **[적대 정체성 강화]** 사이버 테러 발생: 상대방을 공존 불가능한 '절대 악'으로 재정의 (+25)")
    if proxy_support:
        conflict_score += 15
        log.append("🔴 '저항의 축' 연대: 관념적 반서구 정체성 결속 가속 (+15)")
    if nuclear_breakout:
        conflict_score += 20
        log.append("🔴 핵 보유 시도: 양측의 인식을 '홉스적 생존 투쟁 구조'로 전면 고착화 (+20)")
    if treaty_active:
        conflict_score -= 5
        log.append("🟡 평화 조약 체결: 형식적 제도이나 불신 구조가 내부를 지배하여 효과 미미 (-5)")
    if imec_active or saudi_mediation:
        conflict_score -= 15
        log.append("🟢 공급망 구축 및 사우디 중재: 이익의 공유가 적대적 정체성을 느슨하게 완화 (-15)")

# 스코어 보정 (0 ~ 100)
conflict_score = max(0, min(100, conflict_score))

# =================================================================
# 4. 결과 대시보드 시각화 및 출력
# =================================================================
st.subheader("📊 확장형 시뮬레이션 결과 리포트")

# 로그 박스 렌더링
st.info("\n".join(log))

st.markdown("---")

# 갈등 지수 게이지 표시
st.metric(label="🔥 최종 복합 연산된 중동 갈등 지수", value=f"{conflict_score} %")
st.progress(conflict_score / 100)

st.markdown("---")

# 종합 예측 결과 출력
if conflict_score >= 75:
    st.error("🔮 **최종 예측 결과: [🚨 제5차 중동전쟁 발발 및 국제 안보 시스템의 전면적 파산]**")
    st.caption("핵 위협, 사이버 테러, 상호 불신이 임계점을 넘었습니다. 기존의 평화 각서는 종이 조각이 되었으며 시스템은 전면전 루프에 진입했습니다.")
elif 45 <= conflict_score < 75:
    st.warning("🔮 **최종 예측 결과: [⚠️ 초국적 대리전 격화 및 회색지대 도발 구도 지속]**")
    st.caption("경제적 경제회랑(IMEC)이나 외교적 중재 덕분에 전면전은 간신히 억제 중이나, 사이버전과 대리 세력을 통한 국지적 충돌이 끊이지 않는 위태로운 상태입니다.")
else:
    st.success("🔮 **최종 예측 결과: [✅ 다자적 거버넌스 정착 및 다차원적 평화 구조 달성]**")
    st.caption("평화 조약의 제도적 신뢰성과 경제적 상호의존 공급망이 승리했습니다. 군사적 자극 요소들이 시스템 내부에서 완전히 흡수 및 통제됩니다.")
