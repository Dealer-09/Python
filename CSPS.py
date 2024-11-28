from sympy import symbols, diff, solve, Matrix, sympify

def critical_point_calculator():
    # Input variables and function
    variables_input = input("Enter variables separated by commas (e.g., x, y, z): ").replace(" ", "")
    variables = symbols(variables_input)  # Dynamically create symbolic variables
    if not isinstance(variables, tuple):
        variables = (variables,)
    function_input = input(f"Enter a function in terms of {variables_input} (e.g., x*2 + y*2 - x*y): ")
    f = sympify(function_input)  # Safely evaluate the input as a symbolic function

    # First derivative
    derivatives = [diff(f, var) for var in variables]
    critical_points = solve(derivatives, variables, dict=True)

    if not critical_points:
        print("No critical points found.")
        return

    print("\nCritical Points and Classification:")

    for point in critical_points:
        #Hessian matrix
        hessian_matrix = Matrix([[diff(diff(f, var1), var2) for var2 in variables] for var1 in variables])
        hessian_at_point = hessian_matrix.subs(point)

        #Calculate determinant of the Hessian
        determinant = hessian_at_point.det()

        # Classification of critical point
        if determinant > 0:
            classification = "Local Minimum" if hessian_at_point[0, 0] > 0 else "Local Maximum"
        elif determinant < 0:
            classification = "Saddle Point"
        else:
            classification = "Indeterminate"

        print(f"Point: {point} - {classification}")

# Run the function
critical_point_calculator()
