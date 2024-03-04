from behave import given, when, then

@given(u'I navigate to the matches pages')
def nav(context):
    """ 
    Navigate to the matches page
    """
    context.browser.get('https://electrasilicon-koalafood-5000.codio-box.uk/matches/1')

@when(u'I click on the link to goals details')
def click(context):
    """ 
    Find the desired link
    """
    context.browser.find_element_by_partial_link_text('1').click()

@then(u'I should see the goals for that match')
def details(context):
    """ 
    if successful, then we should be directed to the goalscorers page
    """
    # use print(context.browser.page_source) to aid debugging
    print(context.browser.page_source)
    assert context.browser.current_url == 'https://cs551p-web-development.onrender.com/scorers/348'
    assert 'Brazil (3) VS Croatia (1)' in context.browser.page_source