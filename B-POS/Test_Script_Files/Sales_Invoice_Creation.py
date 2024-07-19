import VitPySelEnv
from VitPySelLibV2 import VitSelWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Xpath_Files import LoginScreen
from Xpath_Files import HomeScreen
from Xpath_Files import Transaction
from Xpath_Files import SalesInvoice

# ****** Test case data ****** #
browser = VitSelWebDriver(VitPySelEnv.vWebDriver)
waitTime = 1
TC_ID = "TC_03"
TC_Name = "Sales_Invoice_Creation"
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





def salesInvoice():

    navigatingToTransactionModule()
    

    # Navigating to Sales invoice screen.
    browser.vitMouseOverClickXP(Transaction.TransactionModule_hoverDropdown_Sales,Transaction.Sales_link_salesInvoice,'System should navigate user to Sales Invoice screen.')
    wait(4)
    print_('Successfully navigated to sales invoice screen.')
    browser.vitSStoDoc(TC_ID,'Sales invoice page, The sales invoice screen is where sales transactions are recorded and processed.')
    waitUntilElementVisible(SalesInvoice.SalesInvoice_SelectionBox_Customer)


    # Performing ENTER on customer selection box.
    browser.vitENTER(SalesInvoice.SalesInvoice_SelectionBox_Customer,'customers pop-up window should display.')
    print_('Performed ENTER on customer selection box.')
    waitUntilElementVisible(SalesInvoice.SalesInvoice_input_customer_EnterKeywordToSearch)


    # Entering customer name in Item pop-up window.
    browser.vitTextInputXP(SalesInvoice.SalesInvoice_input_customer_EnterKeywordToSearch,'Atharav','Customer name')
    wait(3)
    print_('Successfully entered customer name')

    # Performing ENTER operation on customer search field.
    browser.vitENTER(SalesInvoice.SalesInvoice_input_customer_EnterKeywordToSearch,'Should select preferred customer for sales invoice.')
    print_('Preformed ENTER on search field of customer modal window')
    waitUntilElementVisible(SalesInvoice.SalesInvoice_button_F10)

    # Clicking on F10 button.
    browser.vitClickXPWithJavaScript(SalesInvoice.SalesInvoice_button_F10,'F10','F10 modal window should be open.')
    print_('Clicked on F10 button.')
    waitUntilElementVisible(SalesInvoice.SalesInvoice_dropdown_BillSeries)

    # Selecting value from Bill series dropdown.
    browser.vitDropDownTextXP(SalesInvoice.SalesInvoice_dropdown_BillSeries,'0','Bill series')
    print_('Selected value from Bill series dropdown')

    # Clicking on F10 button to close.
    browser.vitClickXPWithJavaScript(SalesInvoice.SalesInvoice_button_F10,'F10','F10 modal window should close.')
    print_('Clicked on F10 button to close it.')
    waitUntilElementVisible(SalesInvoice.SalesInvoice_input_ItemCode)


    # Performing enter operation on Item code item field.
    browser.vitENTER(SalesInvoice.SalesInvoice_input_ItemCode,'Items pop-up window should display.')
    print_('Performed ENTER on intem code selectino box')
    waitUntilElementVisible(SalesInvoice.SalesInvoice_input_Item_Enter_Keyword_to_Search)

    # Entering item name in search field of Items modal window.
    browser.vitTextInputXP(SalesInvoice.SalesInvoice_input_Item_Enter_Keyword_to_Search,'Orient _Ceiling Fan','Item Name')
    wait(3)
    print_('Entered item name in search field of Items modal window.')
    # waitUntilElementVisible(SalesInvoice.SalesInvoice_input_Item_Enter_Keyword_to_Search)

    browser.vitENTER(SalesInvoice.SalesInvoice_input_Item_Enter_Keyword_to_Search,'System should selected product specified by user.')
    waitUntilElementVisible(SalesInvoice.SalesInvoice_input_Batch)
    print_('Successfully selected Item.')

    # Performing ENTER on Batch number selection box field.
    browser.vitENTER(SalesInvoice.SalesInvoice_input_Batch,'System should display all existing batch numbers for specified product.')
    # waitUntilElementVisible(SalesInvoice.SalesInvoice_input_Avl_Quantity)
    wait(5)

    # Selecting batch.
    browser.vitDoubleClickXP(SalesInvoice.SalesInvoice_link_2nd_batch,'Second_Batch','System should select preferred batch by user from listed batches.')
    print_('Selected existing batch')
    waitUntilElementVisible(SalesInvoice.SalesInvoice_input_quantity)

    

    # Entering quantity.
    browser.vitTextInputENTERXP(SalesInvoice.SalesInvoice_input_quantity,'1','Quantity')
    print_('Entered Quantity of item.')
    waitUntilElementVisible(SalesInvoice.SalesInvoice_button_Save)

    # Clicking on save button.
    browser.vitClickXP(SalesInvoice.SalesInvoice_button_Save,'Save button','System should populate Available schems window')
    print_('Clicked on SAVE button.')
    browser.Vit_wait_for_element_visibility(SalesInvoice.SalesInvoice_input_CashTender)

    # waitUntilElementVisible(SalesInvoice.SalesInvoice_button_availbleSchems_Apply)

    # # clicking on apply button of available tenders window.
    # browser.vitClickXPWithJavaScript(SalesInvoice.SalesInvoice_button_availbleSchems_Apply,'Apply button','should populate tenders window.')
    # print_('Clicked on apply button of available tenders window.')
    # waitUntilElementVisible(SalesInvoice.SalesInvoice_input_CashTender)


    # Performing ENTER on cash tender input field..
    browser.vitENTER(SalesInvoice.SalesInvoice_input_CashTender,'Sales invoice total should populate in cash tender fields.')
    print_('Performed ENTER operation on cash tender field.')


    # Clicking on save button of cash tender.
    browser.vitENTER(SalesInvoice.SalesInvoice_button_Cash_Tender_Save,'System should create sales invoice with user specified details.')
   
    wait(5)

    # Accepting alert.
    browser.vitAcceptAlert('','')
    browser.vitSStoDoc(TC_ID,'Successfully created sales invoice for specified product with unbatched batch of items.')

    
    waitUntilElementVisible(HomeScreen.HomeScreen_link_Reports)
    print('=================Successfully created sales invoice ===================')

    browser.vitHeading(TC_ID + " - TEST PASSED",4)
    browser.vitDocSave(VitPySelEnv.vWebDriver + '_' + TC_ID+ '_' +"Sales Invoice")
    browser.vitTestCasePath(VitPySelEnv.tcDIR+'/'+TC_ID+'_'+TC_Name+'.csv')


def execute():
    launchApplication()
    login()
    salesInvoice()

execute()