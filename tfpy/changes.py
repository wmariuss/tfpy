import os
import sys
import re
import asyncio
from typing import List, IO, Any, Dict, Union
from subprocrunner import SubprocessRunner, Which

from tfpy.common import TerraCommon
from tfpy.exceptions import TerraformExceptions
from tfpy.common import Utils


class TerraConfigs(object):
    def __init__(self, path: str = ".") -> None:
        self.terraform_exe = Which("terraform")
        self.current_dir = path
        self.terraform_ext = ".tf"
        self.output_dir = ".terraformpy"
        self.output_file = "status.log"
        self.basepath = os.path.realpath(path)
        self.utils = Utils()
        self.tf_common = TerraCommon()

    def dirs(self) -> List[str]:
        dirs_list: List[str] = []
        new_dirs_list: List[str] = []

        for dirname, _, filenames in os.walk(self.current_dir):
            for filename in filenames:
                if filename.endswith(self.terraform_ext):
                    dirs_list.append(os.path.join(dirname))

        for dir in dirs_list:
            if ".terraform" not in dir:
                path = os.path.join(self.basepath, os.path.realpath(dir))
                if path not in new_dirs_list:
                    new_dirs_list.append(
                        os.path.join(self.basepath, os.path.realpath(dir))
                    )

        return new_dirs_list

    def check_exec(self) -> Any:
        if self.terraform_exe.is_exist():
            return True
        else:
            raise TerraformExceptions("Terraform executable not found")

    def save_output(self, content: str, dir_name: str, file_name: IO[bytes]) -> None:
        full_path = os.path.join(dir_name, file_name)

        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)

        if os.path.isfile(full_path):
            os.remove(full_path)

        with open(full_path, "w") as f:
            f.write(self.utils.escape_ansi(content))
        return

    async def execute_cmds(
        self, cmds: List[str], dir: str, show_output: bool = False
    ) -> None:
        if len(cmds) > 0:
            if self.check_exec():
                os.chdir(dir)

                for cmd in cmds:
                    execute_tf = SubprocessRunner(cmd)
                    exec = execute_tf.run()
                    execute_tf.command

                    if exec == 0:
                        out = execute_tf.stdout
                        self.save_output(out, self.output_dir, self.output_file)
                    else:
                        out = execute_tf.stderr
                        self.save_output(out, self.output_dir, self.output_file)
                        raise TerraformExceptions(
                            self.utils.message(dir, err=True, result=out)
                        )
                if show_output:
                    self.utils.message(dir, result=out)
        else:
            raise TerraformExceptions("There are no any commands in the list")
        return

    def version_file(self, dir_name: str, file_name: IO[bytes] = None) -> None:
        if not file_name:
            file_name = ".terraform-version"

        version = re.compile(r"^([0-9]+.[0-9]+.[0-9]+)$")
        foundit = None

        os.chdir(dir_name)

        if os.path.isfile(file_name):
            with open(file_name, "r") as f:
                content = f.readlines()

                for line in content:
                    findit = version.match(line)
                    if findit:
                        foundit = findit.group(1)
        return foundit

    async def check_changes(
        self, dir_name: str, file: Union[bytes], cmds: List[str]
    ) -> Any:
        need_line = re.compile(
            r"^(Plan: (\d+) to add, (\d+) to change, (\d+) to destroy.)$"
        )
        status = {}
        os.chdir(dir_name)

        if self.utils.check_file(file):
            with open(file, "r") as f:
                result = f.readlines()

            for line in result:
                find = need_line.match(line)
                if find:
                    status = {
                        "add": int(find.group(2)),
                        "change": int(find.group(3)),
                        "destroy": int(find.group(4)),
                    }
                    if (
                        status.get("add") >= 1
                        or status.get("change") >= 1
                        or status.get("destroy") >= 1
                    ):
                        await self.execute_cmds(cmds=cmds, dir=dir_name, show_output=True)

    async def terraform_tasks(self, tf_command: str) -> Any:
        dirs = self.dirs()
        status_full_path = os.path.join(self.output_dir, self.output_file)

        for dir in dirs:
            if tf_command == "init":
                version = self.version_file(dir)
                cmds = self.tf_common.commands(command="init")

                if version:
                    cmds = self.tf_common.commands(command="init", version=version)

                asyncio.ensure_future(self.execute_cmds(cmds=cmds, dir=dir))
            if tf_command == "show":
                cmds = self.tf_common.commands(command="show")

                asyncio.ensure_future(
                    self.check_changes(dir_name=dir, file=status_full_path, cmds=cmds)
                )
            elif tf_command == "apply":
                cmds = self.tf_common.commands(command="apply")

                asyncio.ensure_future(
                    self.check_changes(dir_name=dir, file=status_full_path, cmds=cmds)
                )

    def execute_terraform_tasks(self, **options: str) -> Any:
        tf_command = options.get("terraform")

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.terraform_tasks(tf_command=tf_command))
        loop.close()
