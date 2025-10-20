from django.core.mail import EmailMessage
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json

def home(request):
    repeat = range(3)
    return render(request, 'portfolio/home.html', {'repeat': repeat})

@csrf_exempt
def contact_form_submit(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    try:
        # Parse and validate incoming JSON
        data = json.loads(request.body)
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()

        if not name or not email or '@' not in email or not message:
            return JsonResponse({'status': 'error', 'message': 'Missing or invalid fields'}, status=400)

        # ✅ Email to Ranganathan with full client details
        owner_email = EmailMessage(
            subject=f"New message from {name}",
            body=(
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Message:\n{message}"
            ),
            from_email=email,
            to=['pranganathan844@gmail.com'],
            reply_to=[email]
        )
        owner_email.send()

        # ✅ Styled HTML confirmation email to client
        html_body = f"""
        <html>
          <body style="font-family: Arial, sans-serif; color: #333;">
            <h2 style="color: #4CAF50;">✅ We received your message!</h2>
            <p>Hi <strong>{name}</strong>,</p>
            <p>Thanks for reaching out to <strong>Ranganathan</strong>!<br>
               Your message has been received and passed along.</p>
            <p>📬 He will contact you shortly.</p>
            <hr>
            <p style="font-size: 0.9em;">
              — Ranganathan<br>
              📍 Chennai, India<br>
              📧 <a href="mailto:pranganathan844@gmail.com">pranganathan844@gmail.com</a>
            </p>
          </body>
        </html>
        """

        confirmation_email = EmailMessage(
            subject='✅ We received your message!',
            body=html_body,
            from_email='pranganathan844@gmail.com',
            to=[email],
            reply_to=['pranganathan844@gmail.com']
        )
        confirmation_email.content_subtype = 'html'
        confirmation_email.send()

        return JsonResponse({'status': 'success'})

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
