*** Settings ***
Resource  ../keywords/test_keywords.robot
Resource  ../keywords/web_keywords.robot
Suite Setup  Web Suite Setup Keywords


*** Variables ***
${target_env}  uat
${territory}  tw
${local}  ${True}


*** Test Cases ***


Search Movie To Play
    [tags]  ashley1
    Create Webdriver  Chrome
    Maximize Browser Window
    Go To  ${base_url}
    Login Web  0966666000  00000000
    ${result}=  Search Video By Keyword  老大人
    Should Be True  ${result['found']}
    Should Contain  ${result['video_name']}  老大人
    Click Element  ${result['xpath']}
    Start To Proceed And Watch Video
    Close All Browsers








