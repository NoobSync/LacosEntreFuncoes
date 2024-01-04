import layout_menu, limpar_console

limpar_console.cls()

def menu_principal():
    layout_menu.m_layout()
    menu_principal_check()

def menu_principal_check():
    seletor = input(layout_menu.option)
    if seletor == '1':
         limpar_console.cls()
         layout_menu.item_1()
         loop_menu()
    elif seletor == '2' :
         limpar_console.cls()
         layout_menu.item_2()
         loop_menu()
    elif seletor == '3' :
         limpar_console.cls()
         layout_menu.item_3()
         loop_menu()
    elif seletor == '0' :
         limpar_console.cls()
         print ('')
    else:
         limpar_console.cls()
         print(layout_menu.m_erro)
         menu_principal()
         
def loop_menu():
     layout_menu.m_layout_2()
     loop_menu_check()

def loop_menu_check():
     seletor = input(layout_menu.option)
     limpar_console.cls()
     if seletor == '1':
          menu_principal()
     elif seletor == '0':
          print ('')
     else:
          print(layout_menu.m_erro)
          loop_menu()

          

menu_principal()