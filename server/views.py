from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
def send_value_to_esp(request):
    if request.method == 'POST':
        value = request.POST.get('input')
        print("Value sent to ESP32:", value)
        
        # Create a dictionary and convert it to JSON
        payload = {'value': value}
        json_payload = json.dumps(payload)
        print("JSON Payload:", json_payload)
        
        # Send a POST request to the ESP32 with the JSON payload
        esp32_url = "http://192.168.148.175:80/receive-value"
        
        try:
            response = requests.post(esp32_url, data=json_payload, headers={'Content-Type': 'application/json'})
            if response.status_code == 200:
                return JsonResponse({'message': 'Value sent to ESP32 successfully.'})
            else:
                return JsonResponse({'error': 'Failed to send value to ESP32.'})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)})

    return render(request, 'index.html')
