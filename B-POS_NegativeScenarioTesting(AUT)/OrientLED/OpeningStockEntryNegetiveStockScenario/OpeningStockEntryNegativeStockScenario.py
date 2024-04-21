import VitPySelEnv
from VitPySelLibV2 import VitSelWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Xpath_Files import LoginScreen
from Xpath_Files import HomeScreen
from Xpath_Files import Masters
from Xpath_Files import ProductMaster
from Xpath_Files import Transaction
from Xpath_Files import PurchaseInvoice
from Xpath_Files import OpeningStockEntry
from Xpath_Files import Common_Xpaths

browser = VitSelWebDriver(VitPySelEnv.vWebDriver)
waitTime = 1
TC_ID = "TC_01"
TC_Name = "Opening_Stock_Entry_Negative_Stock_Testing"
browser.vitTCHeading(VitPySelEnv.vWebDriver + "_" + TC_ID + ":" + TC_Name)

#============ Data needed for test case ============#
ItemName = 'Orient Charger 20V'
ItemCode = 10031
BatchNumber = 'BA_01'
Quantity  = 10
MRP = 125
LandingCost = 110
InvoiceNumber = 'TI1138AAA2324'
BatchNumber='Batch_01'

BatchNumberForOpeningStockEdit = 'BA_02'

#=========================================================================================================================#

# ================== Time management variables ==========================#
OneSec = 1
ThreeSec = 3
FiveSec = 5
TenSec = 10

# browser.vitSStoDoc(TC_ID,'Bpos sahakari Supplier List window ')


# ========================================================================================================================#


def wait(time):
    browser.vitWait(time)
# ========================================================================================================================#
def print_(message):
    print('------------',message,'--------------')
# ========================================================================================================================#

def waitUntilElementVisible(element):
    browser.wait_for_element_visibility(element)


def launchApplication():
    
    browser.vitLaunchUrl(VitPySelEnv.URL)
    browser.vitWait(FiveSec)
    print('----- application launched successfully -----')
    browser.vitMaxmizeScreen()
    print('------ successfully maximized browser window ------')
    browser.vitWait(OneSec)
# ========================================================================================================================#
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
# ========================================================================================================================#
def navigatingToTransactionModule():
    # Clicking on Transaction Component.
    browser.vitClickXP(HomeScreen.HomeScreen_link_Transactions,'Transactions module link','System should display transaction inner menu.')
    print('------ Successfully clicked on Transaction module ------')
    waitUntilElementVisible(HomeScreen.HomeScreen_link_Masters)

