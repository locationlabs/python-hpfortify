## Contributing to Python HPFortify

We'd love to accept your patches!
To contribute to python-hpfortify simply open a pull request against the [develop branch](https://github.com/rakeshcusat/python-hpfortify/tree/develop)

We expect you to adhere to the following rubric. This will increase the chance that your pull request is accepted:
* Succinctly describe your changes in the pull request description
* Write tests:
  * New features should include tests
  * Changes to existing code should be reflected in the tests
  * Code coverage should not decrease. We would love to see increase in the code coverage.
  * Run **all** the tests to assure nothing else was accidentally broken.
  * If you have fixed any issue then write a test case to make sure that your fix is working. It also increases the code coverage and avoid us doing the same mistake in future.
* Be consistent with the coding style. We closely follow the `pep8` coding standard. Run the `tox` command to make sure your changes have not violated any of the `pep8` rules.
* Make commits of logical units.
  * Write quality commit message by providing enough context and information.  
* Avoid unnecessary whitespace. Check for unnecessary whitespace with `git diff --check` before committing.


## Unit Test Case

We use `nosetest` to write unit test case. You can check `hpfortify/tests` directory for reference. 

### Run Unit Test Case

You can run the unit test cases by executing the following command in the project root directory.

    ```sh
    python setup.py nosetests
    ```

### Code Style Guide

We closely follow `pep8` code style guide. We have configured `tox` to check the code style and also run the unit test. You can use the following command to run the tox. You can run this command in the project root directory.

    ```sh
    tox
    ```