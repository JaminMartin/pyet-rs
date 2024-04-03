from pyet.structure import Structure
import os
from pyet_rs import doper_seq
import pandas as pd

cif_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'cif_files'))
cif_file = os.path.join(cif_dir, 'KY3F10.cif')
KY3F10 = Structure(cif_file= cif_file)
KY3F10.centre_ion('Y3+')

coords = KY3F10.nearest_neighbours_spherical_coords(40)
filtered_coords = coords.loc[coords['species'].isin([KY3F10.centre_ion_species])].reset_index(drop=True)

for i in range(100):
    l = doper_seq(len(filtered_coords), 50.0)
    filtered_coords['species'] = pd.Series(l)

