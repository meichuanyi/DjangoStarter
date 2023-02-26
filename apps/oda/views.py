from django.shortcuts import render

# Create your views here.
# 扩展admin主页，美化后台
def extend_admin_home(request):
    return render(request, 'admin/extend_home.html')

def test(request):
    return render(request, "adminlte/example.html")
