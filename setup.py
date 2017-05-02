from setuptools import find_packages, setup

setup(
    name='uscis-quiz',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'uscis-quiz=uscis_quiz.quiz:main'
        ]
    }
)
