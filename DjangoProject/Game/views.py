from django.http import JsonResponse


# Create your views here.
def playGame(request):
    name = request.POST['name']
    return JsonResponse({"name":name})
