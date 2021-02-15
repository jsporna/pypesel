# pypesel

PESEL Python module

PESEL is the national identification number used in Poland since 1979. It always has 11 digits, identifies just one person and cannot be changed to another one (except some specific situations such as gender reassignment).

## Installation

```shell
pip install pesel
```

## Python usage

```python
from pesel import Pesel

random_pesel = Pesel.generate()
random_pesel_male = Pesel.generate(male=True)
random_pesel_2021 = Pesel.generate(year=2021)

pesel = Pesel("65432101239")
```

## Shell usage
There are 2 commands: `generate` & `validate`

```shell
❯ pesel generate --help
usage: pesel generate [-h] [--year YEAR] [--month MONTH] [--day DAY] [--male | --female]

optional arguments:
  -h, --help            show this help message and exit
  --year YEAR, -y YEAR  Year of birth
  --month MONTH, -m MONTH
                        Month of birth
  --day DAY, -d DAY     Day of birth
  --male                It is male person
  --female              It is female person
```

```shell
❯ pesel generate  
62512426682
```

```shell
❯ pesel validate --help  
usage: pesel validate [-h] pesel

positional arguments:
  pesel       PESEL number

optional arguments:
  -h, --help  show this help message and exit
```

```shell
> pesel validate 62512426682
True
```