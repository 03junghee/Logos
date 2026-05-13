# mentoring/views.py
from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def instructor(request):
    return render(request, 'instructor.html')

def curriculum(request):
    return render(request, 'curriculum.html')

def reviews(request):
    # Imgur 링크 리스트 등을 여기에 정의
    return render(request, 'reviews.html')

def faq(request):
    return render(request, 'faq.html')

def apply(request):
    return render(request, 'apply.html')