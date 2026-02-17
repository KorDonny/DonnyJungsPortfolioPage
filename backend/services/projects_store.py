def get_projects_payload() -> dict:
    return {
        "projects": [
            {
                "id": 1,
                "title": "Portfolio Website",
                "summary": "Next.js + S3/CloudFront + Django(App Runner) 구축",
                "tags": ["Next.js", "AWS", "CloudFront", "Django"],
                "url": "https://www.donnyjungsweb.dedyn.io",
                "source": "https://github.com/KorDonny/DonnyJungsPortfolioPage",
            },
            {
                "id": 2,
                "title": "Network Monitoring Concept",
                "summary": "중앙 서버에서 매장 PC 연결상태 모니터링 설계",
                "tags": ["Network", "Monitoring", "SQL"],
                "url": "",
                "source": "",
            },
        ]
    }
