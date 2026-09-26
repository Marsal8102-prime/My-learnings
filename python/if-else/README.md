# Python If-Else

`if`, `elif`, and `else` let a Python program make decisions. Python evaluates conditions from top to bottom, runs the first matching block, and then skips the rest of that chain.

![Python if-else flow diagram](assets/if-else-flow.svg)

## Basic Syntax

```python
if condition:
    # Runs when condition is True
elif another_condition:
    # Runs only when the first condition is False
else:
    # Runs when all earlier conditions are False
```

Python uses indentation to define each block. Consistent four-space indentation is the usual convention.

## Decision Flow

```mermaid
flowchart TD
    A([Start]) --> B{Is the if condition True?}
    B -- Yes --> C[Run the if block]
    B -- No --> D{Is an elif condition True?}
    D -- Yes --> E[Run the matching elif block]
    D -- No --> F[Run the else block]
    C --> G([Continue])
    E --> G
    F --> G
```
