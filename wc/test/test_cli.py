import click
from click.testing import CliRunner
from ccwc.cli import main

def test_main_with_c_flag():
    runner = CliRunner()
    result = runner.invoke(main, ['-c', 'test/data/test.txt'])
    assert result.exit_code == 0
    assert result.output.strip() == '342190 test.txt'
