# requires kaleido to save the image to a file:
# pip install -U kaleido

import pandas as pd
import plotly.express as px

dict_num_bacterial_genomes_in_each_phyla = {
    "Firmicutes": 1831,
    "Actinobacteria": 550,
    "Bacteroidota": 511,
    "Proteobacteria": 184,
    "Campylobacterota": 74,
    "Fusobacteriota": 39,
    "Cyanobacteriota": 35,
    "Verrucomicrobiota": 25,
    "Desulfobacterota": 21,
    "Patescibacteria": 8,
    "Spirochaetota": 6,
    "Elusimicrobiota": 5,
    "Synergistota": 4
}

# create Dataframe from a list of key, value pairs
df = pd.DataFrame(list(dict_num_bacterial_genomes_in_each_phyla.items()), 
                  columns = ['phyla','num_genomes'])

fig = px.treemap(df, 
                 path=[px.Constant("Human Gut Bacterial Genomes 3293"), "phyla"], 
                 values="num_genomes",
                 title="A TREEmap of gut FLORA:  In the study, 3,293 genomes were classified into 13 phyla.")

fig.update_traces(root_color="lightgrey")
fig.update_traces(textinfo="label+value")

# This is the white box outside the treemap
fig.update_layout(margin = dict(t=50, l=5, r=5, b=40))

fig.update_layout(
    title_font_family="Times New Roman",
    title_font_size=18,
    title_x=0.01,
    title_yanchor="top"
)

fig.add_annotation(text="Data Source: https://www.biorxiv.org/content/10.1101/2020.09.24.311720v1.full  |  Data Viz: @roannav",
                   yanchor="top",
                   x=0,
                   y = -0.02,
                   showarrow=False)

fig.write_image("day04_flora.png")
