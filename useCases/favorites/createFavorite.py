from interfaces.create import CreateStrategy
from bson import ObjectId

class AddToFavoritesStrategy(CreateStrategy):
    def create(self, db) -> bool:
        print("\nAdicionar produto aos favoritos")
        
        
        user_cpf = input("Digite o CPF do usuário: ")
        user = db.usuarios.find_one({"cpf": user_cpf})
        
        if not user:
            print("Usuário não encontrado!")
            return False
        
        
        search_term = input("Buscar produto pelo nome: ")
        if not search_term:
            print("É necessário informar um termo de busca!")
            return False
        
        
        products = list(db.produtos.find(
            {"nome": {"$regex": search_term, "$options": "i"}}
        ))
        
        if not products:
            print("Nenhum produto encontrado com esse termo!")
            return False
        
        
        print("\nProdutos encontrados:")
        for idx, prod in enumerate(products, 1):
            print(f"{idx}. {prod.get('nome')} - R$ {prod.get('valor'):.2f}")
        
        
        try:
            prod_idx = int(input("\nDigite o número do produto para adicionar aos favoritos: ")) - 1
            if 0 <= prod_idx < len(products):
                selected_product = products[prod_idx]
                
                
                product_id = str(selected_product.get("_id"))
                product_summary = {
                    "id": product_id,
                    "nome": selected_product.get("nome"),
                    "valor": selected_product.get("valor")
                }
                
                
                current_favorites = user.get("favorites", [])
                for fav in current_favorites:
                    if fav.get("id") == product_id:
                        print("Este produto já está na lista de favoritos!")
                        return False
                
                
                if "favorites" not in user:
                    db.usuarios.update_one(
                        {"_id": user.get("_id")},
                        {"$set": {"favorites": [product_summary]}}
                    )
                else:
                    db.usuarios.update_one(
                        {"_id": user.get("_id")},
                        {"$push": {"favorites": product_summary}}
                    )
                
                print(f"Produto '{selected_product.get('nome')}' adicionado aos favoritos com sucesso!")
                return True
            else:
                print("Índice de produto inválido!")
                return False
        except ValueError:
            print("Entrada inválida!")
            return False