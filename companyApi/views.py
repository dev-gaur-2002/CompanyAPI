from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("this is home page");
    friends = ["dev", "ujjwal", "shyam", "shivam"];
    return JsonResponse(friends, safe=False);