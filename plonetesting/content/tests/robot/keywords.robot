*** Keywords ***

Suite Setup
    Open Browser  ${front-page}  browser=${BROWSER}  desired_capabilities=Capture Page Screenshot

Suite Teardown
    Close All Browsers

Log in
    [Documentation]  Log in to the site as ${userid} using ${password}. There
    ...              is no guarantee of where in the site you are once this is
    ...              done. (You are responsible for knowing where you are and
    ...              where you want to be)
    [Arguments]  ${userid}  ${password}

    Go to  ${PLONE_URL}/login_form
    Page should contain element  __ac_name
    Page should contain element  __ac_password
    Page should contain button  Log in
    Input text  __ac_name  ${userid}
    Input text  __ac_password  ${password}
    Click Button  Log in

Log in as site owner
    [Documentation]  Log in as the SITE_OWNER provided by plone.app.testing,
    ...              with all the rights and privileges of that user.
    Log in  ${SITE_OWNER_NAME}  ${SITE_OWNER_PASSWORD}

Add Place to
    [Arguments]  ${folder}  ${title}  ${description}  ${geopoint}

    Go to  ${folder}/++add++plonetesting.content.place
    Input Text  name=form.widgets.IBasic.title  ${title}
    Input Text  name=form.widgets.IBasic.description  ${description}
    Click Link  Coordinates
    Click Element  css=.collapsible.collapsedBlockCollapsible .collapsibleHeader
    Input Text  name=form.widgets.ICoordinates.coordinates  POINT(${geopoint})
    Click Button  Save
    Page Should Contain  Item created

Add Rally to
    [Arguments]  ${folder}  ${title}  ${description}

    Go to  ${folder}/++add++plonetesting.content.rally
    Input Text  name=form.widgets.IBasic.title  ${title}
    Input Text  name=form.widgets.IBasic.description  ${description}
    Choose File  name=form.widgets.first_image  ${PATH_TO_TEST_FILES}/plone-logo.png
    Choose File  name=form.widgets.second_image  ${PATH_TO_TEST_FILES}/plone-logo.png
    Click Button  Save
    Page Should Contain  Item created
    Page Should Not Contain Element  css=#rally-map-portlet


Add Place to Rally
    [Arguments]  ${Place}  ${Rally}

    Go to  ${test-folder}/${Rally}
    Click Link  Edit
    Click Button  browse...
    Click Link  css=#form-widgets-places-contenttree a[href$='acceptance-test-folder']
    Click Link  css=#form-widgets-places-contenttree a[href$='${Place}']
    Click Button  Add
    Click Button  Save
    Page Should Contain  Changes saved
    Page Should Contain Element  css=#rally-map-portlet
