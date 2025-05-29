import subprocess
import json

def prompt(msg, prefix_space = False):
    if prefix_space:
        print("\n")
    if isinstance(msg, list):
        msg = "\n".join(msg)
    print(f"==> {msg}")

def clear_screen(banner = False):
    subprocess.run('clear', shell=True, check = True)
    if banner:
        banner.display()

def load_json_file(json_file_path):
    with open(json_file_path,'r') as f:
        loaded_file = json.load(f)
    return loaded_file