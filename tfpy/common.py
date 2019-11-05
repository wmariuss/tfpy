import re
import os
from typing import List, IO, Union, Any

from termcolor import colored


class Utils(object):
    def __init__(self) -> None:
        pass

    def escape_ansi(self, line: str) -> str:
        ansi_escape = re.compile(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]")
        return ansi_escape.sub("", line)

    def check_file(self, file_name: Union[bytes, str]) -> bool:
        size = os.stat(file_name)

        if os.path.isfile(file_name) and size.st_size > 0:
            return True
        return False

    def message(self, dir: str, err: bool = False, result: str = None):
        if err:
            print(colored("\n=> Found error(s) in {} path.\n".format(dir), "red"))
        else:
            print(colored("\n=> Found change(s) in {} path.\n".format(dir), "green"))
        if result:
            print(result)


class TerraCommon(object):
    def __init__(self) -> None:
        pass

    def commands(self, command: str, version: float = None) -> List[str]:
        cmd_list = []

        if version:
            cmd_list = [
                "tfenv install {}".format(version),
                "tfenv use {}".format(version),
            ]

        if command == "init":
            cmd_list += ["terraform init -reconfigure", "terraform plan -out=result"]
        elif command == "show":
            cmd_list = ["terraform plan -out=result"]
        elif command == "apply":
            cmd_list = ["terraform apply result"]

        return cmd_list
