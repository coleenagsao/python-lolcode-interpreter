# Semantics Analyzer Implementation
import grab_lexeme

lexemeArr = []
symbolTable = []


def grab_identifiers(symbolTable):
    identifiers = []

    for i in symbolTable:
        identifiers.append(i[0])

    return identifiers


# function that checks if identifier already exists. If not, append. If existing, update the symbol table
def insertToTable(testing_list, symbolTable, index, data_type, new_identifier, new_value):
    if new_identifier not in grab_identifiers(symbolTable):
        symbolTable.append([testing_list[index+1][0], new_value, data_type])
    else:
        dupIndex = grab_identifiers(symbolTable).index(
            testing_list[index+1][0])
        del symbolTable[dupIndex]
        symbolTable.insert(
            dupIndex, [testing_list[index+1][0], new_value, data_type])


def grab_symbol_table(lexemeArr):
    testing_list = []

    for i in lexemeArr:
        # print(i)
        testing_list.append(i)

    for index, i in enumerate(testing_list):
        # Variable initialization
        if (i[0] == "I HAS A" and (index+1) < len(testing_list)):
            if testing_list[index+1][1] == "Variable Identifier":
                if (index + 2) < len(testing_list):
                    if testing_list[index+2][0] != "ITZ":
                        insertToTable(testing_list, symbolTable,
                                      index, "NOOB", testing_list[index+1][0], "")
                elif (index + 2) == len(testing_list):
                    insertToTable(testing_list, symbolTable,
                                  index, "NOOB", testing_list[index+1][0], "")

        # Variable initialization (Case 1.1: Literal is NUMBR, NUMBAR, TROOF)
        if (i[0] == "I HAS A" and (index+3) < len(testing_list)):
            if (testing_list[index+1][1] == "Variable Identifier" and testing_list[index+2][0] == "ITZ"):
                if testing_list[index+3][1] in ["NUMBR Literal", "NUMBAR Literal", "TROOF Literal"]:
                    #del testing_list[index:(index+2)]
                    insertToTable(testing_list, symbolTable,
                                  index, testing_list[index+3][1], testing_list[index+1][0], testing_list[index+3][0])
        # Variable initialization (Case 1.2: YARN Literal)
        if (i[0] == "I HAS A" and (index+5) < len(testing_list)):
            if (testing_list[index+1][1] == "Variable Identifier" and testing_list[index+2][0] == "ITZ"):
                if testing_list[index+3][1] == "String Delimiter" and testing_list[index+4][1] == "YARN Literal" and testing_list[index+5][1] == "String Delimiter":
                    insertToTable(testing_list, symbolTable, index, testing_list[index+1][1],
                                  testing_list[index+1][0], testing_list[index+4][0])

    for i in symbolTable:
        print(i)

    return symbolTable


def lex_analyze(lexemeArr, the_long_string):
    lexemeArr.clear()

    lines = the_long_string.split("\n")

    lines2 = []
    for line in lines:
        if (line != ""):
            lines2.append(line.strip())

    for i in range(0, len(lines2)):
        while (lines2[i] != ''):
            grab_lexeme.get_lexemes(lexemeArr, lines2, lines2[i], i)

    grab_symbol_table(lexemeArr)


# temp: test cases
k = "HAI I HAS A monde KTHXBYE"
g = """HAI
    I HAS A monde
    I HAS A num ITZ 17
    I HAS A num ITZ 18
    I HAS A name ITZ "seventeen"
    I HAS A fnum ITZ 17.0
    I HAS A flag ITZ WIN

KTHXBYE"""
h = """HAI

    I HAS A monde
    I HAS A num ITZ 17
    I HAS A name ITZ "seventeen"
    I HAS A fnum ITZ 17.0
    I HAS A flag ITZ WIN

KTHXBYE
"""

lex_analyze(lexemeArr, g)