def createProduct():

    # Ciclking on Masters link.
    browser.vitClickXP(HomeScreen.HomeScreen_link_Masters,'masters link','System should display master related options under the ribbion menu.')
    print('----- Successfully clicked on Masters link ---------')
    waitUntilElementVisible(Masters.MastersScreen_hover_dropdown_InventoryInfo)
    
    # Clicking on product master.
    
    browser.vitMouseOverClickXP(Masters.MastersScreen_hover_dropdown_InventoryInfo,Masters.MastersScreen_link_ProductMaster,'Inventory Info tab','Product master link','System should navigate user to Product master page.')
    print('------- Successfully clicked Product Master link ---------')
    browser.vitWait(FiveSec)
    browser.vitSStoDoc(TC_ID,'Product master page which enables users to view, manage, and create new products.')
    waitUntilElementVisible(ProductMaster.ProductMasterScreen_input_EconmmDesc)

    # Clicking on Econm Desc element.
    browser.vitClickXP(ProductMaster.ProductMasterScreen_input_EconmmDesc,'Econm Input box','System should allow user to enter data in Econm field.')
    waitUntilElementVisible(ProductMaster.ProductMasterScreen_button_AddProduct)


    #Clicking on 'Add product' button.
    browser.vitClickXP(ProductMaster.ProductMasterScreen_button_AddProduct,'Add Product','System should navigate user to Product Master > General screen.')
    print('------ Successful clicked on Add Product button ------')
    wait(ThreeSec)
    browser.vitSStoDoc(TC_ID,'Product master forum General details page, Product master page with different tabs such GENERAL, ALTERNATIVE UNITS, SALES, GST & CHARGES, CATEGORY, OTHERS, PRICE.')
    waitUntilElementVisible(ProductMaster.ProductMasterScreen_input_Name)
    
    # # Entering Mcode in Alias code field.
    # browser.vitTextInputXP(ProductMaster.ProductMasterScreen_input_Alias_Code,ItemCode,'Alias code input field.')
    # print('------ Successfully entered Mcode in Alias code -------')
    # wait(ThreeSec)

    # Entering Name of product.
    browser.vitTextInputXP(ProductMaster.ProductMasterScreen_input_Name,ItemName,'Product Name')
    waitUntilElementVisible(ProductMaster.productMasterScreen_tab_GST_and_Charges)
    print('---- Successfully entered Product Name ------')

    # Switching to 'Gst & Charges' tab.
    browser.vitClickXP(ProductMaster.productMasterScreen_tab_GST_and_Charges,'GST & Charges Tab','System should switch user to GST & Charges Tab.')
    print('------ Successfully switched to GST & Charges tab.------')
    waitUntilElementVisible(ProductMaster.ProductMasterScreen_dropdown_GST_Rate)

    # Selecting GST rate.
    browser.vitDropDownTextXP(ProductMaster.ProductMasterScreen_dropdown_GST_Rate,'1','GST Rate')
    print('------ Successfully selected GST rate from GST dropdown -----')
    waitUntilElementVisible(ProductMaster.ProductMasterScreen_input_HSN_Code)


    """
    Note: Due to no proper HTML element for 'GST Type' I opt workaround way to select value from 'GST type' dropdown.

    """

    # # Selecting GST type.
    # browser.vitTAB(ProductMaster.ProductMasterScreen_dropdown_GST_Rate)
    # wait(OneSec)
    # browser.simulate_enter()
    # wait(ThreeSec)
    # browser.simulate_enter()
    # print('------- Successfully selected GST Type from dropdown ------ ')
    # wait(ThreeSec)

    # Entering HSN Code
    browser.vitTextInputXP(ProductMaster.ProductMasterScreen_input_HSN_Code,ItemCode,'HSN code')
    print('------ Successsfully entered HSN code ------')
    waitUntilElementVisible(ProductMaster.ProductMasterScreen_Tab_Price)

    # Switching to price tab.
    browser.vitClickXP(ProductMaster.ProductMasterScreen_Tab_Price,'Price Tab','System should switch user to PRICE TAB.')
    print('---- Successfully switched to price tab -----')
    waitUntilElementVisible(ProductMaster.ProductMasterScreen_input_MRP)

    # Entering MRP price.
    browser.vitTextInputXP(ProductMaster.ProductMasterScreen_input_MRP,MRP,'MRP price')
    print('---- Successfully entered MRP price.')
    waitUntilElementVisible(ProductMaster.ProductMasterScreen_input_LandingCost)

    # Entering Landing Cost.
    browser.vitTextInputXP(ProductMaster.ProductMasterScreen_input_LandingCost,LandingCost,'Landing Cost')
    print('------ Successfully entered Landing Cost -----')
    waitUntilElementVisible(ProductMaster.ProductMasterScreen_button_save)

    # Clicking on Save button.
    browser.vitClickXP(ProductMaster.ProductMasterScreen_button_save,'Save button','System should create a new product with specified details in database.')
    print('------ Clicked on Save button ------')
    wait(ThreeSec)
    browser.vitSStoDoc(TC_ID,'Successfully created new product, with given details.')
    

    print('=========== Successfully created product ',ItemName,' in System')
