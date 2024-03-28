from pypdf import PdfReader, mult
import os
import re

path = "data/Anexo_I_Rol_2021RN_465.2021_RN599_RN600.pdf"

forbidden_set = {
	"Rol de Procedimentos e Eventos em Saúde",
	"(RN 465/2021, vigente a partir de 01/04/2021, e suas alterações)",
	"(alteração)",
	"Legenda: ",
	"OD: Seg. Odontológica",
	"AMB: Seg. Ambulatorial",
	"HCO: Seg. Hospitalar Com Obstetrícia",
	"HSO: Seg. Hospitalar Sem Obstetrícia",
	"REF: Plano Referência",
	"PAC: Procedimento de Alta Complexidade",
	"DUT: Diretriz de Utilização ",
}

reader = PdfReader(path)

parts = list()

def visitor_body(text, cm, tm, font_dict, font_size):
	m = mult(tm, cm)

	if text not in forbidden_set:
		parts.append([m, text.strip()])


for i in range(2, 180):
	page = reader.pages[i]
	page.extract_text(visitor_text=visitor_body)


for i, part in enumerate(parts):
	text = part[1]
	if text != "" and text != "\n" and part[0][4] == 0.0:
		parts[i+1][1] = text
		parts.pop(i)

parts = list(filter(lambda x: x[1] != "", parts))

aux_list = list()
coord_x = 0

for i, part in enumerate(parts):
	if i == 0:
		aux_list.append(part)
		coord_x = part[0][4]
		continue
	elif part[0][4] == coord_x:
		aux_list[-1][1] = f"{aux_list[-1][1]} {part[1]}"
	else:
		coord_x = part[0][4]
		aux_list.append(part)

aux_list = list(filter(lambda x: x[0][5] < 504.0 and x[0][5] > 25.0, aux_list))

for part in aux_list:
	part[1] = part[1].replace(';', ',')

header = "Procedimento;RN;Vigência;OD;AMB;HCO;HSO;REF;PAC;DUT;SUBGRUPO;GRUPO;CAPÍTULO\n"

for part in aux_list:
	print(part)

with open("data.csv", "w") as file:
	file.write(header)

	ls = ["" for i in range(13)]
	for part in aux_list:
		if part[0][4] < 45.0 and part[0][4] > 44.0:
			ls[0] = part[1]
		elif part[0][4] < 355.0 and part[0][4] > 354.0:
			ls[1] = part[1]
		elif part[0][4] < 390.0 and part[0][4] > 389.0:
			ls[2] = part[1]
		elif part[1] == "OD":
			ls[3] = "Seg. Odontológica"
		elif part[1] == "AMB":
			ls[4] = "Seg. Ambulatorial"
		elif part[1] == "HCO":
			ls[5] = "HCO"
		elif part[1] == "HSO":
			ls[6] = "HSO"
		elif part[1] == "REF":
			ls[7] = "REF"
		elif part[1] == "PAC":
			ls[8] = "PAC"
		elif re.match(r"\d{1, 2, 3}", part[1]):
			ls[9] = part[1]
		elif part[0][4] < 581.0 and part[0][4] > 580.0:
			ls[10] = part[1]
		elif part[0][4] < 710.0 and part[0][4] > 709.0:
			ls[11] = part[1]
		elif part[0][4] < 838.0 and part[0][4] > 837.0:
			ls[12] = part[1]
			final_string = ";".join(ls)
			file.write(f"{final_string}\n")
			ls = ["" for i in range(13)]
