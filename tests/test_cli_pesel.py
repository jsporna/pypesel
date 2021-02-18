from pesel.main import cli
import pytest
import random
import time

random.seed(time.time())


@pytest.mark.parametrize('mock', [_ for _ in range(3)])
def test_cli_pesel_generate(monkeypatch, capsys, mock):
    monkeypatch.setattr("sys.argv", ["pesel", "generate"])
    cli()
    out, _ = capsys.readouterr()
    assert len(out.strip()) == 11


@pytest.mark.parametrize("year", [random.randrange(1800, 2299) for _ in range(3)])
def test_cli_pesel_generate_year(monkeypatch, capsys, year):
    monkeypatch.setattr("sys.argv", ["pesel", "generate", "--year", str(year)])
    cli()
    out, _ = capsys.readouterr()
    with pytest.assume:
        assert len(out.strip()) == 11
        assert out[:2] == str(year)[2:]


@pytest.mark.parametrize("month", [random.randrange(1, 12) for _ in range(3)])
def test_cli_pesel_generate_month(monkeypatch, capsys, month):
    monkeypatch.setattr("sys.argv", ["pesel", "generate", "--month", str(month)])
    cli()
    out, _ = capsys.readouterr()
    with pytest.assume:
        assert len(out.strip()) == 11
        assert int(out[2:4]) % 20 == month


@pytest.mark.parametrize("day", [random.randrange(1, 31) for _ in range(3)])
def test_cli_pesel_generate_day(monkeypatch, capsys, day):
    monkeypatch.setattr("sys.argv", ["pesel", "generate", "--day", str(day)])
    cli()
    out, _ = capsys.readouterr()
    with pytest.assume:
        assert len(out.strip()) == 11
        assert int(out[4:6]) == day


@pytest.mark.parametrize("year", [random.randrange(1800, 2299) for _ in range(3)])
@pytest.mark.parametrize("month", [random.randrange(1, 12) for _ in range(3)])
def test_cli_pesel_generate_year_month(monkeypatch, capsys, year, month):
    monkeypatch.setattr("sys.argv", ["pesel", "generate", "--year", str(year), "--month", str(month)])
    cli()
    out, _ = capsys.readouterr()
    with pytest.assume:
        assert len(out.strip()) == 11
        assert out[:2] == str(year)[2:]
        assert int(out[2:4]) % 20 == month


@pytest.mark.parametrize("year", [random.randrange(1800, 2299) for _ in range(3)])
@pytest.mark.parametrize("day", [random.randrange(1, 31) for _ in range(3)])
def test_cli_pesel_generate_year_day(monkeypatch, capsys, year, day):
    monkeypatch.setattr("sys.argv", ["pesel", "generate", "--year", str(year), "--day", str(day)])
    cli()
    out, _ = capsys.readouterr()
    with pytest.assume:
        assert len(out.strip()) == 11
        assert out[:2] == str(year)[2:]
        assert int(out[4:6]) == day


@pytest.mark.parametrize("month", [random.randrange(1, 12) for _ in range(3)])
@pytest.mark.parametrize("day", [random.randrange(1, 28) for _ in range(3)])
def test_cli_pesel_generate_month_day(monkeypatch, capsys, month, day):
    monkeypatch.setattr("sys.argv", ["pesel", "generate", "--month", str(month), "--day", str(day)])
    cli()
    out, _ = capsys.readouterr()
    with pytest.assume:
        assert len(out.strip()) == 11
        assert int(out[2:4]) % 20 == month
        assert int(out[4:6]) == day


@pytest.mark.parametrize("year", [random.randrange(1800, 2299) for _ in range(3)])
@pytest.mark.parametrize("month", [random.randrange(1, 12) for _ in range(3)])
@pytest.mark.parametrize("day", [random.randrange(1, 28) for _ in range(3)])
def test_cli_pesel_generate_year_month_day(monkeypatch, capsys, year, month, day):
    monkeypatch.setattr("sys.argv", ["pesel", "generate", "--year", str(year), "--month", str(month), "--day", str(day)])
    cli()
    out, _ = capsys.readouterr()
    with pytest.assume:
        assert len(out.strip()) == 11
        assert out[:2] == str(year)[2:]
        assert int(out[2:4]) % 20 == month
        assert int(out[4:6]) == day


@pytest.mark.parametrize("male", [random.randint(0, 1) for _ in range(3)])
def test_cli_pesel_generate_male(monkeypatch, capsys, male):
    monkeypatch.setattr("sys.argv", ["pesel", "generate", "--{}male".format("" if male else "fe")])
    cli()
    out, _ = capsys.readouterr()
    with pytest.assume:
        assert len(out.strip()) == 11
        assert int(out[-3]) % 2 == int(male)


@pytest.mark.parametrize("year", [random.randrange(1, 1799) for _ in range(3)])
def test_cli_pesel_generate_incorrect_year(monkeypatch, capsys, year):
    monkeypatch.setattr("sys.argv", ["pesel", "generate", "--year", str(year)])
    with pytest.raises(SystemExit):
        cli()
    _, err = capsys.readouterr()
    assert err != ""


@pytest.mark.parametrize("month", [random.randrange(13, 100) for _ in range(3)])
def test_cli_pesel_generate_incorrect_month(monkeypatch, capsys, month):
    monkeypatch.setattr("sys.argv", ["pesel", "generate", "--month", str(month)])
    with pytest.raises(SystemExit):
        cli()
    _, err = capsys.readouterr()
    assert err != ""


@pytest.mark.parametrize("day", [random.randrange(33, 100) for _ in range(3)])
def test_cli_pesel_generate_incorrect_day(monkeypatch, capsys, day):
    monkeypatch.setattr("sys.argv", ["pesel", "generate", "--day", str(day)])
    with pytest.raises(SystemExit):
        cli()
    _, err = capsys.readouterr()
    assert err != ""


@pytest.mark.parametrize("pesel", ["65432101239"])
def test_cli_pesel_validate_correct_pesel(monkeypatch, capsys, pesel):
    monkeypatch.setattr("sys.argv", ["pesel", "validate", pesel])
    cli()
    out, _ = capsys.readouterr()
    with pytest.assume:
        assert out.strip() == "True"


@pytest.mark.parametrize("pesel", ["65432101238"])
def test_cli_pesel_validate_incorrect_pesel(monkeypatch, capsys, pesel):
    monkeypatch.setattr("sys.argv", ["pesel", "validate", pesel])
    cli()
    out, _ = capsys.readouterr()
    with pytest.assume:
        assert out.strip() == "False"
