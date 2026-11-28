*** Settings ***
Library    SeleniumLibrary
 
*** Variables ***
${URL}    https://www.google.com
${BROWSER}    Chrome
 
*** Test Cases ***
Verify Login Functionality
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Input Text    id=ti6dpd    Robot Framework
    Sleep    2s
    #Click Element    name = Google Search
    Press Key    name=btnK    ENTER
    Sleep    5s
    #Page Should Contain    Robot Framework
    #Close Browser