import sys
from collections import defaultdict

#cubo semantico sirve para cuando se hacen operaciones aritmeticas, logicas, comparaciones, asignaciones

#para inicializar el dicionario, defaultdict es una clase de colections
cuboSemantico = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))
	
##############################################################
############ PLUS ##########################################
cuboSemantico['int']['int']['+'] = 'int' #int con int
cuboSemantico['int']['float']['+'] = 'float' # int con float
cuboSemantico['float']['int']['+'] = 'float'

cuboSemantico['int']['char']['+'] = 'error' # int con char
cuboSemantico['char']['int']['+'] = 'error'

cuboSemantico['char']['float']['+'] = 'error' 
cuboSemantico['float']['char']['+'] = 'error'  # float con char

cuboSemantico['float']['float']['+'] = 'float'  # float con float

cuboSemantico['char']['char']['+'] = 'error' # char con char



# ############################################################
# ############ MINUS #############################################
cuboSemantico['int']['int']['-'] = 'int' #int con int

cuboSemantico['int']['float']['-'] = 'float' # int con float
cuboSemantico['float']['int']['-'] = 'float'

cuboSemantico['int']['char']['-'] = 'error' # int con char
cuboSemantico['char']['int']['-'] = 'error'

cuboSemantico['char']['float']['-'] = 'error' 
cuboSemantico['float']['char']['-'] = 'error'  # float con char

cuboSemantico['float']['float']['-'] = 'float'  # float con float

cuboSemantico['char']['char']['-'] = 'error' # char con char




# ############################################################
# ############# MULTIPLICATION ##############################
cuboSemantico['int']['int']['*'] = 'int' #int con int

cuboSemantico['int']['float']['*'] = 'float' # int con float
cuboSemantico['float']['int']['*'] = 'float'

cuboSemantico['int']['char']['*'] = 'error' # int con char
cuboSemantico['char']['int']['*'] = 'error'

cuboSemantico['char']['float']['*'] = 'error' 
cuboSemantico['float']['char']['*'] = 'error'  # float con char

cuboSemantico['float']['float']['*'] = 'float'  # float con float

cuboSemantico['char']['char']['*'] = 'error' # char con char





# ##########################################################
# ############ DIVISION #######################################
cuboSemantico['int']['int']['/'] = 'float' #int con int

cuboSemantico['int']['float']['/'] = 'float' # int con float
cuboSemantico['float']['int']['/'] = 'float'

cuboSemantico['int']['char']['/'] = 'error' # int con char
cuboSemantico['char']['int']['/'] = 'error'

cuboSemantico['char']['float']['/'] = 'error' 
cuboSemantico['float']['char']['/'] = 'error'  # float con char

cuboSemantico['float']['float']['/'] = 'float'  # float con float

cuboSemantico['char']['char']['/'] = 'error' # char con char




# #############################################################
# ################## GREATER THAN #############################
cuboSemantico['int']['int']['>'] = 'bool' #int con int

cuboSemantico['int']['float']['>'] = 'bool' # int con float
cuboSemantico['float']['int']['>'] = 'bool'

cuboSemantico['int']['char']['>'] = 'error' # int con char
cuboSemantico['char']['int']['>'] = 'error'

cuboSemantico['char']['float']['>'] = 'error' 
cuboSemantico['float']['char']['>'] = 'error'  # float con char

cuboSemantico['float']['float']['>'] = 'bool'  # float con float

cuboSemantico['char']['char']['>'] = 'error' # char con char




# #############################################################
# ############### LESS THAN #####################################
cuboSemantico['int']['int']['<'] = 'bool' #int con int

cuboSemantico['int']['float']['<'] = 'bool' # int con float
cuboSemantico['float']['int']['<'] = 'bool'

cuboSemantico['int']['char']['<'] = 'error' # int con char
cuboSemantico['char']['int']['<'] = 'error'

cuboSemantico['char']['float']['<'] = 'error' 
cuboSemantico['float']['char']['<'] = 'error'  # float con char

cuboSemantico['float']['float']['<'] = 'bool'  # float con float

cuboSemantico['char']['char']['<'] = 'error' # char con char





# ###############################################################
# ############### GREATER EQUAL THAN ##############################
cuboSemantico['int']['int']['=>'] = 'bool' #int con int

cuboSemantico['int']['float']['=>'] = 'bool' # int con float
cuboSemantico['float']['int']['=>'] = 'bool'

