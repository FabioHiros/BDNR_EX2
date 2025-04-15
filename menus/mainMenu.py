from menus.userMenu import userMenu
from dbConnection import connect_db
from menus.productMenu import productMenu
from menus.ordersMenu import OrderMenu
from menus.favoriteMenu import FavoteMenu
def mainMenu():
    db = connect_db()
    while (True):
        print("""
                ##### Menu Principal #####
                    1- CRUD Usuário
                    2- CRUD Compras
                    3- CRUD Produto
                    4- CRUD Favoritos
            """)
        option = input('Digite a  opção desejada (S para sair):  ')

        match option:
            case '1':
                userMenu(db)
            case '3':
                productMenu(db)
            case '2':
                OrderMenu(db)
            case '4':
                FavoteMenu(db)


