import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="김동욱 - Modern AI Portfolio",
    page_icon="🚒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 모던 AI 스타일 CSS
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
        @import url('https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css');
        * { font-family: 'Inter', sans-serif; }
        .stApp { background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #667eea 100%); background-size: 400% 400%; animation: gradient-wave 8s ease infinite; min-height: 100vh; }
        @keyframes gradient-wave { 0%, 100% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } }
        .modern-card { background: rgba(255,255,255,0.95); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.3); border-radius: 24px; box-shadow: 0 20px 40px rgba(0,0,0,0.1), 0 0 0 1px rgba(255,255,255,0.05); padding: 2.5rem; margin: 1.5rem auto; transition: all 0.4s cubic-bezier(0.175,0.885,0.32,1.275); position: relative; overflow: hidden; }
        .modern-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px; background: linear-gradient(90deg, transparent, rgba(102,126,234,0.5), transparent); }
        .modern-card:hover { transform: translateY(-8px) scale(1.02); box-shadow: 0 32px 64px rgba(0,0,0,0.15), 0 0 0 1px rgba(255,255,255,0.1); }
        .ai-avatar { width: 180px; height: 180px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center; position: relative; margin: 0 auto; box-shadow: 0 20px 40px rgba(102,126,234,0.3), 0 0 0 8px rgba(255,255,255,0.1); animation: float 6s ease-in-out infinite; }
        .ai-avatar::before { content: ''; position: absolute; inset: -4px; border-radius: 50%; background: conic-gradient(from 0deg, #667eea, #764ba2, #667eea); z-index: -1; animation: rotate 10s linear infinite; opacity: 0.5; }
        @keyframes float { 0%,100% { transform: translateY(0px); } 50% { transform: translateY(-15px); } }
        @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
        .gradient-text { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 800; }
        .feature-card { background: rgba(255,255,255,0.8); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); border-radius: 16px; padding: 2rem; text-align: center; position: relative; transition: all 0.3s ease; overflow: hidden; }
        .feature-card:hover { transform: translateY(-5px); box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
        .feature-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, #667eea, #764ba2); border-radius: 16px 16px 0 0; }
        .icon-modern { width: 64px; height: 64px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 16px; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; box-shadow: 0 8px 24px rgba(102,126,234,0.3); position: relative; overflow: hidden; }
        .icon-modern::before { content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent); transform: rotate(45deg); animation: shine 3s ease-in-out infinite; }
        @keyframes shine { 0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); } 100% { transform: translateX(100%) translateY(100%) rotate(45deg); } }
        .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin: 2rem 0; }
        .stat-item { background: rgba(255,255,255,0.9); border-radius: 12px; padding: 1.5rem; text-align: center; border: 1px solid rgba(255,255,255,0.2); position: relative; overflow: hidden; }
        .stat-number { font-size: 2.5rem; font-weight: 800; color: #667eea; margin-bottom: 0.5rem; }
        .stat-label { color: #64748b; font-size: 0.9rem; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px; }
        .progress-modern { background: rgba(102,126,234,0.1); height: 8px; border-radius: 4px; overflow: hidden; margin: 1rem 0; position: relative; }
        .progress-fill-modern { background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); height: 100%; border-radius: 4px; position: relative; animation: progress-load 2s ease-out; }
        .progress-fill-modern::after { content: ''; position: absolute; top: 0; right: 0; bottom: 0; width: 20px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.6)); animation: progress-shine 2s ease-in-out infinite; }
        @keyframes progress-load { from { width: 0%; } }
        @keyframes progress-shine { 0% { transform: translateX(-20px); } 100% { transform: translateX(20px); } }
        .section-header { text-align: center; margin-bottom: 3rem; }
        .section-title { font-size: 2.5rem; font-weight: 800; color: #1e293b; margin-bottom: 1rem; }
        .section-subtitle { color: #64748b; font-size: 1.1rem; font-weight: 400; }
        .timeline-modern { position: relative; padding-left: 2rem; }
        .timeline-modern::before { content: ''; position: absolute; left: 12px; top: 0; bottom: 0; width: 2px; background: linear-gradient(to bottom, #667eea, #764ba2); }
        .timeline-item-modern { position: relative; margin-bottom: 2rem; padding-left: 2rem; }
        .timeline-item-modern::before { content: ''; position: absolute; left: -2rem; top: 6px; width: 24px; height: 24px; background: linear-gradient(135deg, #667eea, #764ba2); border-radius: 50%; border: 4px solid white; box-shadow: 0 4px 12px rgba(102,126,234,0.3); }
        .quote-modern { background: rgba(255,255,255,0.9); border-left: 4px solid #667eea; border-radius: 12px; padding: 2rem; margin: 2rem 0; font-style: italic; font-size: 1.2rem; color: #334155; position: relative; }
        .quote-modern::before { content: '"'; font-size: 4rem; color: #667eea; position: absolute; top: -10px; left: 20px; opacity: 0.3; }
        .element-container { padding: 0 !important; }
        .stMarkdown { padding: 0 !important; }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display: none;}
        .stRadio > div { display: flex; justify-content: center; gap: 1rem; margin: 2rem 0; }
        .stRadio > div > label { background: rgba(255,255,255,0.9); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); border-radius: 12px; padding: 0.8rem 1.5rem; transition: all 0.3s ease; cursor: pointer; font-weight: 500; }
        .stRadio > div > label:hover { background: linear-gradient(135deg, #667eea, #764ba2); color: white; transform: translateY(-2px); }
        .particle-modern { position: absolute; width: 6px; height: 6px; background: rgba(102,126,234,0.6); border-radius: 50%; animation: float-particle 8s ease-in-out infinite; }
        @keyframes float-particle { 0%,100% { transform: translateY(0px) translateX(0px); opacity: 0.6; } 25% { transform: translateY(-20px) translateX(10px); opacity: 1; } 50% { transform: translateY(-10px) translateX(-10px); opacity: 0.8; } 75% { transform: translateY(-30px) translateX(5px); opacity: 1; } }
        .skill-badge { display: inline-block; background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem; font-weight: 500; margin: 0.25rem; box-shadow: 0 4px 12px rgba(102,126,234,0.3); transition: all 0.3s ease; }
        .skill-badge:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(102,126,234,0.4); }
    </style>
""", unsafe_allow_html=True)

# 페이지 선택
page = st.radio(
    "페이지 선택",
    ["🙋‍♂️ 자기소개", "👨‍🚒 장래희망", "🎨관심사와 학업현황", "🕵️ 성격과 강점", "🧾비전과 각오"],
    horizontal=True,
    label_visibility="collapsed"
)
if page == "🙋‍♂️ 자기소개":
    st.markdown("""
        <div class="modern-card">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
                <div style="text-align: center; position: relative;">
                    <div style="position: relative;">
                        <div class="ai-avatar" style="margin-bottom: 2rem;">
                            <i class="fas fa-user-circle" style="color: white; font-size: 3.5rem;"></i>
                        </div>
                        <div class="particle-modern" style="top: 20%; left: 15%; animation-delay: 0s;"></div>
                        <div class="particle-modern" style="top: 40%; right: 10%; animation-delay: 2s;"></div>
                        <div class="particle-modern" style="bottom: 30%; left: 20%; animation-delay: 4s;"></div>
                        <div class="particle-modern" style="bottom: 15%; right: 25%; animation-delay: 6s;"></div>
                    </div>
                    <h1 style="font-size: 3.5rem; font-weight: 800; margin-bottom: 1rem; color: #1e293b;">김동욱</h1>
                    <p class="gradient-text" style="font-size: 1.4rem; margin-bottom: 0.5rem; font-weight: 600;">Kim Dong Wook</p>
                    <p style="color: #64748b; font-size: 1.1rem; font-weight: 500;">소속 | 건양대학교 3학년 재학중</p>
                    <p style="color: #64748b; font-size: 1.1rem; font-weight: 500;">나이 | 24세</p>
                    <p style="color: #64748b; font-size: 1.1rem; font-weight: 500;">이메일 | dognwook14161@gmail.com</p>
                    <p style="color: #64748b; font-size: 1.1rem; font-weight: 500;">연락처 | 010-4266-7886</p>
                </div>
                <div>
                    <div class="stats-grid">
                        <div class="feature-card">
                            <div class="icon-modern">
                                <i class="fas fa-users" style="color: white; font-size: 1.5rem;"></i>
                            </div>
                            <h3 style="color: #1e293b; font-size: 1.3rem; font-weight: 700; margin-bottom: 1rem;">가족관계</h3>
                            <p style="color: #64748b; margin: 0; font-weight: 500;">저희 가족 관계는 부,모,형,반려동물을 포함한 5인 가족입니다.</p>
                        </div>
                        <div class="feature-card">
                            <div class="icon-modern">
                                <i class="fas fa-home" style="color: white; font-size: 1.5rem;"></i>
                            </div>
                            <h3 style="color: #1e293b; font-size: 1.3rem; font-weight: 700; margin-bottom: 1rem;">거주지</h3>
                            <p style="color: #64748b; margin: 0; font-weight: 500;">경기도 시흥시에 거주 중입니다.</p>
                        </div>
                        <div class="feature-card">
                            <div class="icon-modern">
                                <i class="fas fa-user-edit" style="color: white; font-size: 1.5rem;"></i>
                            </div>
                            <h3 style="color: #1e293b; font-size: 1.3rem; font-weight: 700; margin-bottom: 1rem;">소개글</h3>
                            <p style="color: #64748b; margin: 0; font-weight: 500;">자기소개서를 통해 저의 장래희망, 관심사, 성격, 비전과 각오를 전하겠습니다.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
elif page == "👨‍🚒 장래희망":
    st.markdown("""
        <div class="card">
            <div style="text-align: center; margin-bottom: 2.5rem;">
                <h1 style="font-size: 3rem; font-weight: bold; color: #2d3748;">장래희망</h1>
                <div style="width: 6rem; height: 0.25rem; background: linear-gradient(to right, #ef4444, #f97316); margin: 0 auto; border-radius: 9999px;"></div>
                <p style="font-size: 1.25rem; color: #4b5563; margin-top: 1rem; font-weight: 1;">소방공무원의 꿈</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class="card-hover" style="background: linear-gradient(to right, #fef2f2, #fff7ed); padding: 1.5rem; border-radius: 1rem; margin-bottom: 1rem;">
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <div class="fire-glow" style="width: 3rem; height: 3rem; background: #ef4444; border-radius: 9999px; display: flex; align-items: center; justify-content: center; margin-right: 1rem;">
                        <i class="fas fa-fire" style="color: white; font-size: 1.25rem;"></i>
                    </div>
                    <h3 style="font-size: 1.5rem; font-weight: bold; color: #2d3748;">나의 꿈</h3>
                </div>
                <p style="color: #4b5563; font-size: 1.125rem; line-height: 1.75;">
                    위기의 순간, 누군가의 생명을 지키는 <span style="font-weight: 600; color: #ef4444;">소방관이</span> 되어서<br>
                    숭고한 사명을 실현하고 싶습니다.
                </p>
            </div>

            <div class="card-hover" style="background: linear-gradient(to right, #eff6ff, #ecfeff); padding: 1.5rem; border-radius: 1rem; margin-bottom: 1rem;">
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <div style="width: 3rem; height: 3rem; background: #3b82f6; border-radius: 9999px; display: flex; align-items: center; justify-content: center; margin-right: 1rem;">
                        <i class="fas fa-shield-alt" style="color: white; font-size: 1.25rem;"></i>
                    </div>
                    <h3 style="font-size: 1.5rem; font-weight: bold; color: #2d3748;">꿈의 계기</h3>
                </div>
                <p style="color: #4b5563; font-size: 1.125rem; line-height: 1.75;">
                    유튜브 채널 창원소방본부에서 소방관 분들이 두려움을 무릎쓰고 시민의 <span style="font-weight: 600; color: #3b82f6;">생명을 지키는</span> 모습이<br>
                    제 마음 깊은 곳에 각인 되었습니다.
                </p>
            </div>

            <div class="card-hover" style="background: linear-gradient(to right, #ecfdf5, #d1fae5); padding: 1.5rem; border-radius: 1rem;">
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <div style="width: 3rem; height: 3rem; background: #10b981; border-radius: 9999px; display: flex; align-items: center; justify-content: center; margin-right: 1rem;">
                        <i class="fas fa-hands-helping" style="color: white; font-size: 1.25rem;"></i>
                    </div>
                    <h3 style="font-size: 1.5rem; font-weight: bold; color: #2d3748;">꿈의 이유</h3>
                </div>
                <p style="color: #4b5563; font-size: 1.125rem; line-height: 1.75;">
                    누군가의 도움이 절실한 순간, 가장 먼저<br>
                    <span style="font-weight: 600; color: #10b981;">손을 내미는</span> 사람이 되고싶습니다.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="display: flex; flex-direction: column; align-items: center;">
                <div style="position: relative; margin-bottom: 2rem;">
                    <div class="icon-bounce" style="width: 16rem; height: 16rem; background: linear-gradient(135deg, #ef4444, #f97316); border-radius: 9999px; display: flex; align-items: center; justify-content: center; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                        <i class="fas fa-fire-extinguisher" style="color: white; font-size: 6rem;"></i>
                    </div>
                    <div style="position: absolute; top: -1.5rem; left: 50%; transform: translateX(-50%); width: 4rem; height: 4rem; background: #eab308; border-radius: 9999px; display: flex; align-items: center; justify-content: center; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                        <i class="fas fa-star" style="color: white; font-size: 1.5rem;"></i>
                    </div>
                    <div style="position: absolute; top: 25%; right: -2rem; width: 3.5rem; height: 3.5rem; background: #3b82f6; border-radius: 9999px; display: flex; align-items: center; justify-content: center; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                        <i class="fas fa-truck" style="color: white; font-size: 1.25rem;"></i>
                    </div>
                    <div style="position: absolute; top: 75%; left: -2rem; width: 3.5rem; height: 3.5rem; background: #10b981; border-radius: 9999px; display: flex; align-items: center; justify-content: center; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                        <i class="fas fa-heartbeat" style="color: white; font-size: 1.25rem;"></i>
                    </div>
                    <div style="position: absolute; bottom: -1.5rem; left: 25%; width: 3rem; height: 3rem; background: #a855f7; border-radius: 9999px; display: flex; align-items: center; justify-content: center; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                        <i class="fas fa-medal" style="color: white; font-size: 1rem;"></i>
                    </div>
                    <div style="position: absolute; bottom: -1.5rem; right: 25%; width: 3rem; height: 3rem; background: #6366f1; border-radius: 9999px; display: flex; align-items: center; justify-content: center; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                        <i class="fas fa-graduation-cap" style="color: white; font-size: 1rem;"></i>
                    </div>
                </div>
                         <div style="text-align: center; background: linear-gradient(to right, #f9fafb, #eff6ff); padding: 1.5rem; border-radius: 1rem; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                            <h4 style="font-size: 1.5rem; font-weight: bold; color: #2d3748; margin-bottom: 0.75rem;">나의 다짐</h4>
                          <p style="font-size: 1rem; color: #4b5563; font-weight: 500; line-height: 1.6;">
                                "언제 어떤 절망적인 상황이 와도<br>시민을 지킬 수 있는 사람이 되겠습니다.<br><br>
                        누군가에게는 전부일 그 순간,<br>제가 그 희망이 되고 싶습니다."
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

elif page == "🎨관심사와 학업현황":
    st.markdown("""
        <div class="main">
            <div class="card">
                <div style="text-align: center; margin-bottom: 2rem;">
                    <h1 style="font-size: 2.5rem; font-weight: bold; color: #2d3748;">관심사와 학업현황</h1>
                    <div style="width: 5rem; height: 0.25rem; background: linear-gradient(to right, #f97316, #ef4444); margin: 0 auto; border-radius: 9999px;"></div>
                    <p style="font-size: 1.125rem; color: #4b5563; margin-top: 0.75rem; font-weight: 500;"></p>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2.5rem; align-items: center;">
                    <div style="space-y: 1.5rem;">
                        <div class="card-hover" style="background: linear-gradient(to right, #eff6ff, #ecfeff); padding: 1.25rem; border-radius: 0.75rem; margin-bottom: 1.5rem;">
                            <div style="display: flex; align-items: center; margin-bottom: 0.75rem;">
                                <div style="width: 2.5rem; height: 2.5rem; background: #3b82f6; border-radius: 9999px; display: flex; align-items: center; justify-content: center; margin-right: 0.75rem;">
                                    <i class="fas fa-dumbbell icon-pulse" style="color: white; font-size: 1rem;"></i>
                                </div>
                                <h3 style="font-size: 1.25rem; font-weight: bold; color: #2d3748;">체력 운동</h3>
                            </div>
                            <p style="color: #4b5563; line-height: 1.75;">
                                주 5회 근력 운동과 유산소로<br>
                                <span style="font-weight: 600; color: #3b82f6;">체력시험 대비</span> 훈련
                            </p>
                            <div style="margin-top: 0.75rem; background: #e5e7eb; border-radius: 9999px; height: 0.5rem;">
                                <div class="progress-bar" style="background: #3b82f6; height: 0.5rem; border-radius: 9999px; width: 85%;"></div>
                            </div>
                        </div>
                        <div class="card-hover" style="background: linear-gradient(to right, #fef2f2, #fce7f3); padding: 1.25rem; border-radius: 0.75rem; margin-bottom: 1.5rem;">
                            <div style="display: flex; align-items: center; margin-bottom: 0.75rem;">
                                <div style="width: 2.5rem; height: 2.5rem; background: #ef4444; border-radius: 9999px; display: flex; align-items: center; justify-content: center; margin-right: 0.75rem;">
                                    <i class="fas fa-fire-extinguisher icon-pulse" style="color: white; font-size: 1rem;"></i>
                                </div>
                                <h3 style="font-size: 1.25rem; font-weight: bold; color: #2d3748;">주요 전공 과목
                            </div>
                            <p style="color: #4b5563; line-height: 1.75;">
                                소방안전관리론, 소방학개론, 소방관계법규,<br>
                                <span style="font-weight: 600; color: #ef4444;">소방법규</span> 등 실무 중심 학습
                            </p>
                            <div style="margin-top: 0.75rem; background: #e5e7eb; border-radius: 9999px; height: 0.5rem;">
                                <div class="progress-bar" style="background: #ef4444; height: 0.5rem; border-radius: 9999px; width: 75%;"></div>
                            </div>
                        </div>
                        <div class="card-hover" style="background: linear-gradient(to right, #ecfdf5, #d1fae5); padding: 1.25rem; border-radius: 0.75rem; margin-bottom: 1.5rem;">
                            <div style="display: flex; align-items: center; margin-bottom: 0.75rem;">
                                <div style="width: 2.5rem; height: 2.5rem; background: #10b981; border-radius: 9999px; display: flex; align-items: center; justify-content: center; margin-right: 0.75rem;">
                                    <i class="fab fa-python icon-pulse" style="color: white; font-size: 1rem;"></i>
                                </div>
                                <h3 style="font-size: 1.25rem; font-weight: bold; color: #2d3748;">Python 프로그래밍</h3>
                            </div>
                            <p style="color: #4b5563; line-height: 1.75;">
                                개인적 관심사로<br>
                                <span style="font-weight: 600; color: #10b981;">Python 언어</span> 학습 및 활용
                            </p>
                            <div style="margin-top: 0.75rem; background: #e5e7eb; border-radius: 9999px; height: 0.5rem;">
                                <div class="progress-bar" style="background: #10b981; height: 0.5rem; border-radius: 9999px; width: 60%;"></div>
                            </div>
                        </div>
                        <div class="card-hover" style="background: linear-gradient(to right, #fef3c7, #fde68a); padding: 1.25rem; border-radius: 0.75rem;">
                            <div style="display: flex; align-items: center; margin-bottom: 0.75rem;">
                                <div style="width: 2.5rem; height: 2.5rem; background: #f59e0b; border-radius: 9999px; display: flex; align-items: center; justify-content: center; margin-right: 0.75rem;">
                                    <i class="fas fa-certificate icon-pulse" style="color: white; font-size: 1rem;"></i>
                                </div>
                                <h3 style="font-size: 1.25rem; font-weight: bold; color: #2d3748;">자격증 준비</h3>
                            </div>
                            <p style="color: #4b5563; line-height: 1.75;">
                                위험물 산업기사,<br>
                                <span style="font-weight: 600; color: #f59e0b;">소방설비기사(전기)</span> 등 준비 중
                            </p>
                            <div style="margin-top: 0.75rem; background: #e5e7eb; border-radius: 9999px; height: 0.5rem;">
                                <div class="progress-bar" style="background: #f59e0b; height: 0.5rem; border-radius: 9999px; width: 70%;"></div>
                            </div>
                        </div>
                    </div>
                    <div style="display: flex; flex-direction: column; align-items: center;">
                        <div style="position: relative; margin-bottom: 1.5rem;">
                            <div style="width: 12rem; height: 12rem; background: linear-gradient(135deg, #f97316, #ef4444); border-radius: 9999px; display: flex; align-items: center; justify-content: center; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                                <i class="fas fa-fire" style="color: white; font-size: 4rem;"></i>
                            </div>
                            <div style="position: absolute; top: -1rem; left: 50%; transform: translateX(-50%); width: 3rem; height: 3rem; background: #3b82f6; border-radius: 9999px; display: flex; align-items: center; justify-content: center; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                                <i class="fas fa-dumbbell" style="color: white; font-size: 1rem;"></i>
                            </div>
                            <div style="position: absolute; top: 25%; right: -1.5rem; width: 3rem; height: 3rem; background: #ef4444; border-radius: 9999px; display: flex; align-items: center; justify-content: center; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                                <i class="fas fa-fire-extinguisher" style="color: white; font-size: 1rem;"></i>
                            </div>
                            <div style="position: absolute; top: 75%; left: -1.5rem; width: 3rem; height: 3rem; background: #10b981; border-radius: 9999px; display: flex; align-items: center; justify-content: center; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                                <i class="fab fa-python" style="color: white; font-size: 1rem;"></i>
                            </div>
                            <div style="position: absolute; bottom: -1rem; left: 25%; width: 2.5rem; height: 2.5rem; background: #f59e0b; border-radius: 9999px; display: flex; align-items: center; justify-content: center; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                                <i class="fas fa-certificate" style="color: white; font-size: 0.75rem;"></i>
                            </div>
                            <div style="position: absolute; bottom: -1rem; right: 25%; width: 2.5rem; height: 2.5rem; background: #a855f7; border-radius: 9999px; display: flex; align-items: center; justify-content: center; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                                <i class="fas fa-graduation-cap" style="color: white; font-size: 0.75rem;"></i>
                            </div>
                        </div>
                        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; width: 100%;">
                            <div style="text-align: center; background: #eff6ff; padding: 0.75rem; border-radius: 0.5rem;">
                                <div style="font-size: 1.5rem; font-weight: bold; color: #3b82f6;">주5회</div>
                                <div style="font-size: 0.875rem; color: #4b5563;">운동</div>
                            </div>
                            <div style="text-align: center; background: #fef2f2; padding: 0.75rem; border-radius: 0.5rem;">
                                <div style="font-size: 1.5rem; font-weight: bold; color: #ef4444;">4과목</div>
                                <div style="font-size: 0.875rem; color: #4b5563;">소방학습</div>
                            </div>
                            <div style="text-align: center; background: #ecfdf5; padding: 0.75rem; border-radius: 0.5rem;">
                                <div style="font-size: 1.5rem; font-weight: bold; color: #10b981;">3학년</div>
                                <div style="font-size: 0.875rem; color: #4b5563;">재학중</div>
                            </div>
                        </div>
                        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; width: 100%; margin-top: 1rem;">
                            <div style="text-align: center; background: #fef3c7; padding: 0.75rem; border-radius: 0.5rem;">
                                <div style="font-size: 1.25rem; font-weight: bold; color: #f59e0b;">Python</div>
                                <div style="font-size: 0.875rem; color: #4b5563;">관심분야</div>
                            </div>
                            <div style="text-align: center; background: #f3e8ff; padding: 0.75rem; border-radius: 0.5rem;">
                                <div style="font-size: 1.25rem; font-weight: bold; color: #a855f7;">2개</div>
                                <div style="font-size: 0.875rem; color: #4b5563;">자격증</div>
                            </div>
                        </div>
                        <div style="text-align: center; margin-top: 1rem; background: linear-gradient(to right, #f9fafb, #ffedd5); padding: 1rem; border-radius: 0.75rem;">
                            <p style="font-size: 1.125rem; color: #4b5563; font-weight: 500;">
                                "꾸준한 노력으로 <span style="color: #f97316; font-weight: bold;">완벽한 준비</span>"
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


elif page == "🕵️ 성격과 강점":
  st.markdown("""
        <div class="main">
            <div class="card">
                <div style="text-align: center; margin-bottom: 2rem;">
                    <h1 style="font-size: 2.5rem; font-weight: bold; color: #2d3748;">성격과 강점</h1>
                    <div style="width: 5rem; height: 0.25rem; background: linear-gradient(to right, #a855f7, #6366f1); margin: 0 auto; border-radius: 9999px;"></div>
                    <p style="font-size: 1.125rem; color: #4b5563; margin-top: 0.75rem; font-weight: 500;"></p>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
                    <div class="card-hover" style="background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(255,255,255,0.7)); padding: 1.5rem; border-radius: 1rem; border: 1px solid rgba(255,255,255,0.2);">
                        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                            <div class="icon-pulse" style="width: 3.5rem; height: 3.5rem; background: linear-gradient(135deg, #ef4444, #f472b6); border-radius: 9999px; display: flex; align-items: center; justify-content: center; margin-right: 1rem;">
                                <i class="fas fa-shield-alt" style="color: white; font-size: 1.5rem;"></i>
                            </div>
                            <div>
                                <h3 style="font-size: 1.5rem; font-weight: bold; color: #2d3748;">책임감</h3>
                                <p style="font-size: 0.875rem; color: #4b5563;">Responsibility</p>
                            </div>
                        </div>
                        <p style="color: #4b5563; font-size: 1.125rem; line-height: 1.75;">
                            맡은 일에 대해 <span style="font-weight: 600; color: #ef4444;">끝까지 책임</span>지는 자세로<br>
                            신뢰받는 사람이 되고자 합니다
                        </p>
                        <div style="margin-top: 1rem; display: flex; gap: 0.5rem;">
                            <span style="padding: 0.25rem 0.75rem; background: #fee2e2; color: #dc2626; border-radius: 9999px; font-size: 0.875rem; font-weight: 500;">신뢰성</span>
                            <span style="padding: 0.25rem 0.75rem; background: #fce7f3; color: #db2777; border-radius: 9999px; font-size: 0.875rem; font-weight: 500;">완수력</span>
                        </div>
                    </div>
                    <div class="card-hover" style="background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(255,255,255,0.7)); padding: 1.5rem; border-radius: 1rem; border: 1px solid rgba(255,255,255,0.2);">
                        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                            <div class="icon-pulse" style="width: 3.5rem; height: 3.5rem; background: linear-gradient(135deg, #3b82f6, #06b6d4); border-radius: 9999px; display: flex; align-items: center; justify-content: center; margin-right: 1rem;">
                                <i class="fas fa-search" style="color: white; font-size: 1.5rem;"></i>
                            </div>
                            <div>
                                <h3 style="font-size: 1.5rem; font-weight: bold; color: #2d3748;">탐구심</h3>
                                <p style="font-size: 0.875rem; color: #4b5563;">Curiosity</p>
                            </div>
                        </div>
                        <p style="color: #4b5563; font-size: 1.125rem; line-height: 1.75;">
                            새로운 것에 대한 <span style="font-weight: 600; color: #3b82f6;">끊임없는 탐구심</span>으로<br>
                            계속해서 성장하고 발전합니다
                        </p>
                        <div style="margin-top: 1rem; display: flex; gap: 0.5rem;">
                            <span style="padding: 0.25rem 0.75rem; background: #dbeafe; color: #2563eb; border-radius: 9999px; font-size: 0.875rem; font-weight: 500;">탐구력</span>
                            <span style="padding: 0.25rem 0.75rem; background: #cffafe; color: #0891b2; border-radius: 9999px; font-size: 0.875rem; font-weight: 500;">학습욕</span>
                        </div>
                    </div>
                    <div class="card-hover" style="background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(255,255,255,0.7)); padding: 1.5rem; border-radius: 1rem; border: 1px solid rgba(255,255,255,0.2);">
                        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                            <div class="icon-pulse" style="width: 3.5rem; height: 3.5rem; background: linear-gradient(135deg, #10b981, #047857); border-radius: 9999px; display: flex; align-items: center; justify-content: center; margin-right: 1rem;">
                                <i class="fas fa-tools" style="color: white; font-size: 1.5rem;"></i>
                            </div>
                            <div>
                                <h3 style="font-size: 1.5rem; font-weight: bold; color: #2d3748;">실용성</h3>
                                <p style="font-size: 0.875rem; color: #4b5563;">Practicality</p>
                            </div>
                        </div>
                        <p style="color: #4b5563; font-size: 1.125rem; line-height: 1.75;">
                            현실적이고 <span style="font-weight: 600; color: #10b981;">효율적인 해결책</span>을 찾아<br>
                            실질적인 결과를 만들어냅니다
                        </p>
                        <div style="margin-top: 1rem; display: flex; gap: 0.5rem;">
                            <span style="padding: 0.25rem 0.75rem; background: #d1fae5; color: #059669; border-radius: 9999px; font-size: 0.875rem; font-weight: 500;">효율성</span>
                            <span style="padding: 0.25rem 0.75rem; background: #a7f3d0; color: #047857; border-radius: 9999px; font-size: 0.875rem; font-weight: 500;">현실감</span>
                        </div>
                    </div>
                    <div class="card-hover" style="background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(255,255,255,0.7)); padding: 1.5rem; border-radius: 1rem; border: 1px solid rgba(255,255,255,0.2);">
                        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                            <div class="icon-pulse" style="width: 3.5rem; height: 3.5rem; background: linear-gradient(135deg, #f97316, #eab308); border-radius: 9999px; display: flex; align-items: center; justify-content: center; margin-right: 1rem;">
                                <i class="fas fa-rocket" style="color: white; font-size: 1.5rem;"></i>
                            </div>
                            <div>
                                <h3 style="font-size: 1.5rem; font-weight: bold; color: #2d3748;">행동력</h3>
                                <p style="font-size: 0.875rem; color: #4b5563;">Action</p>
                            </div>
                        </div>
                        <p style="color: #4b5563; font-size: 1.125rem; line-height: 1.75;">
                            생각보다는 <span style="font-weight: 600; color: #f97316;">실행을 우선</span>하며<br>
                            자신감 있게 도전하고 실천합니다
                        </p>
                        <div style="margin-top: 1rem; display: flex; gap: 0.5rem;">
                            <span style="padding: 0.25rem 0.75rem; background: #ffedd5; color: #ea580c; border-radius: 9999px; font-size: 0.875rem; font-weight: 500;">추진력</span>
                            <span style="padding: 0.25rem 0.75rem; background: #fef9c3; color: #ca8a04; border-radius: 9999px; font-size: 0.875rem; font-weight: 500;">자신감</span>
                        </div>
                    </div>
                </div>
                <div style="text-align: center; margin-top: 2rem; background: linear-gradient(to right, #f9fafb, #f3e8ff); padding: 1.5rem; border-radius: 1rem;">
                    <h4 style="font-size: 1.5rem; font-weight: bold; color: #2d3748; margin-bottom: 0.5rem;">나의 강점 조합</h4>
                    <p style="font-size: 1.125rem; color: #4b5563; font-weight: 500;">
                        <span style="color: #ef4444;">책임감</span> + <span style="color: #3b82f6;">탐구심</span> + <span style="color: #10b981;">실용성</span> + <span style="color: #f97316;">행동력</span> = 
                        <span class="text-gradient" style="font-weight: bold; font-size: 1.25rem;">완벽한 소방관</span>
                    </p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

elif page == "🧾비전과 각오":
     st.markdown("""
        <div class="main">
            <div class="card">
                <div style="text-align: center; margin-bottom: 1.5rem;">
                    <h1 style="font-size: 2.5rem; font-weight: bold; color: #2d3748;">비전과 각오</h1>
                    <div style="width: 5rem; height: 0.25rem; background: linear-gradient(to right, #ef4444, #f97316); margin: 0 auto; border-radius: 9999px;"></div>
                    <p style="font-size: 1.125rem; color: #4b5563; margin-top: 0.75rem; font-weight: 500;"></p>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 2rem; align-items: center;">
                    <div style="space-y: 1rem;">
                        <div class="card-hover" style="background: linear-gradient(135deg, #eff6ff, #ecfeff); padding: 1.25rem; border-radius: 0.75rem;">
                            <div style="display: flex; align-items: center; margin-bottom: 0.75rem;">
                                <div style="width: 2.5rem; height: 2.5rem; background: #3b82f6; border-radius: 9999px; display: flex; align-items: center; justify-content: center; margin-right: 0.75rem;">
                                    <i class="fas fa-calendar-alt" style="color: white;"></i>
                                </div>
                                <h3 style="font-size: 1.125rem; font-weight: bold; color: #2d3748;">단기 목표</h3>
                            </div>
                            <ul style="color: #4b5563; font-size: 0.875rem; space-y: 0.5rem;">
                                <li>• 소방 관련 자격증 취득</li>
                                <li>• 대학교 졸업</li>
                                <li>• 소방공무원 시험 준비</li>
                                <li>• 소방공무원 합격 </li>
                            </ul>
                        </div>
                        <div class="card-hover" style="background: linear-gradient(135deg, #ecfdf5, #d1fae5); padding: 1.25rem; border-radius: 0.75rem;">
                            <div style="display: flex; align-items: center; margin-bottom: 0.75rem;">
                                <div style="width: 2.5rem; height: 2.5rem; background: #10b981; border-radius: 9999px; display: flex; align-items: center; justify-content: center; margin-right: 0.75rem;">
                                    <i class="fas fa-chart-line" style="color: white;"></i>
                                </div>
                                <h3 style="font-size: 1.125rem; font-weight: bold; color: #2d3748;">장기 비전</h3>
                            </div>
                            <ul style="color: #4b5563; font-size: 0.875rem; space-y: 0.5rem;">
                                <li>• 전문 소방관 되기</li>
                                <li>• 구조 전문가 양성</li>
                                <li>• 소방 안전 교육</li>
                                <li>• 지역 사회 도움</li>
                            </ul>
                        </div>
                    </div>
                    <div style="display: flex; flex-direction: column; align-items: center;">
                        <div style="position: relative;">
                            <div class="flame-animation" style="width: 10rem; height: 10rem; background: linear-gradient(135deg, #ef4444, #f97316); border-radius: 9999px; display: flex; align-items: center; justify-content: center; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                                <i class="fas fa-fire" style="color: white; font-size: 3rem;"></i>
                            </div>
                            <div class="pulse-dot" style="position: absolute; top: -0.75rem; left: 50%; transform: translateX(-50%); width: 2rem; height: 2rem; background: #3b82f6; border-radius: 9999px; display: flex; align-items: center; justify-content: center; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                                <i class="fas fa-star" style="color: white; font-size: 0.75rem;"></i>
                            </div>
                            <div class="pulse-dot" style="position: absolute; top: 25%; right: -1rem; width: 2rem; height: 2rem; background: #10b981; border-radius: 9999px; display: flex; align-items: center; justify-content: center; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                                <i class="fas fa-heart" style="color: white; font-size: 0.75rem;"></i>
                            </div>
                            <div class="pulse-dot" style="position: absolute; top: 75%; left: -1rem; width: 2rem; height: 2rem; background: #a855f7; border-radius: 9999px; display: flex; align-items: center; justify-content: center; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                                <i class="fas fa-shield-alt" style="color: white; font-size: 0.75rem;"></i>
                            </div>
                            <div class="pulse-dot" style="position: absolute; bottom: -0.75rem; left: 33%; width: 1.5rem; height: 1.5rem; background: #eab308; border-radius: 9999px; display: flex; align-items: center; justify-content: center; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                                <i class="fas fa-trophy" style="color: white; font-size: 0.75rem;"></i>
                            </div>
                            <div class="pulse-dot" style="position: absolute; bottom: -0.75rem; right: 33%; width: 1.5rem; height: 1.5rem; background: #ec4899; border-radius: 9999px; display: flex; align-items: center; justify-content: center; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                                <i class="fas fa-medal" style="color: white; font-size: 0.75rem;"></i>
                            </div>
                        </div>
                        <div style="text-align: center; margin-top: 1rem;">
                            <p class="text-gradient" style="font-size: 1.125rem; font-weight: 600;">
                            </p>
                        </div>
                    </div>
                    <div style="space-y: 1rem;">
                        <div class="card-hover" style="background: linear-gradient(135deg, #fef2f2, #fce7f3); padding: 1.25rem; border-radius: 0.75rem;">
                            <div style="display: flex; align-items: center; margin-bottom: 0.75rem;">
                                <div style="width: 2.5rem; height: 2.5rem; background: #ef4444; border-radius: 9999px; display: flex; align-items: center; justify-content: center; margin-right: 0.75rem;">
                                    <i class="fas fa-fist-raised" style="color: white;"></i>
                                </div>
                                <h3 style="font-size: 1.125rem; font-weight: bold; color: #2d3748;">나의 각오</h3>
                            </div>
                            <p style="color: #4b5563; font-size: 0.875rem; line-height: 1.75;">
                                "위험한 상황에서도 <span style="font-weight: 600; color: #ef4444;">냉정함을 잃지 않고</span>, 
                                시민의 안전을 최우선으로 생각하는 소방관이 될것입니다."
                            </p>
                        </div>
                        <div class="card-hover" style="background: linear-gradient(135deg, #ffedd5, #fef9c3); padding: 1.25rem; border-radius: 0.75rem;">
                            <div style="display: flex; align-items: center; margin-bottom: 0.75rem;">
                                <div style="width: 2.5rem; height: 2.5rem; background: #f97316; border-radius: 9999px; display: flex; align-items: center; justify-content: center; margin-right: 0.75rem;">
                                    <i class="fas fa-handshake" style="color: white;"></i>
                                </div>
                                <h3 style="font-size: 1.125rem; font-weight: bold; color: #2d3748;">나와의 약속</h3>
                            </div>
                            <p style="color: #4b5563; font-size: 0.875rem; line-height: 1.75;">
                                "지금의 <span style="font-weight: 600; color: #f97316;">노력과 준비</span>를 바탕으로 
                                사회에 꼭 필요한 인재가 되어 보답하겠습니다."
                            </p>
                        </div>
                    </div>
                </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)