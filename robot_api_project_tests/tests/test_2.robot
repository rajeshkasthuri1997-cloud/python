*** Settings ***
Resource        ../Resources/equipment_keyboard.resource
Suite Setup     Create API Session

*** Test Cases ***
Test Get All Equipment
    log To Console      Test1 Started
    ${response}=       Get All Equipment
    ${data}=        Set Variable        ${response.json()}
    Should Be Equal As Integers     ${response.status_code}     200
    Length Should Be        ${data}     2

Test Get Equipment By ID
    ${response}=    Get Equipment By ID    103    404
    ${error}=    Set Variable    ${response.json()}
    Should Be Equal As Integers    ${response.status_code}    404
    Should Be Equal As Strings    ${error}[error]    Equipment not found