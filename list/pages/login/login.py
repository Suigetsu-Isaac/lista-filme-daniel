from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from list.models import SkinUser
def login_view(req):
     if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('index')  # Redirecione para a página inicial após o login
        else:
            # Adicione uma mensagem de erro para exibir no template
            error_message = "Credenciais inválidas. Tente novamente."
            return render(req, 'login.html', {'error_message': error_message})
     else:
        return render(req, 'login.html')
    
def cad_view(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        email = req.POST['email']
        
        user = User.objects.filter(username=username).first()
        
        if(user):
            error_message = "Username já cadastrado"
            return render(req, 'cadastro.html', {'error_message': error_message})
            
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        skin = SkinUser.objects.create(usuario = user)
        skin.save()        
        return render(req, 'login.html')
    
    else:
        return render(req, 'cadastro.html')
    
def logout_view(request):
    logout(request)
    return redirect('login')