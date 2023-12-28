## An Absolute xpath vs Custom Xpath
## An proper xpath can decrease the time consumption of the test run
## The Absolute Xpath or the Hierarchy based xpath won't work if the
## attributes changes, element changes, or the node name changes.
## So we can create Generic Xpath


#
# Here, Input is the tag,  type is the attribute
# //input[@type='f']
#
#
# For links a is the tag, link text can be used here, text() and contains() are functions.
# //a[text()='send']
# Or better use the below for links
# //a[contains(text(), 'send')]
#
#
# For Link of a tag text xpath use
# //a[@text()='Bootstrap']
#
#
# Normalise space usage:-
#//a[normalize-space()='28']
#//button[normalise-space(text()='Click Me'))]
# It is used when there is spacing issue in a value/text of a attribute/tag
#
#
# 'And' Use :-
# //div[@class='dropdown']//button[@type='button' and @class='btn btn-secondary dropdown-toggle' and @id='dropdownMenuButton']
# But we can use id directly to like below, but performance wise above xpath is better
# //button[@id='dropdownMenuButton']
#
#
# Parent and Siblings :-
# preceding-sibling and forward-sibling: preceding for before child, following for after child
#//a[text()='test2 test2']//parent::td[@class='datalistrow']//preceding-sibling::td[@class='datalistrow']//input[@name='contact_id']
#//a[text()='test2 test2']//parent::td[@class='datalistrow']//following-sibling::td[@class='datalistrow']//input[@name='contact_id']
# By these you are going in reverse manner to a tag for the child's Xpath
# Instead of writing two for loops you can use the above, this is the xpath of the child that has this parent and sibling
#//a[text()='TEST demo']//parent::td//preceding-sibling::td//div//input[@name='id']
# To use this first go to the the XPATH sibling and then go to the real XPATH that
# you want to use
#
# Starts-with and Ends-with :-
# Used for dynamic ID
# class name can change, Dynamic ID changes everytime the page refreshes
# You can use contains() function in Dynamic ID, and exclude the dynamic part
# //input[contains(@id, 'test_')]
# //input[starts-with(@id, 'test_')
# //input[ends-with(@id, '_test')
# With ID/Selector Contains function requires @ sig and with func you can write directly eg=//a[text()='send']
#
#
# Double Quote in XPath:-
# Some API or Website supports only "" in xpath to handle it in find_element()
# use escape character
# print("\"Hello\"") will print "Hello"
#
# * example : "//*[@id='TEST_0'][disabled='']"

## AI Usage

## SelectorsHub
## You can use SelectorsHub for Big pages/Multiple Projects
## In this if the relative Xpath is the Absolute Xpath
## then again you can use locators knowledge to generate a custom locator using HTML DOM of DEVTools of Chrome
## You can also copy JScript path and paste it in Console of DevTools


## Bug Magnet : It generates dummy details for us to fill a form
## In Credit Card filling we can use this to fill VISA, MasterCard credential for check
## While filling an application if the user is from an latin america, arabic country
## so we can use this to check the entries that a webpage takes

