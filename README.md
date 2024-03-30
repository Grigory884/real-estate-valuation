# Telegram bot for real estate valuation
  This project is a Telegram bot that allows users to get a preliminary estimate of the value of a piece of real estate, based on the data entered by them.
  ## Table of Contents:
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Documentation](#documentation)
- [Contribution](#contribution)
  ## Installation
1. Clone the repository:

shell
   
>``git clone https://github.com/Grigory884/real-estate-valuation ``
2. Install the necessary dependencies:

shell

>``pip install -r requirements.txt``

3. Replace

> '6374538466:AAEdhZ7gnNfBoPPjIffDk9QD7QqAGt7253c'

to your own Telegram bot token

## Usage
Launch the bot using the following command:

shell

>``telegrambot.py``

The bot will be waiting for messages from users. To get an estimate of the value of the property, the user must send a message containing the following data:
- total_area
- num_room
- sub_area
- kitch_sq

The bot will process this data and return a preliminary estimate of the value of the property.

## Examples
Example of a user message:

```
Площадь: 80 кв.м.
Количество_комнат: 2
Район: Басманный
Площадь_кухни: 12 кв.м..
```

The bot's answer:

```Предварительная оценка стоимости недвижимости: 23 000 000 рублей```

## Documentation
Additional documentation is available at:
[https://github.com/Grigory884/real-estate-valuation/blob/main/macro.csv]
[]

## Contributing
If you would like to contribute to this project, we would appreciate it if you created a new issue or opened a pull request on our GitHub repository.
