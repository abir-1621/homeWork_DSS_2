from setuptools import setup, find_packages

setup(
    name='math_quiz', 
    version='0.1',
    packages=find_packages(),
    install_requires=[], 
    description='Score based random math quiz game',
    author='Md Abir',
    author_email='abirkhan88821@gmail.com',
    url='https://github.com/abir-1621/homeWork_DSS_2',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',  
        ],
    },
)
