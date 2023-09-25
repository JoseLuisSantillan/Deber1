
flag = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}"

AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
az = "abcdefghijklmnopqrstuvwxyz"

# string to store result
result = ""

for x in flag:
    if x in AZ:
        result += AZ[(AZ.index(x)+13)%len(AZ)]
    elif x in az:
        result += az[(az.index(x)+13)%len(az)]
    else:
        result += x
print(result)