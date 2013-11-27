*** Settings ***

Library  Selenium2Library  timeout=10  implicit_wait=0.5  run_on_failure=Capture Page Screenshot

Resource  keywords.robot

Variables  plone/app/testing/interfaces.py
Variables  plonetesting/content/tests/variables.py

Suite Setup  Suite Setup
Suite Teardown  Suite Teardown

*** Variables ***

${PORT} =  55001
${ZOPE_URL} =  http://localhost:${PORT}
${PLONE_URL} =  ${ZOPE_URL}/plone
${BROWSER} =  Firefox

${front-page}  http://localhost:55001/plone/
${test-folder}  http://localhost:55001/plone/acceptance-test-folder


*** Test Cases ***

Test Plone testing content
    Log in as site owner
    Go to  ${test-folder}
    Add Place to  ${test-folder}  First test place  This is a first place  45.01 50.01
    Add Place to  ${test-folder}  Second test place  This is a second place  45 50
    Add Rally to  ${test-folder}  Rally  This is a rally
    Add Place to Rally  first-test-place  rally
