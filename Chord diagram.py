import pandas as pd
import numpy as np
from plotapi import Chord
df = pd.read_csv('/Users/lijieyi/Desktop/Business_model/Results/document_cluster_Top2Vec_doc2vec_value_proposition.csv')

topic_words = pd.read_csv('/Users/lijieyi/Desktop/Business_model/Results/document_cluster_Top2Vec_doc2vec_topic_words_value_proposition.csv')

df_filtered = df[df['HPC_healthcare'].isin(['YY', 'NY'])]


topics = df_filtered['Topic'].unique()
transition_matrix = pd.DataFrame(0, index=topics, columns=topics)

# for each cik_str group，check transfer from NN to YY
for cik, group in df_filtered.groupby('cik_str'):
    if 'NY' in group['HPC_healthcare'].values and 'YY' in group['HPC_healthcare'].values:
        ny_rows = group[group['HPC_healthcare'] == 'NY']
        yy_rows = group[group['HPC_healthcare'] == 'YY']

        for _, ny_row in ny_rows.iterrows():
            for _, yy_row in yy_rows.iterrows():
                prev_topic = ny_row['Topic']
                current_topic = yy_row['Topic']
                transition_matrix.at[prev_topic, current_topic] += 1

transition_matrix.columns = transition_matrix.columns.astype(int)
transition_matrix.index = transition_matrix.index.astype(int)

# sort it based on row and column
transition_matrix = transition_matrix.sort_index(axis=0).sort_index(axis=1)
transition_matrix = np.array(transition_matrix).tolist()
data_list = topic_words['topic_words_short'].tolist()
Chord.api_key("xxx")
chord_diagram = Chord(transition_matrix, data_list,font_size_large="38px",directed=True,reverse_gradients=True,wrap_labels=True,width=2000,margin=350)
# chord_diagram = Chord(transition_matrix, data_list,font_size_large="16px",directed=True,reverse_gradients=True,colored_diagonals=False,wrap_labels=True,width=2000,margin=350)

chord_diagram.show()
