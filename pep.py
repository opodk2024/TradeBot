import subprocess

print("""
╔════════════════════════════════════════════════╗
║                                                ║
║ 1. Option                                      ║
║ 2. Option                                      ║
║ 3. Option                                      ║
║ 4. Option                                      ║
║ 5. Option                                      ║
║ 6. Option                                      ║
║ 7. Option                                      ║
║ 8. Option                                      ║
║ 9. Option                                      ║
║ 10. Option                                     ║
║                                                ║
╚════════════════════════════════════════════════╝
""")
name = input('1')
if name == '1':
    url = 'https://github.com/ejemplo/repo.git'
    comando = f'git clone {url}'
    subprocess.call(comando, shell=True)









comando = f'git clone {url}'
subprocess.call(comando, shell=True)
