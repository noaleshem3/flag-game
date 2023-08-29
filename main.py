import functions
import bombs
matrix = functions.creating_matrix()
list_index_bombs, list_index_grass = bombs.rand_bombs(matrix)
cord_bombs = functions.trans_index_to_cordinata(list_index_bombs)
cord_grass = functions.trans_index_to_cordinata(list_index_grass)
# matrix = creating_matrix()
# matrix = add_flag(matrix)
# for row in matrix:
#     print(row)



