from .models import Ingresso


for i in range(100):
    Ingresso.objects.update_or_create(
        numero=i+1,
        status=0,
        preco=50,
    )