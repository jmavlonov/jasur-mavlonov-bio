from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMessage
from threading import Thread
from django.http import JsonResponse
import resend
import os 
from blog.models import Portfolio
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


resend.api_key = os.getenv("RESEND_API_KEY")


def index(request):
    portfolios = Portfolio.objects.all().order_by('-created_at')
    return render(request, 'blog/index.html', {'portfolios': portfolios})


# def portfolio_list(request):
#     portfolios = Portfolio.objects.all().order_by('-created_at')
#     return render(request, 'blog/index.html', {'portfolios': portfolios})

def send_email_async(params):
    """Emailni fon jarayonida yuboradi (Resend orqali)"""
    try:
        resend.Emails.send(params)
    except Exception as e:
        print("❌ Email yuborishda xato:", e)

@csrf_exempt
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")  # foydalanuvchi emaili
        message = request.POST.get("message")

        if not name or not email or not message:
            return JsonResponse({"success": False, "message": "❌ Please fill in all required fields."})
        
        subject = f"New message from: {name}"
        html_content = f"""
        <h3>New Contact Message</h3>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Message:</strong><br>{message}</p>
        """
        
        params = {
            "from": "Portfolio Contact <onboarding@resend.dev>",  # or noreply@yourdomain.com
            "to": [settings.DEFAULT_FROM_EMAIL],
            "subject": subject,
            "html": html_content,
            "reply_to": [email],
        }


        
        # Emailni fon jarayonida yuborish
        Thread(target=send_email_async, args=(params,)).start()

        return JsonResponse({"success": True, "message": "✅ Your message has been sent successfully!"})

    return render(request, "blog/index.html")


def custom_404(request, exception):
    return render(request, 'blog/404.html', status=404)