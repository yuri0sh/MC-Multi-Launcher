
from pathlib import Path
from typing import List, TypedDict

from config import DataFile, load_config, DEFAULT_ICON
from env import python_path, run


def build(python_path: str = "python", main_file: str = "src/run.py", icon: str = DEFAULT_ICON, data_files: List[DataFile] = None):
    cmd = [python_path, '-m', 'nuitka', main_file,
           '--assume-yes-for-downloads', '--standalone']
    if Path(icon).exists():
        cmd.append(f"--windows-icon-from-ico={icon}")
    if data_files is not None:
        for data_file in data_files:
            cmd.append(
                f'--include-data-file={data_file["src"]}={data_file["dest"]}')
    # print(f"Running {' '.join(cmd)}")
    run(cmd)


def main():
    config = load_config()
    python = python_path(config.virtual_env)
    build(python, config.main_file, config.icon, config.data_files)


if __name__ == '__main__':
    main()
    # bell
    print('\a')
