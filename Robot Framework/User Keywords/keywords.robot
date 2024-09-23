*** Keywords ***
Concatenate varargs
    [Documentation]    The keyword should take a variable number of positional arguments.
    ...                The keyword should log the following message when called: "Got args=<values>"
    ...                For example: "Got args=['first', 'second']"
    ...                Logs should appear in the console.
    ...                The keyword should return a string made of space-separated arguments it received.
    ...                For example: "first second"
    ...                Hint: use the 'Catenate' keyword from the BuiltIn library, or extended variable syntax.
    [Arguments]    @{args}
    Log    Got args=${args}
    ${result}=    Catenate    SEPARATOR=    @{args}
    [Return]    ${result}