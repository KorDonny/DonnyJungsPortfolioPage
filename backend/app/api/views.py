from django.http import JsonResponse

# 프론트엔드에서 API 호출시 백엔드에서 응답하는 데이터 셋을 스켈레톤으로 구현해 놓은 것
def projects(request):
    data = {
        "projects": [
            {
                "id": 1,
                "title": "Portfolio Website",
                "summary": "Next.js + S3/CloudFront + Django(App Runner) 구축",
                "tags": ["Next.js", "AWS", "CloudFront", "Django"],
                "url": "https://www.donnyjungsweb.dedyn.io",
                "source": "https://github.com/KorDonny/DonnyJungsPortfolioPage"
            },
            {
                "id": 2,
                "title": "Network Monitoring Concept",
                "summary": "중앙 서버에서 매장 PC 연결상태 모니터링 설계",
                "tags": ["Network", "Monitoring", "SQL"],
                "url": "",
                "source": ""
            }
        ]
    }
    return JsonResponse(data)
