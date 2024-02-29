import sys
import mypy.api


def test_typing():
    out, err, exit_code = mypy.api.run(['--config-file', 'pyproject.toml'])
    sys.stdout.write(out)
    sys.stderr.write(err)
    assert 0 == exit_code, out
