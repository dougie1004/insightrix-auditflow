import http.server
import socketserver
import urllib.parse

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------
LOGO_FILE = "auditflow_logo.png" 
DIAGRAM_FILE = "diagram_image.png" 
VIDEO_FILE = "Video Project 1 1.mp4" # 데모 영상 파일명
PORT = 9000
# ---------------------------------------------------------

html_content = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AuditFlow | AI Autonomous Audit Platform</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&family=Pretendard:wght@400;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --audit-blue: #0A192F;
            --innovation-gold: #D4AF37;
            --bg-light: #F8FAFC;
            --text-main: #111827;
            --border: #E2E8F0;
        }}
        body {{ font-family: 'Pretendard', 'Inter', sans-serif; margin: 0; color: var(--text-main); background-color: #fff; line-height: 1.6; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 24px; }}
        
        /* Language Switcher */
        .lang-switch {{ position: fixed; top: 20px; right: 20px; z-index: 2000; background: var(--audit-blue); padding: 5px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.2); }}
        .lang-switch button {{ background: none; border: none; color: #fff; cursor: pointer; padding: 5px 12px; font-weight: bold; opacity: 0.6; transition: 0.3s; }}
        .lang-switch button.active {{ opacity: 1; border-bottom: 2px solid var(--innovation-gold); }}

        /* Navigation - Logo 300px Left */
        nav {{ padding: 10px 0; border-bottom: 1px solid var(--border); position: sticky; top: 0; background: #fff; z-index: 1000; }}
        .logo-img {{ height: 300px; width: auto; display: block; }} 

        /* Hero Split Section - Video Auto Play */
        .hero-section {{ padding: 40px 0; background: var(--bg-light); border-radius: 0 0 40px 40px; }}
        .hero-flex {{ display: flex; align-items: center; gap: 40px; }}
        .hero-content {{ flex: 1; }}
        .hero-video-box {{ flex: 1.2; border-radius: 20px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.15); background: #000; }}
        video {{ width: 100%; display: block; }}
        
        .hero-content h1 {{ font-size: 2.8rem; font-weight: 800; color: var(--audit-blue); margin-bottom: 20px; line-height: 1.2; letter-spacing: -1px; }}
        .hero-content h1 span {{ color: var(--innovation-gold); }}
        .btn-primary {{ display: inline-block; background: var(--audit-blue); color: white; padding: 16px 36px; border-radius: 12px; font-weight: 700; text-decoration: none; transition: 0.3s; }}

        /* Value Cards */
        .value-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; padding: 50px 0; }}
        .value-card {{ padding: 30px; border-radius: 20px; border: 1px solid var(--border); background: #fff; }}
        .value-card h3 {{ color: var(--audit-blue); margin-top: 0; font-size: 1.3rem; margin-bottom: 10px; }}

        /* Diagram Section */
        .diagram-section {{ padding: 60px 0; text-align: center; border-top: 1px solid var(--border); }}
        .diagram-img {{ max-width: 90%; height: auto; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); }}

        /* Form Section */
        .form-section {{ padding: 80px 0; background-color: var(--bg-light); text-align: center; border-radius: 40px 40px 0 0; }}
        .form-box {{ background: white; border-radius: 24px; max-width: 850px; margin: 40px auto; overflow: hidden; box-shadow: 0 15px 35px rgba(0,0,0,0.06); }}
        iframe {{ width: 100%; min-height: 900px; border: none; }}
        
        footer {{ padding: 40px 0; text-align: center; font-size: 0.9rem; color: #94A3B8; border-top: 1px solid var(--border); }}

        @media (max-width: 968px) {{ .hero-flex {{ flex-direction: column; }} .value-grid {{ grid-template-columns: 1fr; }} .logo-img {{ height: 150px; }} }}
    </style>
</head>
<body>

<div class="lang-switch">
    <button id="btn-kr" class="active" onclick="switchLang('kr')">KR</button>
    <button id="btn-en" onclick="switchLang('en')">EN</button>
</div>

<nav>
    <div class="container"><img src="{LOGO_FILE}" alt="AuditFlow Logo" class="logo-img"></div>
</nav>

<section class="hero-section">
    <div class="container hero-flex">
        <div class="hero-content">
            <h1 id="hero-title">당신의 전문성을 증명하는<br><span>1인 감사 시스템</span>, AuditFlow</h1>
            <p id="hero-desc">Gemini 3.0 Pro 기반 차세대 AI 감사 엔진. 2년치 데이터를 10초 만에 통합 분석하여 리스크 사각지대를 완전히 제거합니다.</p>
            <a href="#apply" class="btn-primary" id="btn-apply-text">AuditFlow 구축 희망업체 신청하기</a>
        </div>
        <div class="hero-video-box">
            <video autoplay muted loop playsinline>
                <source src="{urllib.parse.quote(VIDEO_FILE)}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
    </div>
</section>

<div class="container">
    <div class="value-grid">
        <div class="value-card"><h3 id="v1-t">통찰력 (Insight)</h3><p id="v1-d">데이터 간 유기적 관계 분석을 통한 숨겨진 부정 적발</p></div>
        <div class="value-card"><h3 id="v2-t">혁신 (Innovation)</h3><p id="v2-d">대용량 전사 데이터 10초 분석, 업무 90% 단축</p></div>
        <div class="value-card"><h3 id="v3-t">자율성 (Autonomy)</h3><p id="v3-d">AI 스스로 감사 시나리오 자동 생성 및 등록 (ASG)</p></div>
    </div>
</div>

<section class="diagram-section">
    <div class="container">
        <h2 id="diag-title">AuditFlow Process Mining Workflow</h2>
        <img src="{DIAGRAM_FILE}" alt="AuditFlow Workflow Diagram" class="diagram-img">
    </div>
</section>

<section id="apply" class="form-section">
    <div class="container">
        <h2 id="form-title" style="color: var(--audit-blue);">AuditFlow 구축 희망업체 모집</h2>
        <div class="form-box">
            <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdaceSg7sSHIbFXH9JLB06xQ5go0Kh-vubLm4E7xXt48kYX-w/viewform?embedded=true">로드 중…</iframe>
        </div>
    </div>
</section>

<footer id="footer-text">
    "따뜻한 기술이 빚어낸 인생의 품격, 데이터의 진실을 찾는 가장 빠른 길 AuditFlow"
</footer>

<script>
const content = {{
    kr: {{
        heroTitle: "당신의 전문성을 증명하는<br><span>1인 감사 시스템</span>, AuditFlow",
        heroDesc: "Gemini 3.0 Pro 기반 차세대 AI 감사 엔진. 2년치 데이터를 10초 만에 통합 분석하여 리스크 사각지대를 완전히 제거합니다.",
        btnApply: "AuditFlow 구축 희망업체 신청하기",
        v1t: "통찰력 (Insight)", v1d: "데이터 간 유기적 관계 분석을 통한 숨겨진 부정 적발",
        v2t: "혁신 (Innovation)", v2d: "대용량 전사 데이터 10초 분석, 업무 90% 단축",
        v3t: "자율성 (Autonomy)", v3d: "AI 스스로 감사 시나리오 자동 생성 및 등록 (ASG)",
        diagTitle: "AI 프로세스 마이닝 워크플로우",
        formTitle: "AuditFlow 구축 희망업체 모집",
        footer: "따뜻한 기술이 빚어낸 인생의 품격, 데이터의 진실을 찾는 가장 빠른 길 AuditFlow"
    }},
    en: {{
        heroTitle: "Empower Your Expertise with <br><span>Solo Audit System</span>, AuditFlow",
        heroDesc: "Next-gen AI engine based on Gemini 3.0 Pro. Analyze 2 years of data in 10 seconds to eliminate every blind spot.",
        btnApply: "Request AuditFlow Implementation",
        v1t: "Insight", v1d: "Identify hidden fraud patterns through organic data relationship analysis.",
        v2t: "Innovation", v2d: "Process 2 years of enterprise big data in 10 seconds, reducing manual work by 90%.",
        v3t: "Autonomy", v3d: "Self-learning AI automatically generates and registers audit scenarios.",
        diagTitle: "AI-Driven Process Mining Workflow",
        formTitle: "Recruiting Partners for Implementation",
        footer: "Finding the Truth in Data. The fastest path to audit integrity, AuditFlow."
    }}
}};

function switchLang(lang) {{
    document.getElementById('hero-title').innerHTML = content[lang].heroTitle;
    document.getElementById('hero-desc').innerText = content[lang].heroDesc;
    document.getElementById('btn-apply-text').innerText = content[lang].btnApply;
    document.getElementById('v1-t').innerText = content[lang].v1t; document.getElementById('v1-d').innerText = content[lang].v1d;
    document.getElementById('v2-t').innerText = content[lang].v2t; document.getElementById('v2-d').innerText = content[lang].v2d;
    document.getElementById('v3-t').innerText = content[lang].v3t; document.getElementById('v3-d').innerText = content[lang].v3d;
    document.getElementById('diag-title').innerText = content[lang].diagTitle;
    document.getElementById('form-title').innerText = content[lang].formTitle;
    document.getElementById('footer-text').innerText = content[lang].footer;

    document.getElementById('btn-kr').classList.toggle('active', lang === 'kr');
    document.getElementById('btn-en').classList.toggle('active', lang === 'en');
}}
switchLang('kr');
</script>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"🚀 Integrated Multilingual Page Running: http://localhost:{PORT}")

    httpd.serve_forever()
