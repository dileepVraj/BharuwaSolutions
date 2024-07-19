import VitPySelEnv
from VitPySelLibV2 import VitSelWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Xpath_Files import LoginScreen
from Xpath_Files import HomeScreen
from Xpath_Files import Transaction
from Xpath_Files import PurchaseInvoice
# ****** Test case data ****** #
browser = VitSelWebDriver(VitPySelEnv.vWebDriver)
waitTime = 1
TC_ID = "TC_01"
TC_Name = "Purchase_Invoice_Creation"
browser.vitTCHeading(VitPySelEnv.vWebDriver + "_" + TC_ID + ":" + TC_Name)
from Xpath_Files import PurchaseInvoice
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



def purchaseInvoice():
    
    navigatingToTransactionModule()

    # Clicking on purchase invoice link.
    browser.vitMouseOverClickXP(Transaction.TransactionModule_hoverDropdown_Purchase,Transaction.TransactionModule_link_PurchaseInvoice,'System should navigate user to purchase invoice screen.')
    print('--------- Successfully clicked on purchase invoice screen ------')
    wait(3)
    browser.vitSStoDoc(TC_ID,'Purchase Invoice screen where user can purchase stock for selected items.')
    waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_selectionBox_Supplier)


    # Clicking on Supplier selection box.
    browser.vitENTER(PurchaseInvoice.PurchaseInvoiceScreen_selectionBox_Supplier,'System should diaplay window with existing suppliers')
    print_('successfully displayed supplier window')
    waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_input_Suppliers_EnterKeyWordToSearch)


    # Entering supplier name in 'Enter key word to search field'
    browser.vitTextInputXP(PurchaseInvoice.PurchaseInvoiceScreen_input_Suppliers_EnterKeyWordToSearch,'ANMOL ENTERPRISES','Enter keyword to search')
    print_('Successfully entered supplier name')
    wait(3)
    browser.vitENTER(PurchaseInvoice.PurchaseInvoiceScreen_input_Suppliers_EnterKeyWordToSearch,'System should select user specified supplier.')
    waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_input_InvoiceNumber)
    

    # capturing invoice number into a variable.
    InvoiceNumber = browser.vitCaptureLabelText(PurchaseInvoice.PurchaseInvoiceScreen_label_InvoiceNumber)
    wait(2)

    # Entering Invoice number.
    browser.vitTextInputXP(PurchaseInvoice.PurchaseInvoiceScreen_input_InvoiceNumber,InvoiceNumber,'Invoice number')
    print_('successfully entered Invoice number')
    waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_input_ItemCode)

    # Performing Enter Operation on Item code field.
    browser.vitENTER(PurchaseInvoice.PurchaseInvoiceScreen_input_ItemCode,'System should display window with existing items.')
    print_('successfully clicked on item menu code field')
    # waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_input_Item_EnterKeywordToSearch)
    wait(4)

    # Entering Item Name in Enter Key word to search field.
    browser.vitTextInputXP(PurchaseInvoice.PurchaseInvoiceScreen_input_Item_EnterKeywordToSearch,'Orient Air Cooler','Item Name')
    wait(3)
    # waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_input_Item_EnterKeywordToSearch)
    print_('Item name entered successfully')


    #performing enter operation in EnterKeywordToSearch field.
    browser.vitENTER(PurchaseInvoice.PurchaseInvoiceScreen_input_Item_EnterKeywordToSearch,'System should select specified item successfully')
    waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_input_batchNumber)
    print_('Item selected successfully')

    # Entering batch number
    browser.vitTextInputXP(PurchaseInvoice.PurchaseInvoiceScreen_input_batchNumber,'Batch_01','Batch number')
    print_('Entered batch number for product.')
    waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_input_manufacturerDate)
    print_('Successfully entered Batch number')

    # Entering manufacturing date.
    browser.vitTextInputXP(PurchaseInvoice.PurchaseInvoiceScreen_input_manufacturerDate,'09/10/2023','Manufacturing Date')
    print_('MGF_date entered')
    waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_input_expireyDate)
    print_('Successfully entered manufacturing date')

    # Entering expiry date.
    browser.vitTextInputXP(PurchaseInvoice.PurchaseInvoiceScreen_input_expireyDate,'09/10/2029','Expiry Date')
    print_('EXP_date entered.')
    waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_input_quantity)
    print_('Successfully entered expired date')

    # Entering quantity .
    browser.vitTextInputXP(PurchaseInvoice.PurchaseInvoiceScreen_input_quantity,'2','Item quantity')
    print_('Entered quantity.')
    waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_input_quantity)
    print_('Successfully entered quantity')

    # performing Enter operation on quantity field.
    browser.vitENTER(PurchaseInvoice.PurchaseInvoiceScreen_input_quantity,'Prices and discounts should populate appropriately in respective fields.')
    print_('Performed ENTER operation on quantity field.')
    waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_label_Total)


    # capturing total amount.
    Total = browser.vitCaptureLabelText(PurchaseInvoice.PurchaseInvoiceScreen_label_Total)
    print('-----------------------------------------------------------------------------------')
    print(Total)
    wait(3)

    GrandTotal = Total[7:]
    truncated_Total = GrandTotal.split('.')[0]
    # Entering invoice amount

    print('=======================================================================')

    print('Total = ',truncated_Total)

    # Clicking on F1 hide details.
    browser.vitClickXP(PurchaseInvoice.PurchaseInvoiceScreen_button_F1_HideDetails,'System should elobrate Details Tab')
    print_('Clicked on Hide details button.')
    waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_input_invoice_amount)
    print_('Clicked on F1 details button.')
    

    # Entering amount in Invoice amount field.
    browser.vitTextInputXP(PurchaseInvoice.PurchaseInvoiceScreen_input_invoice_amount,truncated_Total,'Invoice amount')
    print_('Entered invoice amount in invoice amount field.')
    # waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_button_Save)
    wait(4)
    print_('Successfully entered invoice amount')


    # Clicking on save button.
    browser.vitClickXP(PurchaseInvoice.PurchaseInvoiceScreen_button_Save,'Save button','System should create purchase invoice with user specified details.')
    print_('Clicked on save button.')
    wait(5)
    print_('Successfully created purchase invoice')
    browser.vitAcceptAlert('','')

    # Clicking on escape button
    # browser.vitClickXP(Common_Xpaths.Common_button_escapeButton,'Escape button','Print window should be closed.')
    # wait(ThreeSec)
    browser.vitSStoDoc(TC_ID,'Purchase invoice created Successfully to add stock for selected items for preferred customer.')
    # waitUntilElementVisible(Transaction.TransactionModule_hoverDropdown_Inventory)
    wait(2)
    browser.vitHeading(TC_ID + " - TEST PASSED",4)
    browser.vitDocSave(VitPySelEnv.vWebDriver + '_' + TC_ID+ '_' +"Purchase Invoice")
    browser.vitTestCasePath(VitPySelEnv.tcDIR+'/'+TC_ID+'.csv')


def execute():
    launchApplication()
    login()
    purchaseInvoice()

execute()