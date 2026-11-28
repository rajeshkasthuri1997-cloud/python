*** Settings ***
Library    RequestsLibrary
Library    Collections
*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Keywords ***
Create API Session
    Create Session       Equipment_API      ${BASE_URL}
*** Test Cases ***
Test Get All Equipment
    Create API Session
    ${response}=        GET On Session      Equipment_API       /api/equipment
    Should Be Equal As Integers     ${response.status_code}      200
    Log To Console      ${response.json()}
TC002_Test_GET_one
    Create API Session
    ${response}=        GET On Session      Equipment_API       /api/equipment/101
    Should Be Equal As Integers     ${response.status_code}      200
    ${Data}=        Set Variable        ${response.json()}
    Should Be Equal As Integers     ${Data}[id]      101
    Should Be Equal As Strings      ${Data}[name]       flight control unit
    Should Be Equal As Strings      ${Data}[type]       bFCU
    Should Be Equal As Strings      ${Data}[STATUS]     operational
    Log To Console      ${response.json()}