#%%
from library_management import *



# %%
library.book_state('reglamento')
# %%
library.add_book('La odisea')
# %%
user.get_book('reglamento')
# %%
user.return_book('reglamento')
# %%
user.display_book()
# %%
