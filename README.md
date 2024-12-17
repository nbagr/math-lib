# Math library

[![Python CI](https://github.com/nbagr/math_lib/actions/workflows/check.yaml/badge.svg)](https://github.com/nbagr/math_lib/actions/workflows/check.yaml)

[![Maintainability](https://api.codeclimate.com/v1/badges/8085da87212e1b4208c1/maintainability)](https://codeclimate.com/github/nbagr/math-lib/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/986ff24f761015883fbe/test_coverage)](https://codeclimate.com/github/nbagr/math_lib/test_coverage)

## Description

Library with simple mathematical functions.

## Setup

```bash
git clone git@github.com:nbagr/math_lib.git
cd math_lib
make install
```

## Using

```python
from math_lib import arithmetic, collection, figures

arithmetic.sum(3, 4) # 7
collection.max([24, 10, 7, 6, 0]) # 24
figures.square_perimeter(3) # 12
```

## Modules and functions

Functions list:

- [arithmetic.sum()](#sum)
- [arithmetic.subtraction()](#subtraction)
- [arithmetic.multiply()](#multiply)
- [arithmetic.divide()](#divide)
- [arithmetic.factorial()](#factorial)
- [arithmetic.pow()](#pow)
- [arithmetic.log()](#log)
- [arithmetic.degrees_to_radians()](#degrees_to_radians)
- [arithmetic.radians_to_degrees()](#radians_to_degrees)



### arithmetic

#### sum()

*Description:* sum all the arguments.

*Arguments:* *args

*Example:*

```python
sum(3, 4) #7
sum(18, 41, 16, 8) # 83
```

#### subtraction()

*Description:* subtraction all the arguments.

*Arguments:* *args

*Example:*

```python
sum(3, 4) #7
sum(18, 41, 16, 8) # 83
```

### Collection

### Figures