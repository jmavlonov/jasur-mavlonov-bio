from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMessage
from threading import Thread
from django.http import JsonResponse

from blog.models import Portfolio
# Create your views here.


def index(request):
    portfolios = Portfolio.objects.all().order_by('-created_at')
    return render(request, 'blog/index.html', {'portfolios': portfolios})


# def portfolio_list(request):
#     portfolios = Portfolio.objects.all().order_by('-created_at')
#     return render(request, 'blog/index.html', {'portfolios': portfolios})


def send_email_async(mail):
    """Emailni fon jarayonida yuboradi"""
    mail.send()
    
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")  # foydalanuvchi emaili
        message = request.POST.get("message")

        subject = f"Yangi murojaat: {name}"
        full_message = f"""
        Ism: {name}
        Email: {email}

        Xabar:
        {message}
        """

        mail = EmailMessage(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            headers={"Reply-To": email},
        )
        if not name or not email or not message:
            return JsonResponse({"success": False, "message": "❌ Please fill in all required fields."})
        
        # Emailni fon jarayonida yuborish
        Thread(target=send_email_async, args=(mail,)).start()

        return JsonResponse({"success": True, "message": "✅ Your message has been sent successfully!"})

    return render(request, "blog/index.html")


def custom_404(request, exception=None):
    return render(request, 'blog/404.html', status=404)