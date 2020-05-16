import sys
from collections import defaultdict

#cubo semantico sirve para cuando se hacen operaciones aritmeticas, logicas, comparaciones, asignaciones

#para inicializar el dicionario, defaultdict es una clase de colections
cuboSemantico = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))
	
#################################################################
############ PLUS ##################################################
cuboSemantico['int']['int']['+'] = 'int' #int con int

cuboSemantico['int']['float']['+'] = 'float' # int con float
cuboSemantico['float']['int']['+'] = 'float'

cuboSemantico['int']['char']['+'] = 'error' # int con char
cuboSemantico['char']['int']['+'] = 'error'

cuboSemantico['char']['float']['+'] = 'error' 
cuboSemantico['float']['char']['+'] = 'error'  # float con char

cuboSemantico['float']['float']['+'] = 'float'  # float con float

cuboSemantico['char']['char']['+'] = 'error' # char con char

#################################################################
############ MINUS ####################################################
cuboSemantico['int']['int']['-'] = 'int' #int con int

cuboSemantico['int']['float']['-'] = 'float' # int con float
cuboSemantico['float']['int']['-'] = 'float'

cuboSemantico['int']['char']['-'] = 'error' # int con char
cuboSemantico['char']['int']['-'] = 'error'

cuboSemantico['char']['float']['-'] = 'error' 
cuboSemantico['float']['char']['-'] = 'error'  # float con char

cuboSemantico['float']['float']['-'] = 'float'  # float con float

cuboSemantico['char']['char']['-'] = 'error' # char con char


#################################################################
############# MULTIPLICATION ######################
cuboSemantico['int']['int']['+'] = 'int' #int con int

cuboSemantico['int']['float']['+'] = 'float' # int con float
cuboSemantico['float']['int']['+'] = 'float'

cuboSemantico['int']['char']['+'] = 'error' # int con char
cuboSemantico['char']['int']['+'] = 'error'

cuboSemantico['char']['float']['+'] = 'error' 
cuboSemantico['float']['char']['+'] = 'error'  # float con char

cuboSemantico['float']['float']['+'] = 'float'  # float con float

cuboSemantico['char']['char']['+'] = 'error' # char con char





