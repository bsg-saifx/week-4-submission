from dotenv import load_dotenv
import os

load_dotenv()

app_name = os.getenv("APP_NAME")
debug_mode = os.getenv("DEBUG")

print(f"App Name: {app_name}")
print(f"Debug Mode: {debug_mode}")