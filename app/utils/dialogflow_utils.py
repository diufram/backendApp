from google.cloud import dialogflow_v2 as dialogflow

def process_dialogflow(text):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path("YOUR_PROJECT_ID", "YOUR_SESSION_ID")
    
    text_input = dialogflow.TextInput(text=text, language_code="en")
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(request={"session": session, "query_input": query_input})
    
    return response.query_result.fulfillment_text
