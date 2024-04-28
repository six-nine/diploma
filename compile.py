#!/usr/bin/python3
import subprocess
import sys, platform
import os
import sysconfig

def main():
    system = platform.system()

    compile_cmd = 'make -j4 -C "src" all'

    clean_cmd = 'make -C "src" clean'
    
    docker_platform_flag = '--platform linux/amd64' if sysconfig.get_platform().split("-")[-1].lower() == 'arm64' else ''
    run_docker_cmd = f'docker run {docker_platform_flag} -i --rm -v "{os.getcwd()}:/test" -w /test ajiob/docker-xelatex-fonts:1.2.1'

    shell_and_symbol = ";" if system == "Windows" else "&&"

    cmd = " ".join([run_docker_cmd, compile_cmd, shell_and_symbol, clean_cmd])

    print(f"Running command:\n{cmd}")

    subprocess.run(cmd, shell=True)

if __name__=="__main__":
    main()
