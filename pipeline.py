
with open('C:/Users/bonna/Downloads/StockUniteLegaleHistorique_utf8/StockUniteLegaleHistorique_utf8.csv', encoding='utf-8') as f:
     for i in range(100):
        ligne = f.readline()
        if not ligne:
            break  # fin du fichier atteinte avant 100 lignes
        print(ligne.strip())