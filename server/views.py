from django.shortcuts import render
from django.http import JsonResponse
import requests

def send_value_to_esp(request):
    if request.method == 'POST':
        value = request.POST.get('input')
        print(value)
        
        # Send a POST request to the ESP32 with the integer value
        esp32_url = "http://192.168.148.175:80/receive-value" # Replace with your ESP32's IP and port
        payload = {'value': value}
        
        try:
            response = requests.post(esp32_url, json=payload)
            if response.status_code == 200:
                return JsonResponse({'message': 'Value sent to ESP32 successfully.'})
            else:
                return JsonResponse({'error': 'Failed to send value to ESP32.'})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)})

    return render(request, 'index.html')
