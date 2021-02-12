# pypesel

PESEL Python module

PESEL is the national identification number used in Poland since 1979. It always has 11 digits, identifies just one person and cannot be changed to another one (except some specific situations such as gender reassignment).

## Installation

```shell
pip install pesel
```

## Usage

```python
from pesel import Pesel

random_pesel = Pesel.generate()
random_pesel_male = Pesel.generate(male=True)
random_pesel_2021 = Pesel.generate(year=2021)

pesel = Pesel("65432101239")
```