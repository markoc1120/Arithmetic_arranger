
def arithmetic_arranger(problems, *args):

    # Declaring and assigning each line
    arranged_problem_1 = ''
    arranged_problem_2 = ''
    arranged_problem_3 = ''
    arranged_problem_4 = ''

    # Limiting number of problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # Going over each problem one by one
    for problem in problems:

        problem = problem.split()

        # Checking if given input are numbers
        try:
            int(problem[0])
            int(problem[2])
        except ValueError:
            return 'Error: Numbers must only contain digits.'

        # Checking if operators have been given properly
        if (problem[1] != '-') and (problem[1] != '+'):
            return "Error: Operator must be '+' or '-'."

        # Getting the length of each number
        f_line = len(problem[0])
        s_line = len(problem[2])

        # Checking if numbers are small enough
        if f_line > 4 or s_line > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Calculating the whitespaces needed in the result
        if f_line > s_line:
            a = f_line - s_line
            b = 0
        elif f_line == s_line:
            (a, b) = (0, 0)
        else:
            a = 0
            b = s_line-f_line

        # Creating problems line by line
        arranged_problem_1 += f'  {" "*b + problem[0]}    '
        arranged_problem_2 += f'{problem[1]} {" "*a + problem[2]}    '
        arranged_problem_3 += f'{"--"+ "-"*(s_line if s_line > f_line else f_line)}    '

        # Calculating problem's result and building its line
        result = str(int(problem[0]) - int(problem[2]) if problem[1] == '-' else  int(problem[0]) + int(problem[2]))
        arranged_problem_4 += f'{" "*((2 + (s_line if s_line > f_line else f_line)) - len(result)) + result}    '

    # Adding up the lines created before, stripping whitespaces because of the testing phase
    arranged_problems = arranged_problem_1.rstrip() + '\n' + arranged_problem_2.rstrip() + '\n' + arranged_problem_3.rstrip()

    # Decide if arranged_problems should include result
    if args:
        arranged_problems += '\n' + arranged_problem_4.rstrip()

    # returning arranged_problems as a string
    return arranged_problems