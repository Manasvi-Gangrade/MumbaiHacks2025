import sys

def check_import(module_name, package_name=None):
    if package_name is None:
        package_name = module_name
    try:
        __import__(module_name)
        print(f"[OK] {package_name} imported successfully")
    except ImportError as e:
        print(f"[FAIL] Failed to import {package_name}: {e}")

print("Verifying FactSeeker Dependencies...")
check_import("transformers")
check_import("sentence_transformers")
check_import("faiss", "faiss-cpu")
check_import("langchain")
check_import("fastapi")
check_import("uvicorn")
check_import("streamlit")
check_import("telegram", "python-telegram-bot")
check_import("cv2", "opencv-python")

print("\nVerification Complete.")
