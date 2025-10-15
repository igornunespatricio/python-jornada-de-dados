import create_measurements
import using_polas
import using_python
import using_python_old
from utils import print_statistics_file


def main():
    create_measurements.main()
    using_python.main()
    using_python_old.main()
    using_polas.main()
    print_statistics_file()
    print("Done.")


if __name__ == "__main__":
    main()
