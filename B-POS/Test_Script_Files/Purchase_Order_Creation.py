import VitPySelEnv
from VitPySelLibV2 import VitSelWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Xpath_Files import LoginScreen
from Xpath_Files import HomeScreen
from Xpath_Files import Transaction
from Xpath_Files import PurchaseOrder

# ****** Test case data ****** #
browser = VitSelWebDriver(VitPySelEnv.vWebDriver)
waitTime = 1
TC_ID = "TC_01"
TC_Name = "Purchase Order"
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

def PurchaseOrderCreation():

    navigatingToTransactionModule()
    waitUntilElementVisible(Transaction.TransactionModule_hoverDropdown_Purchase)

    # clicking on purchase order link
    browser.vitMouseOverClickXP(Transaction.TransactionModule_hoverDropdown_Purchase,Transaction.TransactionModule_link_purchaseOrder,'Purchase Sub Module','Purchase Order link','Application should navigate to Purchase order screen. ')
    print_('Clicked on purchase order link')
    waitUntilElementVisible(PurchaseOrder.PurchaseOrder_selectionBox_suppliers)
    browser.vitSStoDoc(TC_ID,'Purchase order screen, where user can raise purchase orders for preferred suppliers.')
    # Performing enter operation on suppliers selection box.
    browser.vitENTER(PurchaseOrder.PurchaseOrder_selectionBox_suppliers,'Application should populate suppliers modal window with all available suppliers.')
    print_('Performed Enter operation on Suppliers selection box')
    waitUntilElementVisible(PurchaseOrder.PurchaseOrder_textField_Suppliers_enterKeywordToSearch)
    wait(2)
    browser.vitSStoDoc(TC_ID,'Suppliers modal window which lists all available suppliers.')
    # Entering supplier name in suppliers modal enter keyword to search field.
    browser.vitTextInputXP(PurchaseOrder.PurchaseOrder_textField_Suppliers_enterKeywordToSearch,'Tata Motors','Suppliers keyword to search')
    print_('Entered supplier name in suppliers modal window enter keyword to search field.')
    wait(2)
    # Performing ENTER operation on suppliers modal window enter keyword to search field
    browser.vitENTER(PurchaseOrder.PurchaseOrder_textField_Suppliers_enterKeywordToSearch,'Should select preferred supplier to create purchase order.')
    print_('Performed ENTER operation on suppliers modal window enter keyword to search field.')
    # Clicking on F1_hide_details button.
    browser.vitClickXPWithJavaScript(PurchaseOrder.PurchaseOrder_button_hideDetails,'Hide Details button','Application should close suppliers details window.')
    print_('Clicked on Hide details button.')

    # Perform ENTER operation on Item code selectino field.
    browser.vitENTER(PurchaseOrder.PurchaseOrder_selectionBox_ItemCode,'Application should display Items modal window with all available items.')
    print_('Performed ENTER operation on Item Code selection field.')

    # Entering Item name in enter keyword to search fiedl of Items modal window.
    browser.vitTextInputXP(PurchaseOrder.PurchaseOrder_textfield_Items_enterKeywordToSearch,'Tata Nexon','Item search field')
    wait(2)
    print_('Entered Item name in Enter keyword to search field of Items modal window.')

    # Performing ENTER operation on Items modal window enter keyword to search field
    browser.vitENTER(PurchaseOrder.PurchaseOrder_textfield_Items_enterKeywordToSearch,'Should select preferred Item to create purchase order.')
    print_('Performed ENTER operation on Items modal window enter keyword to search field.')

    # Entering quantity in quantity field in item details window.
    browser.vitTextInputXP(PurchaseOrder.PurchaseOrder_input_ItemQuantity,'1','Item Quantity')
    print_('Entered quantity in quantity field.')

    # Performing ENTER operation on Item quantity field.
    browser.vitENTER(PurchaseOrder.PurchaseOrder_input_ItemQuantity,'Should select populate MRP and Cost price of selected Item accordin to quantity entered.')
    print_('Performed ENTER operation on Item quantity field.')

    # Clickin on save button.
    browser.vitClickXPWithJavaScript(PurchaseOrder.PurchaseOrder_button_save,'Save','Application should successfully create Purchase order with selected supplier and Items.')
    wait(5)
    print_('Clicked on Save button to create purchase order')
    browser.vitAcceptAlert('','')
    wait(5)
    browser.vitSStoDoc(TC_ID,'Successfully created Purchase Order with selected supplier for preferred items.')

    print_('Successfully created PURCHASE ORDER')

    browser.vitHeading(TC_ID + " - TEST PASSED",4)
    browser.vitDocSave(VitPySelEnv.vWebDriver + '_' + TC_ID + '_' +"Purchase Order")
    browser.vitTestCasePath(VitPySelEnv.tcDIR+'/'+TC_ID+'.csv')






    



def executeScript():
    launchApplication()
    login()
    PurchaseOrderCreation()

executeScript()

    