# ========================================================================================================================#
def purchaseInvoice():
    
    navigatingToTransactionModule()

    # Clicking on Purchase Invoice link
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
    wait(2)
    browser.vitENTER(PurchaseInvoice.PurchaseInvoiceScreen_input_Suppliers_EnterKeyWordToSearch,'System should select user specified supplier.')
    waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_input_InvoiceNumber)
    

    
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
    browser.vitTextInputXP(PurchaseInvoice.PurchaseInvoiceScreen_input_Item_EnterKeywordToSearch,ItemName,'Item Name')
    # waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_input_Item_EnterKeywordToSearch)
    wait(3)
    print_('Item name entered successfully')


    #performing enter operation in EnterKeywordToSearch field.
    browser.vitENTER(PurchaseInvoice.PurchaseInvoiceScreen_input_Item_EnterKeywordToSearch,'System should select specified item successfully')
    waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_input_batchNumber)
    print_('Item selected successfully')

    # Entering batch number
    browser.vitTextInputXP(PurchaseInvoice.PurchaseInvoiceScreen_input_batchNumber,BatchNumber,'Batch number')
    waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_input_manufacturerDate)
    print_('Successfully entered Batch number')

    # Entering manufacturing date.
    browser.vitTextInputXP(PurchaseInvoice.PurchaseInvoiceScreen_input_manufacturerDate,'09/10/2023','Manufacturing Date')
    waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_input_expireyDate)
    print_('Successfully entered manufacturing date')

    # Entering expiry date.
    browser.vitTextInputXP(PurchaseInvoice.PurchaseInvoiceScreen_input_expireyDate,'09/10/2029','Expiry Date')
    waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_input_quantity)
    print_('Successfully entered expired date')

    # Entering quantity .
    browser.vitTextInputXP(PurchaseInvoice.PurchaseInvoiceScreen_input_quantity,'10','Item quantity')
    waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_input_quantity)
    print_('Successfully entered quantity')

    browser.vitENTER(PurchaseInvoice.PurchaseInvoiceScreen_input_quantity,'Prices and discounts should populate appropriately in respective fields.')
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
    waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_input_invoice_amount)
    print_('Clicked on F1 details button.')
    

    # Entering amount in Invoice amount field.
    browser.vitTextInputXP(PurchaseInvoice.PurchaseInvoiceScreen_input_invoice_amount,truncated_Total,'Invoice amount')
    waitUntilElementVisible(PurchaseInvoice.PurchaseInvoiceScreen_button_Save)
    print_('Successfully entered invoice amount')

    # Clicking on save button.
    browser.vitClickXP(PurchaseInvoice.PurchaseInvoiceScreen_button_Save,'Save button','System should create purchase invoice with user specified details.')
    wait(5)
    print_('Successfully created purchase invoice')

    # Clicking on escape button
    # browser.vitClickXP(Common_Xpaths.Common_button_escapeButton,'Escape button','Print window should be closed.')
    # wait(ThreeSec)
    browser.vitSStoDoc(TC_ID,'Purchase invoice created Successfully to add stock for selected item:',ItemName)
    # waitUntilElementVisible(Transaction.TransactionModule_hoverDropdown_Inventory)
    wait(5)

# ========================================================================================================================#


