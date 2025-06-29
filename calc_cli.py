import argparse
from tiferet import App, TiferetError

def main():
    """Parse CLI arguments and execute the calculator feature."""
    parser = argparse.ArgumentParser(description="Basic Calculator CLI using Tiferet")
    parser.add_argument('--config', default='app/configs/config.yml', help='Path to config file')

    subparsers = parser.add_subparsers(dest='operation', required=True, help='Calculator operation')

    # Define subcommands for each feature
    operations = [
        ('add', 'Add two numbers', True),
        ('subtract', 'Subtract one number from another', True),
        ('multiply', 'Multiply two numbers', True),
        ('divide', 'Divide one number by another', True),
        ('exp', 'Raise one number to the power of another', True),
        ('sqrt', 'Calculate the square root of a number', False),
    ]

    for op, help_text, needs_b in operations:
        subparser = subparsers.add_parser(op, help=help_text)
        subparser.add_argument('-a', required=True, help='First number')
        if needs_b:
            subparser.add_argument('-b', required=True, help='Second number')

    args = parser.parse_args()

    # Map operation to feature ID
    feature_map = {
        'add': 'calc.add',
        'subtract': 'calc.subtract',
        'multiply': 'calc.multiply',
        'divide': 'calc.divide',
        'exp': 'calc.exp',
        'sqrt': 'calc.sqrt',
    }
    feature_id = feature_map[args.operation]

    # Prepare feature parameters
    params = {'a': str(args.a)}
    if args.operation != 'sqrt':
        params['b'] = str(args.b)

    # Create app instance
    # # Assume the default app settings is defined in a YAML file
    settings = dict(
        app_repo_module_path='tiferet.proxies.yaml.app',
        app_repo_class_name='AppYamlProxy',
        app_repo_params=dict(
            app_config_file=args.config,
        )
    )
    app = App(settings)

    try:
        # Execute feature with locale
        result = app.run('basic_calc', feature_id, data=params)

        # Display result
        if args.operation == 'sqrt':
            print(f"√{args.a} = {result}")
        else:
            op_symbol = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/', 'exp': '^'}[args.operation]
            print(f"{args.a} {op_symbol} {args.b} = {result}")
    except TiferetError as e:
        print(f"Error: {e.message}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == '__main__':
    main()