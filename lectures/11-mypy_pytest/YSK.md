# Type hints

- What does the `: int` mean in `def add(a: int, b: int) -> int`?
    - **Answer**: It declares that the parameters `a` and `b` are expected to be of type `int`.

- What does the `-> int` mean in `def add(a: int, b: int) -> int`?
    - **Answer**: It declares that the function returns a value of type `int`.

- What will happen at runtime if you call `add(3.14, 7.00)` given the type hints in `def add(a: int, b: int) -> int`?
    - **Answer**: No error will occur, and the function will return `10.14` as a float, ignoring the type hints.

# Type hint examples

- What type hint declares that `numbers` should be a list of floats?
    - **Answer**: `list[float]`.

- What is a downside of typing a parameter as `list[float]` if the function only iterates over it?
    - **Answer**: It rejects other valid finite collections like tuples or sets.

- Which `collections.abc` type is appropriate for "any finite collection of items"?
    - **Answer**: `Collection`.

- What does the type hint `Collection[float]` mean?
    - **Answer**: Any finite collection (list, set, tuple, etc.) whose elements are floats.

- What does the type hint `int | str` mean?
    - **Answer**: A value that is either an `int` or a `str`.

- What is the term for a type hint like `int | str`?
    - **Answer**: A type union.

- What type hint would you use for an optional argument (i.e., one that can be an `int` or `None`)?
    - **Answer**: `int | None`

- What does the syntax `def maximum[T](items: Collection[T]) -> T` introduce?
    - **Answer**: A type variable `T`, making `maximum` a generic function over the element type.

# Pytest basics

- What filename prefix does pytest use to discover test files?
    - **Answer**: `test_`.

- What function-name prefix does pytest use to discover test functions within a test file?
    - **Answer**: `test_`.

- What Python keyword is used inside a test function to check that a condition holds?
    - **Answer**: `assert`.

- What does TDD stand for?
    - **Answer**: Test-driven development.

- After seeing a test fail (red) in TDD, what is the next step?
    - **Answer**: Write the minimum code needed to make the test pass.

- Should tests check the output of a function or its internal implementation?
    - **Answer**: The output of the function.

- Why should you avoid `==` to compare floats in tests?
    - **Answer**: Floating-point arithmetic produces small rounding errors that can make mathematically equal values compare unequal.

- What does `pytest.raises(TypeError)` do when used in a `with` block?
    - **Answer**: Asserts that the code inside the block raises a `TypeError`.