def CreatingNewBatchWithOpeningStockEntry():

    
    # Navigating to Opening stock entry
    browser.vitMouseOverClickXP(Transaction.TransactionModule_hoverDropdown_Inventory,Transaction.Inventory_link_OpeningStockEntry,'Inventory dropdown','System should navigate user to Opening stock entry screen.')
    wait(ThreeSec)
    print_('Successfully clicked on Opening stock entry link')
    browser.vitSStoDoc(TC_ID,'Opening stock entry page, where user can create a new stock for preferred items.')
    waitUntilElementVisible(OpeningStockEntry.OpeningStockEntry_selectionBox_ItemCode)
    
    # Selecting Item.
        # Entering Item code.
    browser.vitENTER(OpeningStockEntry.OpeningStockEntry_selectionBox_ItemCode,'System should display Items Pop_up window.')
    # waitUntilElementVisible(OpeningStockEntry.OpeningStockEntry_input_Item_KeywordToSearch)
    wait(4)
    browser.vitTextInputXP(OpeningStockEntry.OpeningStockEntry_input_Item_KeywordToSearch,ItemName,'Item Name')
    # waitUntilElementVisible(OpeningStockEntry.OpeningStockEntry_input_Item_KeywordToSearch)
    wait(3)
    print_('Successfully entered item name')

    browser.vitENTER(OpeningStockEntry.OpeningStockEntry_input_Item_KeywordToSearch,'System should populate details of selected Product.')
    waitUntilElementVisible(OpeningStockEntry.OpeningStockEntry_input_manufacturerDate)

    # Entering manufacturing date.
    browser.vitTextInputXP(OpeningStockEntry.OpeningStockEntry_input_manufacturerDate,'09/10/2023','Manufacturing Date')
    waitUntilElementVisible(OpeningStockEntry.OpeningStockEntry_input_expireyDate)
    print_('Successfully entered manufacturing date')

        # Entering expiry date.
    browser.vitTextInputXP(OpeningStockEntry.OpeningStockEntry_input_expireyDate,'09/10/2029','Expiry Date')
    waitUntilElementVisible(OpeningStockEntry.OpeningStockEntry_input_quantity)
    print_('Successfully entered expired date')

        # Entering quantity .
    browser.vitTextInputXP(OpeningStockEntry.OpeningStockEntry_input_quantity,Quantity,'quantity')
    waitUntilElementVisible(OpeningStockEntry.OpeningStockEntry_input_quantity)
    print_('Successfully entered quantity')
    browser.vitENTER(OpeningStockEntry.OpeningStockEntry_input_quantity,'Prices and discounts should populate appropriately in respective fields.')
    waitUntilElementVisible(OpeningStockEntry.OpeningStockEntry_selectionBox_SupplierBox)


    """
    Note:
    ----
    Tried to give new values for MRP, cost price and selling price but encountered issue to clear previously existing values in those fields so leaving them as they are.
    """

    # Selecting Supplier.
    browser.vitENTER(OpeningStockEntry.OpeningStockEntry_selectionBox_SupplierBox,'System should display Suppliers pop-up window')
    print_('Successfully performed Enter Operation on Supplier box')
    waitUntilElementVisible(OpeningStockEntry.OpeningStockEntry_input_Supplier_KeywordToSearch)
    browser.vitTextInputENTERXP(OpeningStockEntry.OpeningStockEntry_input_Supplier_KeywordToSearch,'ASHUTOSH MARKETING','Supplier Name')
    print_('Successfully entered supplier name')
    waitUntilElementVisible(OpeningStockEntry.OpeningStockEntry_button_Save)

        # Clicking on save button.
    browser.vitClickXP(OpeningStockEntry.OpeningStockEntry_button_Save,'Save button','System should create new batch for selected item or items.')
    wait(5)
    browser.vitSStoDoc(TC_ID,'Successfully created new batch for specified item using Opening Stock Entry.')
    waitUntilElementVisible(HomeScreen.HomeScreen_link_Transactions)


    print("======================== Successfully created Opening Stock Entry ==================================")
    #========================================================================================================================#
    

