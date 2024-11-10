import requests

def emotion_detector(text_to_analyze):
    # URL for the Emotion Detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Define headers for the request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Define input JSON for the request
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        # Make a POST request to the Emotion Detection service
        response = requests.post(url, headers=headers, json=input_json)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON and print it for inspection
            response_json = response.json()
            print("Full Response JSON:", response_json)
            
            # Extract the detected text (this part may need adjustment based on response structure)
            detected_text = response_json.get('text', 'No text field found in response.')
            return detected_text
        else:
            print(f"Error: Emotion Detection request failed with status code {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: An exception occurred - {e}")
        return None