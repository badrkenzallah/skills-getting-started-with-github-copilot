# Simple runner for pytest that prints exit code and summary
import pytest
import sys

args = ['-q', '--maxfail=1']
print('Running pytest with args:', args)
ret = pytest.main(args)
print('pytest return code:', ret)
sys.exit(ret)
