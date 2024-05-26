#!/usr/bin/python3
import subprocess
import platform
import os
import sysconfig
import argparse
import webbrowser


REPORT_PDF_PATH = os.path.join(os.getcwd(), 'src', 'report.pdf')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--open',
                        action="store_true",
                        required=False,
                        default=False,
                        help='Open report.pdf after successfull compilation')
    FLAGS = parser.parse_args()

    system = platform.system()

    compile_cmd = 'make -j4 -C "src" all'

    clean_cmd = 'make -C "src" clean'
    
    docker_platform_flag = '--platform linux/amd64' if sysconfig.get_platform().split("-")[-1].lower() == 'arm64' else ''
    run_docker_cmd = f'docker run {docker_platform_flag} -i --rm -v "{os.getcwd()}:/test" -w /test ajiob/docker-xelatex-fonts:1.2.1'

    shell_and_symbol = ";" if system == "Windows" else "&&"

    cmd = " ".join([run_docker_cmd, compile_cmd, shell_and_symbol, clean_cmd])

    print(f"Running command:\n{cmd}")

    compilation_exit_code = subprocess.run(cmd, shell=True).returncode

    if compilation_exit_code == 0 and FLAGS.open:
        webbrowser.open_new(rf'file://{REPORT_PDF_PATH}')

if __name__=="__main__":
    main()
