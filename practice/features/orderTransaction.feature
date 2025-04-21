Feature: Order Transaction
    Test the order transaction

    Scenario Outline: verify the order transaction message shown in details page
      Given place the item order with <username> and <password>
      And the user is on landing page
      When I login to portal with <username> and <password>
      And navigate to orders page
      And Select the orderId
      Then order message is successfully displayed
      Examples:
        | username             | password  |
        |rahulshetty@gmail.com |Iamking@000|