from Xpath_Files import SalesInvoice
def salesInvoice():

    navigatingToTransactionModule()
    

    # Navigating to Sales invoice screen.
    browser.vitMouseOverClickXP(Transaction.TransactionModule_hoverDropdown_Sales,Transaction.Sales_link_salesInvoice,'System should navigate user to Sales Invoice screen.')
    print_('Successfully navigated to sales invoice screen.')
    wait(FiveSec)
    browser.vitSStoDoc(TC_ID,'Sales invoice page, The sales invoice screen is where sales transactions are recorded and processed.')
    waitUntilElementVisible(SalesInvoice.SalesInvoice_SelectionBox_Customer)


    # Selecting Customer
    browser.vitENTER(SalesInvoice.SalesInvoice_SelectionBox_Customer,'customers pop-up window should display.')
    waitUntilElementVisible(SalesInvoice.SalesInvoice_input_customer_EnterKeywordToSearch)
    # Entering customer name in Item pop-up window.
    browser.vitTextInputENTERXP(SalesInvoice.SalesInvoice_input_customer_EnterKeywordToSearch,'Dileep','Customer name')
    print_('Successfully entered customer name')
    waitUntilElementVisible(SalesInvoice.SalesInvoice_input_ItemCode)

    # Selecting item code.
    browser.vitENTER(SalesInvoice.SalesInvoice_input_ItemCode,'Items pop-up window should display.')
    # waitUntilElementVisible(SalesInvoice.SalesInvoice_input_Item_Enter_Keyword_to_Search)
    wait(4)
    browser.vitTextInputXP(SalesInvoice.SalesInvoice_input_Item_Enter_Keyword_to_Search,ItemName,'Item Name')
    # waitUntilElementVisible(SalesInvoice.SalesInvoice_input_Item_Enter_Keyword_to_Search)
    wait(3)
    browser.vitENTER(SalesInvoice.SalesInvoice_input_Item_Enter_Keyword_to_Search,'System should selected product specified by user.')
    waitUntilElementVisible(SalesInvoice.SalesInvoice_input_Batch)
    print_('Successfully selected Item.')

    # Selecting Batch number.
    browser.vitENTER(SalesInvoice.SalesInvoice_input_Batch,'System should display all existing batch numbers for specified product.')
    # waitUntilElementVisible(SalesInvoice.SalesInvoice_input_Avl_Quantity)
    wait(5)

    # capturing available stock
    availableStock = browser.vitCaptureLabelText(SalesInvoice.SalesInvoice_label_availabelStockInBatchRecord)
    waitUntilElementVisible(SalesInvoice.SalesInvoice_link_2nd_batch)

    # browser.vitClickXP(SalesInvoice.SalesInvoice_link_2nd_batch,'-------')
    # wait(ThreeSec)

    # browser.vitENTER(SalesInvoice.SalesInvoice_link_2nd_batch,'System should select batch number that intended to select.')
    # wait(FiveSec)
    # print_('Successfully selected batch')

    browser.vitDoubleClickXP(SalesInvoice.SalesInvoice_link_2nd_batch,'Second_Batch','System should select preferred batch by user from listed batches.')
    waitUntilElementVisible(SalesInvoice.SalesInvoice_input_quantity)
    

    # Entering quantity.
    browser.vitTextInputENTERXP(SalesInvoice.SalesInvoice_input_quantity,availableStock,'available stock')
    print_('Successfully entered stock.')
    waitUntilElementVisible(SalesInvoice.SalesInvoice_button_Save)

    
    # Saving sales invoice.
    browser.vitClickXP(SalesInvoice.SalesInvoice_button_Save,'Save button','System should populate cash tender window.')
    wait(ThreeSec)

    # Entering amount in cash tender account.
    browser.vitENTER(SalesInvoice.SalesInvoice_input_CashTender,'Sales invoice total should populate in cash tender fields.')
    waitUntilElementVisible(SalesInvoice.SalesInvoice_button_Cash_Tender_Save)

    # Clicking on save button of cash tender.
    browser.vitENTER(SalesInvoice.SalesInvoice_button_Cash_Tender_Save,'System should create sales invoice with user specified details.')
    wait(ThreeSec)
    # Clicking on escape button
    # browser.vitClickXP(Common_Xpaths.Common_button_escapeButton,'Escape button','Print window should be closed.')
    # wait(ThreeSec)
    browser.vitSStoDoc(TC_ID,'Successfully created sales invoice for specified product with unbatched batch of items.')
    waitUntilElementVisible(HomeScreen.HomeScreen_link_Reports)
    print('=================Successfully created sales invoice ===================')


    # 

from Xpath_Files import Reports
def reportsGeneration():
    # Navigating to Reports module.
    browser.vitClickXP(HomeScreen.HomeScreen_link_Reports,'Reports Link','System should navigate user to Reports module.')
    waitUntilElementVisible(Reports.Reports_hoverDropdown_InventoryReports)
    print_('Successfully navigate to Reports screen')
    

    # Navigating to closing stock reports.
    browser.vitMouseOverClickXP(Reports.Reports_hoverDropdown_InventoryReports,Reports.Reports__link_AnalysisReports,'System should display all sub-reports under Analysis Reports')
    waitUntilElementVisible(Reports.Reports__link_ClosingStockReport)
    browser.vitClickXP(Reports.Reports__link_ClosingStockReport,'Closing stock report link','System should navigate user to Closing stock report screen.')
    print_('Successfully navigated to Closing Stock Reports')
    wait(ThreeSec)
    browser.vitSStoDoc(TC_ID,'Closing stock report screen, where user can generate reports for all existing products in application.')
    wait(ThreeSec)

    # Generating last 7 days reports
    browser.vitClickXP(Reports.ClosingStockReport_datepicker_DateSelection,'Date Picker','System should display Calander')
    waitUntilElementVisible(Reports.ClosingStockReport_button_last7days)
    print_('Successfully displayed Calander')
    

    browser.vitClickXP(Reports.ClosingStockReport_button_last7days,'Last 7 days filter button','System should select past 7 days in date selection calander.')
    waitUntilElementVisible(Reports.ClosingStockReport_button_RunButton)
    print_('Successfully clicked on last 7 days reports.')

    browser.vitClickXP(Reports.ClosingStockReport_button_RunButton,'Run Button','System should fetch and display reports in specified date range.')
    waitUntilElementVisible(Reports.ClosingStockReport_input_SearchInReport)
    print('Successfully clicked on RUN button.')
    wait(15)

    browser.vitTextInputXP(Reports.ClosingStockReport_input_SearchInReport,ItemName,'Item Name')
    print_('Successfully entered Item Name in Search In Report input field.')

    print_('Successfully generated Reports')
    wait(FiveSec)
    browser.vitSStoDoc(TC_ID,'last 7 days reports for specified product.')
    waitUntilElementVisible(HomeScreen.HomeScreen_link_Transactions)

