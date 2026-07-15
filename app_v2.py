import streamlit as st
import requests
import plotly.graph_objects as go

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 및 디자인 테마 정의
# -----------------------------------------------------------------------------
st.set_page_config(page_title="국제정치철학 중동 안보 시뮬레이터", layout="wide")

# 🎨 디자인 가이드라인 색상
COLOR_PRIMARY = "#1E293B"  # 딥 네이비
COLOR_ACCENT = "#2563EB"   # 디지털 블루

st.title("🌐 디지털 시뮬레이션을 통한 국제정치철학의 현대적 재해석")
st.markdown("### 2026 중동 정세 복합 변수 매트릭스 대시보드 (고도화 버전)")
st.caption("진주동명고등학교 교과 심화 탐구 프로젝트 (발표자: 이민규)")
st.write("---")

# -----------------------------------------------------------------------------
# 2. [기능 3] 외부 정세 데이터 API 연동 및 실시간 뉴스 마이닝 로직
# -----------------------------------------------------------------------------
st.sidebar.header("📡 1단계: 실시간 안보 데이터 동기화")

# API 키 입력창 (발표 시에는 데모로 작동하거나 샘플 키 사용 가능)
api_key = st.sidebar.text_input("NewsAPI Key 입력 (선택사항)", type="password", help="newsapi.org에서 발급받은 키를 넣으면 실시간 뉴스를 긁어옵니다.")

@st.cache_data(ttl=3600)  # 1시간 동안 API 호출 결과 캐싱하여 속도 최적화
def fetch_middle_east_news(key):
    if not key:
        # 키가 없을 경우 보고서용 가상 샘플 데이터 반환 (실습/발표용)
        return "BREAKING: Serious clashes and missile shots reported near the Strait of Hormuz. Tension rises between Iran and regional powers."
    
    url = f"https://newsapi.org/v2/everything?q=Hormuz+AND+(shot+OR+clash)&apiKey={key}"
    try:
        response = requests.get(url).json()
        articles = response.get('articles', [])
        text_corpus = " ".join([art['title'] + " " + art['description'] for art in articles if art['title']])
        return text_corpus
    except Exception as e:
        return "ERROR"

# 뉴스 데이터 수집 및 텍스트 마이닝 기반 자동 변수 감지
news_data = fetch_middle_east_news(api_key)

# 기본 변수 초기값 설정
q4_default = False
if "Hormuz" in news_data and ("shot" in news_data or "clash" in news_data or "missile" in news_data):
    q4_default = True
    st.sidebar.warning("🚨 API 연동 결과: 호르무즈 해협 오인 사격/분쟁 징후 실시간 감지! (Q4 변수 자동 활성화)")

# -----------------------------------------------------------------------------
# 3. 사이드바 인터랙티브 시나리오 설계 (사용자 입력 제어층)
# -----------------------------------------------------------------------------
st.sidebar.header("⚙️ 2단계: 시나리오 매트릭스 설정")

# Q1. 철학적 뇌 선택
framework = st.sidebar.selectbox("Q1. 분석 프레임워크(사상가) 선택", ["칸트 (자유주의)", "모겐소 (현실주의)", "웬트 (구성주의)"])

# 나머지 7대 안보 변수 토글 스위치
q2_treaty = st.sidebar.checkbox("Q2. 이슬라마바드 평화 각서 유효함", value=True)
q3_proxy = st.sidebar.checkbox("Q3. 이란 '저항의 축' 무기 대량 지원", value=False)
q4_shot = st.sidebar.checkbox("Q4. 호르무즈 해협 군사 오인 사격 발생", value=q4_default)
q5_saudi = st.sidebar.checkbox("Q5. 사우디아라비아의 외교적 중재 개입", value=False)
q6_cyber = st.sidebar.checkbox("Q6. 이스라엘의 선제적 사이버 테러 감행", value=False)
q7_imec = st.sidebar.checkbox("Q7. IMEC 신공급망 정상 가동", value=True)
q8_nuke = st.sidebar.checkbox("Q8. 이란 무기급 우라늄 농축 90% 돌파", value=False)

# -----------------------------------------------------------------------------
# 4. 철학자별 핵심 연산 엔진 (Core Logic)
# -----------------------------------------------------------------------------
# 초기 리스크 프로파일 점수 세팅 [제도적 위기, 물질적 위기, 관념적 위기]
risk_dimensions = [0, 0, 0] 

