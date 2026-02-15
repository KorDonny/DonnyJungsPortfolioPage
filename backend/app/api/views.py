from django.http import JsonResponse

def health(request):
    return JsonResponse({"status": "ok"})

def content(request):
    # 나중에 S3의 content.json을 읽거나, 여기서 간단히 응답
    return JsonResponse({
        "message": "hello from django",
        "version": "v1"
    })
