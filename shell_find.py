#!/usr/bin/env python3
import os
import sys
import platform

def detect_shell():
    #Returns a tuple of (shell_name, shell_version, shell_path)
    
    # Check common shell environment variables
    shell_path = os.environ.get('SHELL', '')
    if not shell_path:
        shell_path = os.environ.get('ComSpec', '')  # Windows CMD
    
    if os.environ.get('BASH_VERSION'):
        return ('bash', os.environ['BASH_VERSION'], shell_path)
    elif os.environ.get('ZSH_VERSION'):
        return ('zsh', os.environ['ZSH_VERSION'], shell_path)
    elif os.environ.get('FISH_VERSION'):
        return ('fish', os.environ['FISH_VERSION'], shell_path)
    elif os.environ.get('PSModulePath'):
        powershell_edition = os.environ.get('PSEdition', 'Desktop')
        return ('powershell', f"{powershell_edition}", shell_path)
    elif 'CMD.EXE' in (shell_path or '').upper():
        return ('cmd', platform.version(), shell_path)
    
    # Detect from the shell path if it isnt above
    shell_name = os.path.basename(shell_path).lower() if shell_path else 'unknown'
    return (shell_name, 'unknown', shell_path)

def get_shell_info():
    shell_name, shell_version, shell_path = detect_shell()

    return f"{'I am using '} {shell_name} {' on '} {platform.system} {platform.release} {'.'}"
    
    # return {
    #     'shell_name': shell_name,
    #     'shell_version': shell_version,
    #     'shell_path': shell_path,
    #     'os_platform': platform.system(),
    #     'os_release': platform.release(),
    # }