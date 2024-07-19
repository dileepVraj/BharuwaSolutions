import VitPySelEnv
from VitPySelLibV2 import VitSelWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Xpath_Files import LoginScreen
from Xpath_Files import HomeScreen
from Xpath_Files import Transaction
from Xpath_Files import SalesOrder

# ****** Test case data ****** #
browser = VitSelWebDriver(VitPySelEnv.vWebDriver)
waitTime = 1
TC_ID = "TC_02"
TC_Name = "Sales_Order_Creation"
browser.vitTCHeading(VitPySelEnv.vWebDriver + "_" + TC_ID + ":" + TC_Name)
# ***********************************************************************#

def wait(time):
    browser.vitWait(time)

def print_(message):
    print('------------',message,'--------------')

def waitUntilElementVisible(element):
    browser.Vit_wait_for_element_visibility(element)

def navigatingToTransactionModule():
    # Clicking on Transaction Component.
    browser.vitClickXP(HomeScreen.HomeScreen_link_Transactions,'Transactions module link','System should display transaction inner menu.')
    print('------ Successfully clicked on Transaction module ------')
    wait(3)
    browser.vitSStoDoc(TC_ID,'Transaction module with lot of sub-modules to perform vairous transactinos for user.')

def launchApplication():
    
    browser.vitLaunchUrl(VitPySelEnv.URL)
    browser.vitWait(5)
    print('----- application launched successfully -----')
    browser.vitMaxmizeScreen()
    print('------ successfully maximized browser window ------')
    browser.vitWait(3)

def login():
    browser.vitSStoDoc(TC_ID,'Orient LED Login Page.')
    waitUntilElementVisible(LoginScreen.LoginScreen_input_username)
    print('----- Started Login Operation -------')
    browser.vitTextInputXP(LoginScreen.LoginScreen_input_username,VitPySelEnv.username,'Username/Email')
    # browser.vitWait(OneSec)
    print('------ Entered username -----')
    waitUntilElementVisible(LoginScreen.LoginScreen_input_password)
    browser.vitTextInputXP(LoginScreen.LoginScreen_input_password,VitPySelEnv.password,'Password')
    print('----- Entered password -----')
    # browser.vitWait(OneSec)

    waitUntilElementVisible(LoginScreen.LoginScreen_button_signIn_btn)
    browser.vitClickXP(LoginScreen.LoginScreen_button_signIn_btn,'Sign In Button','System should redirect user to Home page.')
    print('----- Clicked on Login button -----')
    browser.vitWait(5)
    browser.vitSStoDoc(TC_ID,'The Home page with lot of navigation options to navigate different modules and serving as the entry point to the website.')
    waitUntilElementVisible(HomeScreen.HomeScreen_link_Masters)

def navigateToSalesOrder():
    navigatingToTransactionModule()
    #Clicking on sales order link.
    browser.vitMouseOverClickXP(SalesOrder.SalesOrder_hoverMenu_SalesHoverMenu,SalesOrder.SalesOrder_link_SalesOrderLink,'Sales','Sales Order','Application should navigate user to Sales order screen.')
    wait(4)
    browser.vitSStoDoc(TC_ID,'Sales order screen, where user can create sales order for preferred customer.')
    waitUntilElementVisible(SalesOrder.SalesOrder_selectionBox_Customers)
    
def salesOrderCreation():
    # Performing ENTER operation on suppliers selection box.
    browser.vitENTER(SalesOrder.SalesOrder_selectionBox_Customers,'Application should display Customers modal window with available Customers.')
    print_('Performd ENTER on suppliers selection box.')

    # Entering customer name in ' enter keyword to search field ' of suppliers modal window.
    browser.vitTextInputXP(SalesOrder.SalesOrder_inputBox_customers_enterkeywordTosearch,'Atharav','Customers modal window search field.')
    print_('Entered customer name in search field of customers modal window.')

    # Performing ENTER operation on search field of customers modal window.
    browser.vitENTER(SalesOrder.SalesOrder_inputBox_customers_enterkeywordTosearch,'Should select preferred customer to create sales order.')
    print_('Performed ENTER operation on search field of customers modal window.')

    # Performing ENTER operation on ITEM CODE field.
    browser.vitENTER(SalesOrder.SalesOrder_selectionBox_ItemCode,'Application should display ITEMS modal window with all available items.')
    print_('Performed ENTER operation on ITEM CODE field.')

    # Entering ITEM name in Search field of Items modal window.
    browser.vitTextInputXP(SalesOrder.SalesOrder_inputBox_Items_EnterkeywordToSearch,'Orient Air Cooler','Search of Items modal window.')
    print_('Enered ITEM name in search field.')

    # Performing ENTER operation on search field of Items modal window.
    browser.vitENTER(SalesOrder.SalesOrder_inputBox_Items_EnterkeywordToSearch,'Application should select preferred item to create sales order.')
    print_('Performed ENTER operation on ITEM modal window serach field.')

    # Entering quantity in quantity field.
    browser.vitTextInputXP(SalesOrder.SalesOrder_inputBox_quantity,'1','Quantity')
    print_('Entered quantity of item')

    # Performing ENTER operation on quantity field.
    browser.vitENTER(SalesOrder.SalesOrder_inputBox_quantity,'Application should populate MRP and selling price of item.')
    print_('Performed ENTER operation on Quantity fiel.')

    # Clicking on save button.
    browser.vitClickXPWithJavaScript(SalesOrder.SalesOrder_button_Save,'Save','application should display advance window to pay to advance payment.')
    print_('Clicked on save button of sales order.')
    waitUntilElementVisible(SalesOrder.SalesOrder_inputBox_AdvanceAmount)

    # Entering advance amount in advance amount input field.
    browser.vitTextInputXP(SalesOrder.SalesOrder_inputBox_AdvanceAmount,'100','Advance amount')
    print_('Entered advance amount 100 in advance amount field.')

    # Clicking on OK button of advance amount window.
    browser.vitClickXPWithJavaScript(SalesOrder.SalesOrder_button_Advance_OK,'Sysetem should save sales order successfully and display print receipt modal window.')
    print_('Clicked on OK button of advance amount window.')
    wait(5)
    browser.vitSStoDoc(TC_ID,'Successfully created sales order with preferred customer and items.')
    # Clicking on cancel button of print receipt window.
    browser.vitClickXPWithJavaScript(SalesOrder.SalesOrder_button_print_cancel,'print cacel button','Should close print receipt window.')
    print_('Clicked on cancel button of print receipt window.')

    browser.vitHeading(TC_ID + " - TEST PASSED",4)
    browser.vitDocSave(VitPySelEnv.vWebDriver + '_' + TC_ID + '_' +"Sales Order")
    browser.vitTestCasePath(VitPySelEnv.tcDIR+'/'+TC_ID+'.csv')

    








def execute():
    launchApplication()
    login()
    navigateToSalesOrder()
    salesOrderCreation()

execute()