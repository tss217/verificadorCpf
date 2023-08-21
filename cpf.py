def replaceCpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    return cpf

def checkYY(cpf):
    sliceCpf = cpf[:-2]
    numberList = []
    i = 10
    for x in sliceCpf:
        math = int(x) * i
        numberList.append(math)
        i -= 1
    suma = sum(numberList)
    resto = suma % 11
    if resto < 2:
        return 0
    else:
        return 11 - resto

def checkZZ(cpf, yy):
    sliceCpf = cpf[:-2] + str(yy)
    numberList = []
    i = 11
    for x in sliceCpf:
        math = int(x) * i
        numberList.append(math)
        i -= 1
    suma = sum(numberList)
    resto = suma % 11
    if resto < 2:
        return 0
    else:
        return 11 - resto

cpf = ""
newCpf = replaceCpf(cpf)
yy = checkYY(newCpf)
zz = checkZZ(newCpf, yy)

original_yy = int(newCpf[-2])
original_zz = int(newCpf[-1])

if yy == original_yy and zz == original_zz:
    print("CPF é válido.")
else:
    print("CPF é inválido.")
