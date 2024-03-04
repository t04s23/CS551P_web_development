Feature: Matches
""" 
Confirm that we can browse the matches related pages on our site
"""

Scenario: success for visiting matches and goal scorer details pages
    Given I navigate to the matches pages
    When I click on the link to matches details
    Then I should see the scores for that match