def OpeningStockBatchEdit():

    # Clicking on Transaction Component.
    browser.vitClickXP(HomeScreen.HomeScreen_link_Transactions,'Transaction link','Transaction')
    print('------ Successfully clicked on Transaction module ------')
    waitUntilElementVisible(Transaction.TransactionModule_hoverDropdown_Inventory)


    # Navigating to Opening stock entry
    browser.vitMouseOverClickXP(Transaction.TransactionModule_hoverDropdown_Inventory,Transaction.Inventory_link_OpeningStockEntry,'Inventory dropdown','System should navigate to Opening stock entry screen.')
    wait(ThreeSec)
    print_('Successfully clicked on Opening stock entry link')
    browser.vitSStoDoc(TC_ID,'Navigated to Opening Stock Entry to give batch name for previously created unbatched batch')
    waitUntilElementVisible(OpeningStockEntry.OpeningStockEntry_button_edit)

    # Clicking on Edit button.
    browser.vitClickXP(OpeningStockEntry.OpeningStockEntry_button_edit,'System should display all available Opening stock entry records.')
    wait(ThreeSec)
    print_('Successfully clicked on edit button')
    waitUntilElementVisible(OpeningStockEntry.OpeningStockEntry_label_voucherNumber)


    # selecting first record.
    browser.vitDoubleClickXP(OpeningStockEntry.OpeningStockEntry_label_voucherNumber,'Opening Stock latest record','System should redirect to edit screen of selected record.')
    waitUntilElementVisible(OpeningStockEntry.OpeningStockEntry_Input_BatchNumber)
    print_('Successfully selected first record')

    # # Accepting alert to load selected bill.
    # browser.vitAcceptAlert('Load Bill alert','System should load selected bill.')
    # wait(FiveSec)

    # Entering new batch number.
    browser.vitTextInputXP(OpeningStockEntry.OpeningStockEntry_Input_BatchNumber,'Batch_02','Batch number')
    print_('Successfully entered new batch number')
    waitUntilElementVisible(OpeningStockEntry.OpeningStockEntry_button_Save)
      

    # Saving edited voucher
    browser.vitClickXP(OpeningStockEntry.OpeningStockEntry_button_Save,'Save Button','System should not allow user to save Opening Stock Entry record.')
    print_('Successfylly clicked on save button.')
    wait(2)
    browser.vitSStoDoc(TC_ID,"System is not allowing to edit and save Opening Stock Entry record which don't have any available stock.")
    wait(FiveSec)


    browser.vitHeading(TC_ID + " - TEST PASSED",4)
    browser.vitDocSave(VitPySelEnv.vWebDriver + '_' + TC_ID)
    browser.vitTestCasePath(VitPySelEnv.tcDIR+'/'+TC_ID+'.csv')



   


def execute():
    
    launchApplication()
    login()
    createProduct()

    purchaseInvoice()
    CreatingNewBatchWithOpeningStockEntry()
    salesInvoice()
    reportsGeneration()
    OpeningStockBatchEdit()
    reportsGeneration()


     

execute()
    
