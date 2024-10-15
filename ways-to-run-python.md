# ways to run Python code

### before install
1. `python script.py`
2. `python -m module  # it runs code from __main__.py`
3. `python -m module.submodule  # it runs module directly - module/submodule.py`

### after install
1. `python -m module  # after install available system-wide`
2. `python -c "from module import run;run()"`
3. `entrypoint  # after install available system-wide`

### Linux specific
1. `script  # specified as script in setup.py, available system-wide`
    setup.py
    ```python
    from setuptools import setup

    setup(
        name="the script",
        version="0.1",
        scripts=["example.py"]
    )
    ```

    example.py
    ```python
    #!/usr/bin/env python3
    print('this is example of how script in setup.py works on Linux :)')
    ```

    install & usage
    ```bash
    python setup.py  # install
    example  # system wide usage
    ```

2. `script  # after .deb creation & install, available system-wide`
