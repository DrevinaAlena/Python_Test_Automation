*** Settings ***
Library    ClassLibrary.py    James

*** Test Cases ***
Test My Name Is With Surname
    ${greeting}=    My Name Is    Bond
    Log    ${greeting}
    Should Be Equal As Strings    ${greeting}    My name is Bond, James Bond

Test My Name Is Without Surname
    ${greeting}=    My Name Is
    Log    ${greeting}
    Should Be Equal As Strings    ${greeting}    My name is James

Test Concatenate Varargs
    ${result}=    Concatenate Varargs    Hello    World
    Log    ${result}
    Should Be Equal As Strings    ${result}    Hello World