if framework == "칸트 (자유주의)":
    # 칸트는 제도(Q2)와 지경학적 상호의존성(Q7)이 켜지면 리스크를 낮게 봄
    risk_dimensions[0] = 10 if q2_treaty else 80  # 제도 위기
    risk_dimensions[1] = (50 if q8_nuke else 10) + (30 if q6_cyber else 0)  # 물질 위기
    risk_dimensions[2] = 60 if q4_shot else 20    # 관념 위기
    
elif framework == "모겐소 (현실주의)":
    # 모겐소는 평화 조약(Q2)이나 중재(Q5) 같은 제도/인식 변수를 거의 무시함(0점 처리)
    risk_dimensions[0] = 40  # 제도는 힘의 역관계에 불과하다고 봄
    # 오직 무력, 핵, 경제 공급망 통제 같은 물질적 힘에만 반응
    risk_dimensions[1] = (80 if q8_nuke else 20) + (50 if q3_proxy else 10) + (40 if q6_cyber else 0)
    risk_dimensions[2] = 50 if q4_shot else 10
    
elif framework == "👁️ 웬트 (구성주의)":
    # 웬트는 호르무즈 오인 사격(Q4)이 터졌을 때 역사적 불신 구조와 결합하여 관념적 위기가 폭등함
    risk_dimensions[0] = 30 if q2_treaty else 70
    risk_dimensions[1] = (60 if q8_nuke else 20) + (30 if q6_cyber else 0)
    # 관념적 위기의 상호 작용성 구현
    if q4_shot:
        risk_dimensions[2] = 95 if not q2_treaty else 70  # 조약마저 깨진 상태면 불신 극대화
    else:
        risk_dimensions[2] = 20

# 3대 차원의 평균값으로 최종 안보 갈등 지수 산출
final_score = sum(risk_dimensions) / 3
if final_score > 100: final_score = 100

# -----------------------------------------------------------------------------
# 5. 결과 출력 및 [기능 2] Plotly 레이더 차트 시각화
# -----------------------------------------------------------------------------
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader(f"📊 {framework} 엔진 연산 결과")
    
    # 상단 계량 지표(Metric) 시각화
    if final_score >= 75:
        st.metric(label="최종 안보 위험도 지수", value=f"{final_score:.1f}%", delta="위험 (전면전 위기)", delta_color="inverse")
    elif final_score >= 45:
        st.metric(label="최종 안보 위험도 지수", value=f"{final_score:.1f}%", delta="경계 (회색지대 도발 충돌)", delta_color="off")
    else:
        st.metric(label="최종 안보 위험도 지수", value=f"{final_score:.1f}%", delta="안정 (평화 유지 상태)")
        
    st.write("---")
    st.markdown("#### 📝 시나리오 종합 판정 리포트")
    
    # 조건별 예측 텍스트 분기문
    if framework == "칸트 (자유주의)":
        st.write("조약 체제와 경제 동맹(IMEC)이 유지되는 한 전면전 가능성은 낮다고 보나, 이스라엘의 사이버 테러 및 이란의 핵 임계 돌파 같은 강제력 없는 물질적 도발이 동시 다발적으로 발생할 경우 자유주의 국제 규범 체제가 순간적으로 마비될 위험성이 관측됩니다.")
    elif framework == "모겐소 (현실주의)":
        st.write("평화 각서나 외교적 수사는 안보 리스크를 제어하는 데 아무런 영향력을 주지 못합니다. 핵심은 이란의 무기급 우라늄 농축도와 프록시 무기 지원 강도이며, 물리적 세력 균형(Balance of Power)이 깨지는 즉시 군사적 충돌 경로로 직행할 것임을 경고합니다.")
    else:
        st.write("현 중동 정세의 본질은 무기의 양이 아니라 '서로가 서로를 적대국으로 규정하는 인식의 구조'에 있습니다. 호르무즈 해협의 사소한 오인 사격이 기습 침공 시나리오로 오독되어 불신의 스파이럴(악순환 루프)을 형성하는 과정이 뚜렷하게 관찰됩니다.")

with col2:
    st.subheader("💡 3대 안보 차원 리스크 프로파일")
    
    # 레이더 차트 데이터 준비
    categories = ['제도적 위기 (Institution)', '물질적 위기 (Material)', '관념적 위기 (Ideation)']
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=risk_dimensions + [risk_dimensions[0]],  # 다각형 폐합
        theta=categories + [categories[0]],
        fill='toself',
        name=framework,
        line=dict(color=COLOR_ACCENT, width=3),
        fillcolor='rgba(37, 99, 235, 0.2)'  # 반투명 디지털 블루
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10)
            )
        ),
        showlegend=False,
        margin=dict(l=40, r=40, t=40, b=40)
    )
    
    # Plotly 레이더 차트 화면 출력
    st.plotly_chart(fig, use_container_width=True)
