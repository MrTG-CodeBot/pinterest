import subprocess

try:
    import google.generativeai 
except ImportError:
    print("downloading google-generativeai")
    subprocess.run(["pip", "install", "google-generativeai"])
    
import google.generativeai as genai
genai.configure(api_key="AIzaSyAGv5kIu2-E0N9eTdK7lzevl2nr3sOk6is")

user_input = input("ask a question:\n")

if user_input.lower() in ["who is your owner" , "what is your owner name"]:
    print("<^ ~ ^> ᴍʀ.ʙᴏᴛ ᵀᴳ </>\n\ncontact in telegram: https://t.me/MrTG_Coder")

generation_config = {
    "temperature": 0.9 ,
    "top_p": 1 ,
    "top_k": 1 ,
    "max_output_tokens": 2048 ,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT" ,
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    } ,
    {
        "category": "HARM_CATEGORY_HATE_SPEECH" ,
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    } ,
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT" ,
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    } ,
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT" ,
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    } ,
]

model = genai.GenerativeModel(
    model_name="gemini-pro" ,
    generation_config=generation_config ,
    safety_settings=safety_settings
)

prompt_parts = [user_input]
response = model.generate_content(prompt_parts)
print(response)
