import argparse
from distutils.util import strtobool

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument("task")  
    parser.add_argument("--headless", default=True, type=strtobool)

    args = parser.parse_args()

    print(f"Args: {args}")
    print(f"Headless set to: {args.headless}")
    print(f"Headless type: {type(args.headless)}")

    headless = bool(args.headless)
    print(f"Headless casted: {headless}")