cuboSemantico['int']['char']['=>'] = 'error' # int con char
cuboSemantico['char']['int']['=>'] = 'error'

cuboSemantico['char']['float']['=>'] = 'error' 
cuboSemantico['float']['char']['=>'] = 'error'  # float con char

cuboSemantico['float']['float']['=>'] = 'bool'  # float con float

cuboSemantico['char']['char']['=>'] = 'error' # char con char




# ####################################################################
# ############### LESS EQUAL THAN ###############################
cuboSemantico['int']['int']['<='] = 'bool' #int con int

cuboSemantico['int']['float']['<='] = 'bool' # int con float
cuboSemantico['float']['int']['<='] = 'bool'

cuboSemantico['int']['char']['<='] = 'error' # int con char
cuboSemantico['char']['int']['<='] = 'error'

cuboSemantico['char']['float']['<='] = 'error' 
cuboSemantico['float']['char']['<='] = 'error'  # float con char

cuboSemantico['float']['float']['<='] = 'bool'  # float con float

cuboSemantico['char']['char']['<='] = 'error' # char con char




# #################################################################
# ################ DIFERENT NOT EQUAL ############################
cuboSemantico['int']['int']['<>'] = 'bool' #int con int

cuboSemantico['int']['float']['<>'] = 'bool' # int con float
cuboSemantico['float']['int']['<>'] = 'bool'

cuboSemantico['int']['char']['<>'] = 'error' # int con char
cuboSemantico['char']['int']['<>'] = 'error'

cuboSemantico['char']['float']['<>'] = 'error' 
cuboSemantico['float']['char']['<>'] = 'error'  # float con char

cuboSemantico['float']['float']['<>'] = 'bool'  # float con float

cuboSemantico['char']['char']['<>'] = 'bool' # char con char



# ##################################################################
# ################ AND ##############################################
cuboSemantico['int']['int']['&'] = 'bool' #int con int

cuboSemantico['int']['float']['&'] = 'bool' # int con float
cuboSemantico['float']['int']['&'] = 'bool'

cuboSemantico['int']['char']['&'] = 'error' # int con char
cuboSemantico['char']['int']['&'] = 'error'

cuboSemantico['char']['float']['&'] = 'error' 
cuboSemantico['float']['char']['&'] = 'error'  # float con char

cuboSemantico['float']['float']['&'] = 'bool'  # float con float

cuboSemantico['char']['char']['&'] = 'error' # char con char



# ##################################################################
# ############## OR ###################################################
cuboSemantico['int']['int']['|'] = 'bool' #int con int

cuboSemantico['int']['float']['|'] = 'bool' # int con float
cuboSemantico['float']['int']['|'] = 'bool'

cuboSemantico['int']['char']['|'] = 'error' # int con char
cuboSemantico['char']['int']['|'] = 'error'

cuboSemantico['char']['float']['|'] = 'error' 
cuboSemantico['float']['char']['|'] = 'error'  # float con char

cuboSemantico['float']['float']['|'] = 'bool'  # float con float

cuboSemantico['char']['char']['|'] = 'error' # char con char



# ######################################################################
# ############# EQUAL ##################################################
cuboSemantico['int']['int']['='] = 'int' #int con int

cuboSemantico['int']['float']['='] = 'float' # int con float
cuboSemantico['float']['int']['='] = 'float'

cuboSemantico['int']['char']['='] = 'error' # int con char
cuboSemantico['char']['int']['='] = 'error'

cuboSemantico['char']['float']['='] = 'error' 
cuboSemantico['float']['char']['='] = 'error'  # float con char

cuboSemantico['float']['float']['='] = 'float'  # float con float

cuboSemantico['char']['char']['='] = 'char' # char con char

######################################################################
############# EQUAL EQUAL ##################################################
cuboSemantico['int']['int']['=='] = 'bool' #int con int

cuboSemantico['int']['float']['=='] = 'bool' # int con float
cuboSemantico['float']['int']['=='] = 'bool'

cuboSemantico['int']['char']['=='] = 'error' # int con char
cuboSemantico['char']['int']['=='] = 'error'

cuboSemantico['char']['float']['=='] = 'error' 
cuboSemantico['float']['char']['=='] = 'error'  # float con char

cuboSemantico['float']['float']['=='] = 'bool'  # float con float

cuboSemantico['char']['char']['=='] = 'bool' # char con char

##############################################################
############################################################


def getType( left,right, operator):
	return cuboSemantico[left][right][operator]



# def main():
# 	getType('float', 'float', '+')


# main()
