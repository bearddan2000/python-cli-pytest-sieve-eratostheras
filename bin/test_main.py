import pytest
import main

def test_SieveOfEratosthenes(capsys):
    main.SieveOfEratosthenes(2)
    captured = capsys.readouterr()
    assert captured.out == "2\n"
