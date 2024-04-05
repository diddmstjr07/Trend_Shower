import subprocess
import requests

def reset_tor():
    if reset_tor:
        command = f"brew services restart tor"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout)
        print("ip address changed (engined by tor)")

    else:
        print("tor 프로세스가 실행 중이 아닙니다.")
        command = f"brew services restart tor"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout)
        print("ip address changed (engined by tor)")

def get_current_ip():
    response = requests.get('https://httpbin.org/ip')
    ip_data = response.json()
    return ip_data['origin']