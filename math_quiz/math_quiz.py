import random

def generate_random_integer(minimum_v, maximum_v):

    """
    Generates a random integer within a specified range.
    Args:
        minimum_v (int): minimum value of range.
        maximum_v (int): maximum value of range.
    Returns:
        int: random integer between minimum_v and maximum_v.
    """
    return random.randint(minimum_v, maximum_v)

def generate_random_operator():
    """
    Randomly picks an operator.
    Returns:
        str: randomly selected operator like '+', '-', '*'.
    """
    return random.choice(['+', '-', '*'])

def create_problem(num1, num2, operator):
    """
    Creates a math problem and generates the correct answer.
    Args:
        num1 (int): first number.
        num2 (int): second number.
        operator (str): used operator ('+', '-', or '*').
    Returns:
        tuple: A tuple containing the string representation of the problem and the correct answer.
    Raises:
        ValueError: If an invalid operator is provided.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        raise ValueError("Invalid operator: Only '+', '-', and '*' are allowed.")
    return problem, answer

def math_quiz():
    """
    Runs a math quiz where the user is given with random problems to provide correct answers, based on
    correct answers there is a score.

    Checks invalid input and displays the final score.

    Raises:
        ValueError: If input cannot be converted to an integer.
    """
    score = 0
    total_questions = 3  # Number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, correct_answer = create_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue  # Skips to the next question if input is invalid

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
