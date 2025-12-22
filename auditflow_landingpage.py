import http.server
import socketserver

# ---------------------------------------------------------
# 설정 영역
# ---------------------------------------------------------
LOGO_FILE = "auditflow_logo.png"  
FORM_ID = "1FAIpQLSdaceSg7sSHIbFXH9JLB06xQ5go0Kh-vubLm4E7xXt48kYX-w"
PORT = 9000
# ---------------------------------------------------------

html_content = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AuditFlow | AI 자율 감사 플랫폼</title>
    <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --audit-blue: #0A192F;
            --innovation-gold: #D4AF37;
            --bg-white: #FFFFFF;
            --bg-light: #F9FAFB;
            --text-main: #1F2937;
            --text-muted: #6B7280;
            --border: #E5E7EB;
        }}
        body {{ font-family: 'Pretendard', sans-serif; margin: 0; line-height: 1.7; color: var(--text-main); background-color: var(--bg-white); scroll-behavior: smooth; }}
        .container {{ max-width: 1100px; margin: 0 auto; padding: 0 24px; }}
        
        nav {{ 
            padding: 10px 0; display: flex; justify-content: space-between; align-items: center; 
            border-bottom: 1px solid var(--border); position: sticky; top: 0; 
            background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(10px); z-index: 1000; 
        }}

        /* 로고 크기 조정을 완료했습니다 */
        .logo-img {{ 
            height: 100px;      /* 기존 50px에서 100px로 과감하게 키웠습니다. 너무 크면 80으로 줄이세요. */
            width: auto; 
            display: block; 
            padding: 10px 0;
        }}
        
        .hero {{ padding: 100px 0; text-align: center; background: linear-gradient(to bottom, var(--bg-light), #fff); }}
        .hero h1 {{ font-size: 3.2rem; font-weight: 800; color: var(--audit-blue); margin-bottom: 24px; line-height: 1.2; letter-spacing: -1px; }}
        .hero h1 span {{ color: var(--innovation-gold); }}
        .hero p.mission {{ font-size: 1.2rem; color: var(--text-muted); margin-bottom: 40px; }}

        .btn-primary {{ 
            background-color: var(--audit-blue); color: #fff; padding: 16px 32px; 
            text-decoration: none; border-radius: 8px; font-weight: 600; font-size: 1.1rem;
            transition: 0.3s;
        }}
        .btn-primary:hover {{ background-color: #162c4a; }}

        .form-section {{ padding: 100px 0; background-color: #fff; text-align: center; }}
        .form-box {{ margin-top: 50px; background: #fff; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }}
        
        iframe {{ width: 100%; min-height: 900px; border: none; }}
        
        footer {{ padding: 60px 0; text-align: center; border-top: 1px solid var(--border); color: var(--text-muted); font-size: 0.9rem; }}
    </style>
</head>
<body>

<nav>
    <div class="container" style="display:flex; justify-content:space-between; align-items:center; width:100%;">
        <a href="#"><img src="{LOGO_FILE}" alt="AuditFlow Logo" class="logo-img"></a>
        <div style="font-weight: 600; color: var(--audit-blue);">AI가 당신의 전문성을 증명합니다</div>
    </div>
</nav>

<section class="hero">
    <div class="container">
        <h1>10초 만에 끝내는<br>전사적 감사, <span>AuditFlow</span></h1>
        <p class="mission">"모든 감사인이 데이터의 사각지대 없이 리스크를 완벽하게 통제하도록 돕는다."</p>
        <a href="#apply" class="btn-primary">무료 구축 서비스 신청하기</a>
    </div>
</section>

<section id="apply" class="form-section">
    <div class="container">
        <h2>무료 구축 서비스 파트너 모집</h2>
        <p>AuditFlow와 함께 리스크 관리의 표준을 세울 기업을 찾습니다.</p>
        <div class="form-box">
            <iframe src="https://docs.google.com/forms/d/e/{FORM_ID}/viewform?embedded=true">로드 중…</iframe>
        </div>
    </div>
</section>

<footer>
    <p>© 2025 AuditFlow. Navigate Risks with AI. | insightrix1004@gmail.com</p>
</footer>

</body>
</html>
"""

# 파일 저장
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# 서버 실행
try:
    with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
        print(f"✅ 인사이트릭스 AuditFlow 서버 실행 중: http://localhost:{PORT}")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n서버를 종료합니다.")
