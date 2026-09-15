import inspect
from typing import Any, Callable, Optional
from pygments import highlight  # type: ignore
from pygments.lexers import PythonLexer  # type: ignore
from pygments.formatters import HtmlFormatter  # type: ignore
from IPython.display import display, HTML  # type: ignore
from IPython import get_ipython # type: ignore
import subprocess
import sys


def show_source(function: Callable) -> None:
    code = inspect.getsource(function)
    lexer = PythonLexer()
    formatter = HtmlFormatter(cssclass="pygments")
    html_code = highlight(code, lexer, formatter)
    css = formatter.get_style_defs(".pygments")
    html = f"<style>{css}</style>{html_code}"
    display(HTML(html))  # type: ignore


def hide_traceback(exc_tuple: Optional[Any] = None,
                   filename: Optional[Any] = None,
                   tb_offset: Optional[Any] = None,
                   exception_only: bool = False,
                   running_compiled_code: bool = False) -> Any:
    etype, value, tb = sys.exc_info()
    ipython = get_ipython()  # type: ignore
    exception = ipython.InteractiveTB.get_exception_only(etype, value)
    return ipython._showtraceback(etype,
                                  value,
                                  exception
                                  )

def code_checker(command: str) -> None:
    ipython = get_ipython()  # type: ignore
    ipython.showtraceback = hide_traceback

    result = subprocess.run(command.split(), capture_output=True)
    if result.returncode:
        print()
        raise RuntimeError(
            f"La commande {command} a émis des avertissements:\n\n"
            + result.stdout.decode()
        )
