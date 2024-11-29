from django.shortcuts import render
from django.http import JsonResponse

# Health check endpoint
def health_check(request):
    
    return JsonResponse({"status": "ok"})

# Página de inicio (opcional para personalizar el dominio raíz)
def home(request):
    return JsonResponse({"message": "¡Bienvenido a ClodeFashion API!"})


