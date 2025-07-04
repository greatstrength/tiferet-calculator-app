from tiferet import App

# Create new app (manager) instance.
app = App(dict(
    app_repo_module_path='tiferet.proxies.yaml.app',
    app_repo_class_name='AppYamlProxy',
    app_repo_params=dict(
        app_config_file='app/configs/config.yml',
    )
))

# Execute the add feature to add the values.
a = 1
b = 2
addition = app.run(
    'basic_calc', 
    'calc.add', 
    data=dict(
        a=a,
        b=b,
    )
)

print(f'{a} + {b} = {addition}')

# Execute the subtract feature to subtract the values.
a = 5
b = 3
subtraction = app.run(
    'basic_calc', 
    'calc.subtract', 
    data=dict(
        a=a,
        b=b,    
    )
)

print(f'{a} - {b} = {subtraction}')


# Execute the multiply feature to multiply the values.
a = 4
b = 3
multiplication = app.run(
    'basic_calc', 
    'calc.multiply', 
    data=dict(
        a=a,
        b=b,
    )
)

print(f'{a} * {b} = {multiplication}')


# Execute the divide feature to divide the values.
a = 8
b = 2
division = app.run(
    'basic_calc', 
    'calc.divide', 
    data=dict(
        a = a,
        b = b,
    )
)

print(f'{a} / {b} = {division}')


# Trigger an error by dividing by zero.
a = 8
b = 0
divide_by_zero = app.run(
    'basic_calc',
    'calc.divide',
    data=dict(
        a=a,
        b=b,
    ),
)

print(f'Returned error: {divide_by_zero}')

# Execute the exponentiate feature to raise a to the power of b.
a = 2
b = 3
exponentiation = app.run(
    'basic_calc', 
    'calc.exp',
    data=dict(
        a=a,
        b=b,
    )
)

print(f'{a} ** {b} = {exponentiation}')


# Execute the square root feature to find the square root of a.
a = 16
square_root = app.run(
    'basic_calc', 
    'calc.sqrt',
    data=dict(
        a=a,
    )
)   

print(f'sqrt({a}) = {square_root}')