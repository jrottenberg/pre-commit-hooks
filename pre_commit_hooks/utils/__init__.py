import subprocess
from typing import Any, Dict, Optional, Tuple

from packaging.version import parse as parseVersion


class CalledProcessError(RuntimeError):
    pass


# abreged version of cmd_output_b
# https://github.com/simplivity/pre-commit/blob/524bdaeb33032d97dc27bbeaa6d89eed9e429834/pre_commit/util.py#L123
def _setdefault_kwargs(kwargs: Dict[str, Any]) -> None:
    for arg in ("stdin", "stdout", "stderr"):
        kwargs.setdefault(arg, subprocess.PIPE)


def cmd_output_b(
    *cmd: str,
    retcode: Optional[int] = 0,
    **kwargs: Any,
) -> Tuple[int, bytes, Optional[bytes]]:
    _setdefault_kwargs(kwargs)

    proc = subprocess.Popen(cmd, **kwargs)
    stdout_b, stderr_b = proc.communicate()
    returncode = proc.returncode

    if retcode is not None and retcode != returncode:
        raise CalledProcessError(returncode, cmd, retcode, stdout_b, stderr_b)

    return returncode, stdout_b, stderr_b


def cmd_output(*cmd: str, **kwargs: Any) -> Tuple[int, str, Optional[str]]:
    returncode, stdout_b, stderr_b = cmd_output_b(*cmd, **kwargs)
    stdout = stdout_b.decode() if stdout_b is not None else None
    stderr = stderr_b.decode() if stderr_b is not None else None
    return returncode, stdout, stderr


def get_all_tags(remote: str) -> list[str]:
    out = []
    _, raw, _ = cmd_output("git", "ls-remote", "--tags", "--refs", remote)

    for line in raw.strip().split("\n"):
        try:
            tag = line.split("/")[-1]
        except AttributeError:
            continue
        out.append(tag)
    return out


def highest_version(all_versions: list[str]) -> str:
    all_versions.sort(key=parseVersion)
    return all_versions[-1]
