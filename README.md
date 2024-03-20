## Python unit tests

As much as our code grows, funcionallities may get one, two or three responsabilities and this can pass unnoticed.
Test Driven Development makes the development proccess focus on requirements and the tests written in conjunction with the logic.

So the code becomes more simple and pratical, the software requirements are fullfilled and the releases are updated as new features came.

TDD tells us more about simplicity of our code and helps us to know the mainly purpose of its modules. 

To test:

Create .env file and fill it with
```
API_KEY=1234
```
Run
```
pip install -r requirements.txt
pytest
pytest --cov
```