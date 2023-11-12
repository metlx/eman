from git import Repo
import time
import os
import subprocess

def banner():
    print("""
     ____  ____    ____   ____   ___
    / _  )|    \  / _  | / ___) /___)
   ( (/ / | | | |( ( | |( (___ |___ |
    \____)|_|_|_| \_||_| \____)(___/
                        manager eman™
             """)

def doom_install():
    print('installing doom... ')
    url = 'https://github.com/doomemacs/doomemacs'
    path = os.path.expanduser('~/.config/emacs')
    if not os.path.exists(path):
        os.makedirs(path)
    try:
        Repo.clone_from(url, path)
        script = os.path.expanduser('~/.config/emacs/bin/doom')
        subprocess.run(['bash', script] + ['install'], check=True)
    except Exception as e:
        print(f'install failed because: {e}')

def spacemacs_install():
    print('spacemacs is being installed...')
    url = 'https://github.com/syl20bnr/spacemacs'
    path = os.path.expanduser('~/.emacs.d/')
    if not os.path.exists(path):
        os.makedirs(path)
    try:
        Repo.clone_from(url, path)
        subprocess.run(['emacs'] + ['-nw'], check=True)
    except Exception as e:
        print(f'install failed because: {e}')

def nano_isntall():
    print('nano is being installed...')

def old_config_install():
    try:
        config = os.path.expanduser('~/.emacs.d.bak_nice_af')
        des = os.path.expanduser('~/.emacs.d')
        subprocess.run(['cp', config] + ['-r'] + [des], check=True)
        print('old config installed... ')
    except Exception as e:
        print(f'cleaning failed due to: {e}')

def doom_clean():
    try:
        doom_install = os.path.expanduser('~/.config/doom')
        emacs_install = os.path.expanduser('~/.config/emacs')
        subprocess.run(['rm', emacs_install] + ['-rf'], check=True)
        subprocess.run(['rm', doom_install] + ['-rf'], check=True)
        print('doom cleaned...')
    except Exception as e:
        print(f'cleaning failed due to: {e}')

def spacemacs_clean():
    try:
        space_conf = os.path.expanduser('~/.emacs.d')
        spacemacs = os.path.expanduser('~/.spacemacs')
        spacemacsenv = os.path.expanduser('~/.spacemacs.env')
        subprocess.run(['rm', space_conf] + ['-rf'], check=True)
        subprocess.run(['rm', spacemacs] + ['-rf'], check=True)
        subprocess.run(['rm', spacemacsenv] + ['-rf'], check=True)
        print('spacemacs cleaned... ')
    except Exception as e:
        print(f'cleaning failed due to: {e}')

def old_config_clean():
    try:
        old = os.path.expanduser('~/.emacs.d')
        subprocess.run(['rm', old] + ['-rf'], check=True)
        print('old config cleaned... ')
    except Exception as e:
        print(f'cleaning failed due to: {e}')

if __name__ == '__main__':

    banner()

    while True:
        print(' \n install(1) clean(2) exit(3)')
        ans = input('> ')
        if ans == '3':
            break

        elif ans == '1': # install
            print('    \n doom(1) spacemacs(2) nano(3) old(4) back(b)')
            version = input('install> ')
            if version == '1':
                doom_install()
            elif version == '2':
                spacemacs_install()
            elif version == '3':
                nano_isntall()
            elif version == '4':
                old_config_install()
            elif version == 'b':
                continue

        elif ans == '2': # clean
            print('\n doom(1) spacemacs(2) nano(3) old(4) back(b)')
            to_clean = input('clean> ')
            if to_clean == '1':
                doom_clean()
            elif to_clean == '2':
                spacemacs_clean()
            elif to_clean == 'b':
                continue
            elif to_clean == '4':
                old_config_clean()
