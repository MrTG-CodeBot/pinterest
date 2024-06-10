import subprocess

try:
    import google.generativeai as genai
except ImportError:
    print("downloading google-generativeai")
    subprocess.run(["pip", "install", "google-generativeai"])

genai.configure(api_key="AIzaSyAGv5kIu2-E0N9eTdK7lzevl2nr3sOk6is")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
}

model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                              generation_config=generation_config,


prompt_parts = [input("ask a question")
]

response = model.generate_content(prompt_parts)
print(response.text)
