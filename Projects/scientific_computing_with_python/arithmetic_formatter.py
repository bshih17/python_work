def add_spaces_to_string(spaces, string):
  for i in range (0, spaces):
    string += ' '
  
  return string

def arithmetic_arranger(problems, solve=False):
  arranged_problems = ''
  first_row = ''
  second_row = ''
  third_row = ''
  fourth_row = ''

  if len(problems) > 5:
    return "Error: Too many problems."
  
  else:
    for problem in problems:
      split_problem = problem.split()
      
      if split_problem[1] != '+' and split_problem[1] != '-':
        return "Error: Operator must be '+' or '-'."
      
      elif len(split_problem[0]) > 4 or len(split_problem[2]) > 4:
        return "Error: Numbers cannot be more than four digits."
      
      else:
        try:
          first_operand = int(split_problem[0])
          second_operand = int(split_problem[2])
        
        except:
          return "Error: Numbers must only contain digits."
        
        problem_width = max(len(split_problem[0]), len(split_problem[2])) + 2
        
        # Forming string for 1st row
        first_row = add_spaces_to_string(problem_width - len(f"{first_operand}"), first_row)

        first_row += f"{first_operand}"
        first_row = add_spaces_to_string(4, first_row)

        # Forming string for 2nd row
        if split_problem[1] == '+':
          second_row += '+ '
        else:
          second_row += '- '

        second_row = add_spaces_to_string(problem_width - len(f"{second_operand}") - 2, second_row)
        
        second_row += f"{second_operand}"
        second_row = add_spaces_to_string(4, second_row)

        # Forming string for 3rd row
        for i in range(0, problem_width):
          third_row += '-'
          
        third_row = add_spaces_to_string(4, third_row)

        # If solve == True, calculate solution
        if solve == True:
          if split_problem[1] == '+':
            solution = first_operand + second_operand
            
          else:
            solution = first_operand - second_operand

          # Forming string for 4th row
          fourth_row = add_spaces_to_string(problem_width - len(f"{solution}"), fourth_row)
            
          fourth_row += f"{solution}"
          fourth_row = add_spaces_to_string(4, fourth_row)

    # Put first 3 rows together into 1 string
    arranged_problems += first_row.rstrip() + '\n' + second_row.rstrip() + '\n' + third_row.rstrip()

    # If solve == True, then add 4th row
    if solve == True:
      arranged_problems += '\n' + fourth_row.rstrip()     

    return arranged_problems

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], solve=True))

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))