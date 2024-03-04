import argparse
import importlib
import sys
from contextlib import contextmanager

import mypy.api

@contextmanager
def reimport_argparse():
    imported_argparse = sys.modules.get('argparse')
    if imported_argparse and hasattr(imported_argparse.ArgumentParser, '_parse_args_patched'):
        importlib.reload(argparse)
    yield

def test_typing():
    with reimport_argparse():
        out, err, exit_code = mypy.api.run(['--config-file', 'pyproject.toml'])
        sys.stdout.write(out)
        sys.stderr.write(err)
        assert 0 == exit_code, out
