from django.http import JsonResponse

def projects(request):
    return JsonResponse({"projects": [{"id": 1, "title": "Sample"}]})