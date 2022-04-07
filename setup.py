from setuptools import setup, find_packages

setup(
    name='telegram_bot',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'telegram_bot-cli = telegram_bot.Bot.bot:bot',
        ],
    },
)
