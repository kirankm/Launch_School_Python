import subprocess

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
